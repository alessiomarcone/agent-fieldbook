#!/usr/bin/env python3
"""
Check official Anthropic and OpenAI learning indexes for material not yet
cataloged in this repository.

Checks:
  1. https://claude.com/resources/courses   vs knowledge/claude/courses.csv
  2. https://claude.com/resources/tutorials vs knowledge/claude/tutorials.csv
  3. Codex learning catalog link health
  4. Official Anthropic YouTube count       vs .github/state.json (needs yt-dlp)

Usage:
    python3 check_official_sources.py            # human-readable report
    python3 check_official_sources.py --json     # machine-readable report
    python3 check_official_sources.py --update-state  # persist YouTube count for CI

Exit code is always 0; the report contains "NEW_ITEMS_FOUND" when something
new was detected, so CI can grep for it.
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import re
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CLAUDE_KNOWLEDGE = ROOT / "knowledge" / "claude"
STATE_FILE = ROOT / ".github" / "state.json"
USER_AGENT = "agent-fieldbook-checker (+https://github.com/alessiomarcone/agent-fieldbook)"

INDEXES = [
    {
        "name": "courses",
        "url": "https://claude.com/resources/courses",
        "csv": CLAUDE_KNOWLEDGE / "courses.csv",
        "link_patterns": [
            r"https?://anthropic\.skilljar\.com/[a-z0-9/_-]+",
        ],
    },
    {
        "name": "tutorials",
        "url": "https://claude.com/resources/tutorials",
        "csv": CLAUDE_KNOWLEDGE / "tutorials.csv",
        "link_patterns": [
            r"https?://claude\.com/resources/tutorials/[a-z0-9-]+",
            r"/resources/tutorials/[a-z0-9-]+",
        ],
    },
]

CHANNEL_URL = "https://www.youtube.com/@anthropic-ai/videos"


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def normalize(url: str) -> str:
    url = url.strip().rstrip("/")
    if url.startswith("/"):
        url = "https://claude.com" + url
    return url.lower()


def known_urls_from_csv(csv_path: Path) -> set[str]:
    known: set[str] = set()
    with csv_path.open(encoding="utf-8-sig") as fh:
        for row in csv.DictReader(fh):
            url = (row.get("URL") or "").strip()
            if url:
                known.add(normalize(url))
    return known


def check_index(index: dict) -> dict:
    result = {
        "name": index["name"],
        "catalog": str(index["csv"].relative_to(ROOT)),
        "status": "ok",
        "new": [],
        "found": 0,
    }
    try:
        html = fetch(index["url"])
    except Exception as exc:  # noqa: BLE001
        result["status"] = f"fetch_error: {exc}"
        return result

    found: set[str] = set()
    for pattern in index["link_patterns"]:
        for match in re.findall(pattern, html, flags=re.IGNORECASE):
            found.add(normalize(match))
    result["found"] = len(found)

    if not found:
        # Page structure probably changed (JS-rendered or redesigned):
        # report that instead of a false "nothing new".
        result["status"] = "page_structure_changed"
        return result

    known = known_urls_from_csv(index["csv"])
    # Skilljar paths like /path/<slug> and /<slug> refer to the same course.
    known_slugs = {u.rsplit("/", 1)[-1] for u in known}
    for url in sorted(found):
        if url in known:
            continue
        if url.rsplit("/", 1)[-1] in known_slugs:
            continue
        result["new"].append(url)
    return result


def check_catalog_links(name: str, csv_path: Path) -> dict:
    result = {
        "name": name,
        "catalog": str(csv_path.relative_to(ROOT)),
        "status": "ok",
        "new": [],
        "found": 0,
        "unreachable": [],
    }
    try:
        with csv_path.open(encoding="utf-8-sig", newline="") as handle:
            urls = [
                (row.get("URL") or "").strip()
                for row in csv.DictReader(handle)
                if (row.get("URL") or "").strip()
            ]
    except Exception as exc:  # noqa: BLE001
        result["status"] = f"catalog_error: {exc}"
        return result

    for url in urls:
        try:
            fetch(url)
        except Exception as exc:  # noqa: BLE001
            result["unreachable"].append(f"{url} ({exc})")
    result["found"] = len(urls) - len(result["unreachable"])
    if result["unreachable"]:
        result["status"] = "unreachable_links"
    return result


def check_youtube(*, update_state: bool = False) -> dict:
    result = {"name": "youtube", "status": "ok", "count": None, "previous": None}
    executable = shutil.which("yt-dlp")
    if executable:
        command = [executable]
    elif importlib.util.find_spec("yt_dlp") is not None:
        command = [sys.executable, "-m", "yt_dlp"]
    else:
        result["status"] = "yt-dlp_not_installed"
        return result
    try:
        proc = subprocess.run(
            [*command, "--flat-playlist", "--dump-single-json", CHANNEL_URL],
            capture_output=True, text=True, timeout=300, check=True,
        )
        data = json.loads(proc.stdout)
        result["count"] = len(data.get("entries") or [])
    except Exception as exc:  # noqa: BLE001
        result["status"] = f"error: {exc}"
        return result

    state = {}
    if STATE_FILE.exists():
        state = json.loads(STATE_FILE.read_text(encoding="utf-8"))
    result["previous"] = state.get("youtube_video_count")

    if update_state:
        state["youtube_video_count"] = result["count"]
        STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
        STATE_FILE.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    parser.add_argument(
        "--update-state",
        action="store_true",
        help="Persist the current YouTube count to .github/state.json.",
    )
    args = parser.parse_args()

    reports = [check_index(index) for index in INDEXES]
    reports.append(
        check_catalog_links(
            "codex_learning",
            ROOT / "knowledge" / "codex" / "learning-resources.csv",
        )
    )
    yt = check_youtube(update_state=args.update_state)
    reports.append(yt)

    new_items = any(r.get("new") for r in reports)
    yt_changed = (
        yt["status"] == "ok"
        and yt["previous"] is not None
        and yt["count"] != yt["previous"]
    )
    source_issues = [
        r
        for r in reports
        if r["status"] not in ("ok",) and r["name"] != "youtube"
    ]

    if args.json:
        print(
            json.dumps(
                {
                    "reports": reports,
                    "new_items": new_items,
                    "youtube_changed": yt_changed,
                    "source_issues": bool(source_issues),
                },
                indent=2,
            )
        )
        return 0

    print("# Official sources check\n")
    for r in reports:
        if r["name"] == "youtube":
            if r["status"] != "ok":
                print(f"- YouTube: SKIPPED ({r['status']})")
            elif yt_changed:
                print(f"- YouTube: video count changed {r['previous']} -> {r['count']}"
                      " — run `python3 update_youtube_catalog.py`")
            elif r["previous"] is None:
                print(f"- YouTube: {r['count']} videos (no previous baseline)")
            else:
                print(f"- YouTube: {r['count']} videos, unchanged")
            continue
        if r["name"] == "codex_learning":
            if r["status"] == "ok":
                print(f"- codex_learning: {r['found']} official links reachable")
            else:
                print(
                    f"- codex_learning: CHECK MANUALLY "
                    f"({len(r['unreachable'])} unreachable link(s))"
                )
                for item in r["unreachable"]:
                    print(f"    - {item}")
            continue
        if r["status"] != "ok":
            print(f"- {r['name']}: CHECK MANUALLY ({r['status']})")
        elif r["new"]:
            print(
                f"- {r['name']}: {len(r['new'])} item(s) not in "
                f"{r['catalog']}:"
            )
            for url in r["new"]:
                print(f"    - {url}")
        else:
            print(f"- {r['name']}: {r['found']} links found, all cataloged")

    if new_items or yt_changed:
        print("\nNEW_ITEMS_FOUND")
    if source_issues:
        print("\nSOURCE_CHECK_FAILED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
