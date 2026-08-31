#!/usr/bin/env python3
"""
Check official Anthropic and OpenAI learning indexes for material not yet
cataloged in this repository.

Checks:
  1. Claude Academy sitemap    vs knowledge/claude/courses.csv
  2. Claude Academy sitemap    vs knowledge/claude/tutorials.csv
  3. Link health of every cataloged Claude and Codex URL
  4. Official Anthropic YouTube count vs .github/state.json (needs yt-dlp)

The sitemap at https://academy.claude.com/sitemap.xml is the source of truth:
the /courses and /tutorials index pages render only a curated subset, so
scraping them under-reports the catalog.

Which material belongs in the catalog is declared in
knowledge/claude/catalog-scope.json. Slugs matching an `exclude` pattern there
are counted and reported as out of scope, but never raise an alert.

Usage:
    python3 check_official_sources.py                  # human-readable report
    python3 check_official_sources.py --json           # machine-readable report
    python3 check_official_sources.py --update-state   # persist YouTube count for CI
    python3 check_official_sources.py --skip-link-check # skip per-URL link health

Exit code is always 0. The report carries two independent signals so CI can
route them separately:
  CATALOG_UPDATE_NEEDED  official material changed; the catalog needs an edit
  SOURCE_CHECK_FAILED    the checker itself could not read a source
"""
from __future__ import annotations

import argparse
import concurrent.futures
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
CODEX_KNOWLEDGE = ROOT / "knowledge" / "codex"
SCOPE_FILE = CLAUDE_KNOWLEDGE / "catalog-scope.json"
STATE_FILE = ROOT / ".github" / "state.json"
USER_AGENT = "agent-fieldbook-checker (+https://github.com/alessiomarcone/agent-fieldbook)"

ACADEMY = "https://academy.claude.com"
CHANNEL_URL = "https://www.youtube.com/@anthropic-ai/videos"
LINK_CHECK_WORKERS = 8

CATALOGS = {
    "courses": CLAUDE_KNOWLEDGE / "courses.csv",
    "tutorials": CLAUDE_KNOWLEDGE / "tutorials.csv",
    "codex_learning": CODEX_KNOWLEDGE / "learning-resources.csv",
}


def fetch(url: str, *, head: bool = False) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    if head:
        request.get_method = lambda: "HEAD"
    with urllib.request.urlopen(request, timeout=30) as response:
        return "" if head else response.read().decode("utf-8", errors="replace")


def normalize(url: str) -> str:
    url = url.strip().rstrip("/")
    if url.startswith("/resources/tutorials"):
        url = ACADEMY + url.replace("/resources/tutorials", "/tutorials", 1)
    elif url.startswith("/resources/courses"):
        url = ACADEMY + url.replace("/resources/courses", "/courses", 1)
    elif url.startswith("/"):
        url = ACADEMY + url
    return url.lower()


def load_scope() -> dict:
    return json.loads(SCOPE_FILE.read_text(encoding="utf-8"))


def catalog_urls(csv_path: Path) -> list[str]:
    with csv_path.open(encoding="utf-8-sig", newline="") as handle:
        return [
            (row.get("URL") or "").strip()
            for row in csv.DictReader(handle)
            if (row.get("URL") or "").strip()
        ]


def slug_of(url: str) -> str:
    return normalize(url).rsplit("/", 1)[-1]


def sitemap_slugs(sitemap_url: str) -> dict[str, set[str]]:
    """Top-level /courses/<slug> and /tutorials/<slug> entries from the sitemap."""
    xml = fetch(sitemap_url)
    locations = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", xml)
    found: dict[str, set[str]] = {"courses": set(), "tutorials": set()}
    for location in locations:
        match = re.fullmatch(
            re.escape(ACADEMY) + r"/(courses|tutorials)/([a-z0-9-]+)", location.rstrip("/")
        )
        if match:
            found[match.group(1)].add(match.group(2))
    return found


def check_section(name: str, config: dict, published: set[str]) -> dict:
    csv_path = CATALOGS[name]
    result = {
        "name": name,
        "catalog": str(csv_path.relative_to(ROOT)),
        "status": "ok",
        "published": len(published),
        "in_scope": 0,
        "out_of_scope": 0,
        "cataloged": 0,
        "new": [],
        "retired": [],
    }
    if not published:
        # No entries at all means the sitemap moved or changed shape; say so
        # instead of reporting a falsely clean catalog.
        result["status"] = "sitemap_structure_changed"
        return result

    excludes = [re.compile(pattern) for pattern in config.get("exclude", [])]
    in_scope = {s for s in published if not any(p.search(s) for p in excludes)}
    result["in_scope"] = len(in_scope)
    result["out_of_scope"] = len(published) - len(in_scope)

    cataloged = {slug_of(url) for url in catalog_urls(csv_path)}
    result["cataloged"] = len(cataloged)
    result["new"] = sorted(in_scope - cataloged)
    result["retired"] = sorted(cataloged - published)
    return result


def check_link_health(name: str, csv_path: Path) -> dict:
    result = {
        "name": name,
        "catalog": str(csv_path.relative_to(ROOT)),
        "status": "ok",
        "checked": 0,
        "unreachable": [],
    }
    try:
        urls = catalog_urls(csv_path)
    except Exception as exc:  # noqa: BLE001
        result["status"] = f"catalog_error: {exc}"
        return result

    def probe(url: str) -> tuple[str, str | None]:
        try:
            fetch(url, head=True)
        except Exception as head_error:  # noqa: BLE001
            try:  # some hosts reject HEAD but serve GET
                fetch(url)
            except Exception as exc:  # noqa: BLE001
                return url, f"{exc} (HEAD: {head_error})"
        return url, None

    with concurrent.futures.ThreadPoolExecutor(LINK_CHECK_WORKERS) as pool:
        for url, error in pool.map(probe, urls):
            if error:
                result["unreachable"].append(f"{url} ({error})")
    result["checked"] = len(urls)
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


def build_report(*, update_state: bool, skip_link_check: bool) -> dict:
    scope = load_scope()
    sections: list[dict] = []
    try:
        published = sitemap_slugs(scope["sitemap"])
    except Exception as exc:  # noqa: BLE001
        published = None
        for name in scope["sections"]:
            sections.append(
                {"name": name, "catalog": str(CATALOGS[name].relative_to(ROOT)),
                 "status": f"sitemap_fetch_error: {exc}", "new": [], "retired": []}
            )
    if published is not None:
        for name, config in scope["sections"].items():
            sections.append(check_section(name, config, published.get(name, set())))

    links = []
    if not skip_link_check:
        links = [check_link_health(name, path) for name, path in CATALOGS.items()]

    youtube = check_youtube(update_state=update_state)
    youtube_changed = (
        youtube["status"] == "ok"
        and youtube["previous"] is not None
        and youtube["count"] != youtube["previous"]
    )
    catalog_update_needed = youtube_changed or any(
        section.get("new") or section.get("retired") for section in sections
    )
    check_failed = any(s["status"] != "ok" for s in sections) or any(
        link["status"] != "ok" for link in links
    )
    return {
        "sections": sections,
        "links": links,
        "youtube": youtube,
        "youtube_changed": youtube_changed,
        "catalog_update_needed": catalog_update_needed,
        "check_failed": check_failed,
    }


def print_report(report: dict) -> None:
    print("# Official sources check\n")
    print("## Catalog coverage")
    for section in report["sections"]:
        if section["status"] != "ok":
            print(f"- {section['name']}: CHECK MANUALLY ({section['status']})")
            continue
        print(
            f"- {section['name']}: {section['published']} published "
            f"({section['in_scope']} in scope, {section['out_of_scope']} out of scope), "
            f"{section['cataloged']} cataloged"
        )
        for url in section["new"]:
            print(f"    + not cataloged: {url}")
        for url in section["retired"]:
            print(f"    - cataloged but no longer published: {url}")

    if report["links"]:
        print("\n## Link health")
        for link in report["links"]:
            if link["status"] == "ok":
                print(f"- {link['name']}: {link['checked']} links reachable")
            else:
                print(f"- {link['name']}: CHECK MANUALLY ({link['status']})")
                for item in link["unreachable"]:
                    print(f"    - {item}")

    print("\n## YouTube")
    youtube = report["youtube"]
    if youtube["status"] != "ok":
        print(f"- SKIPPED ({youtube['status']})")
    elif report["youtube_changed"]:
        print(f"- video count changed {youtube['previous']} -> {youtube['count']}"
              " — run `python3 update_youtube_catalog.py`")
    elif youtube["previous"] is None:
        print(f"- {youtube['count']} videos (no previous baseline)")
    else:
        print(f"- {youtube['count']} videos, unchanged")

    if report["catalog_update_needed"]:
        print("\nCATALOG_UPDATE_NEEDED")
    if report["check_failed"]:
        print("\nSOURCE_CHECK_FAILED")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    parser.add_argument(
        "--update-state",
        action="store_true",
        help="Persist the current YouTube count to .github/state.json.",
    )
    parser.add_argument(
        "--skip-link-check",
        action="store_true",
        help="Skip per-URL link health probing.",
    )
    args = parser.parse_args()

    report = build_report(
        update_state=args.update_state, skip_link_check=args.skip_link_check
    )
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print_report(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
