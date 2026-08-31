#!/usr/bin/env python3
"""Apply the mechanical half of a catalog update, and only that half.

`check_official_sources.py` reports what changed upstream. This script writes
the part of the answer that needs no judgment: it appends new rows with the
title, duration, lesson count, and quiz count read from the source page, and
moves rows Anthropic no longer publishes into `retired-sources.md`.

The columns that need judgment — the Italian `Categoria`, `Obiettivo`, and
`Perché è utile` — are filled with a `TODO:` marker. A catalog carrying any
`TODO:` is incomplete by construction, which is what keeps a generated pull
request from being merged unattended.

Usage:
    python3 scripts/apply_catalog_updates.py            # write the changes
    python3 scripts/apply_catalog_updates.py --dry-run  # report, change nothing
    python3 scripts/apply_catalog_updates.py --max-new 10

Exit codes:
    0  changes written (or nothing to do)
    2  refused: more new items than --max-new, or a source could not be read

Exit 2 means a human should look. A bulk upstream change — a site migration,
a section launch — is exactly the case where an unattended edit is wrong.
"""
from __future__ import annotations

import argparse
import csv
import html
import io
import json
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import check_official_sources as checker  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
RETIRED = ROOT / "knowledge" / "claude" / "retired-sources.md"
MANIFEST = ROOT / "manifest.json"
TODO = "TODO: da scrivere a mano"

# "13 lessons · 2.5 hr · 1 quiz" on a course page, separated by icon glyphs.
COURSE_META_RE = re.compile(
    r"(\d+)\s+lessons?\s*\S?\s*([\d.]+\s*(?:hr|min))(?:\s*\S?\s*(\d+)\s+quiz)?"
)
DURATION_RE = re.compile(r"\b(\d+)\s*(hr|min)\b")


def page_text(url: str) -> str:
    raw = checker.fetch(url)
    stripped = re.sub(r"<script.*?</script>|<style.*?</style>", " ", raw, flags=re.S)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", stripped))).strip()


def page_title(text: str) -> str:
    return re.sub(r"\s*·.*$", "", text.split(" Claude Academy")[0]).strip()


def course_metadata(slug: str) -> dict[str, str]:
    text = page_text(f"{checker.ACADEMY}/courses/{slug}")
    match = COURSE_META_RE.search(text)
    if not match:
        raise ValueError(f"could not read lessons/duration for course {slug}")
    return {
        "title": page_title(text),
        "lessons": match.group(1),
        "duration": re.sub(r"\s+", " ", match.group(2)),
        "quiz": match.group(3) or "0",
    }


def tutorial_metadata(slug: str) -> dict[str, str]:
    text = page_text(f"{checker.ACADEMY}/tutorials/{slug}")
    title = page_title(text)
    if not title:
        raise ValueError(f"could not read title for tutorial {slug}")
    duration = DURATION_RE.search(text)
    return {"title": title, "duration": duration.group(0) if duration else ""}


def read_catalog(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def write_catalog(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    path.write_text(buffer.getvalue(), encoding="utf-8-sig")


def append_retired(entries: list[tuple[str, str]]) -> None:
    """Record retired material instead of deleting it."""
    text = RETIRED.read_text(encoding="utf-8")
    start, end = "<!-- retired:start -->", "<!-- retired:end -->"
    head, _, rest = text.partition(start)
    body, _, tail = rest.partition(end)
    today = date.today().isoformat()
    rows = body.strip("\n").split("\n") if body.strip() else []
    for title, url in entries:
        # No TODO here: "none detected" is a fact the script can state, and a
        # placeholder would make an otherwise complete change unmergeable.
        rows.append(
            f"| {title} | {url} | non più pubblicato, rilevato il {today} "
            "| Nessun sostituto rilevato automaticamente. |"
        )
    RETIRED.write_text(
        f"{head}{start}\n" + "\n".join(rows) + f"\n{end}{tail}", encoding="utf-8"
    )


def apply_section(name: str, section: dict, *, dry_run: bool) -> dict:
    """Add rows for newly published material, retire rows that vanished."""
    path = checker.CATALOGS[name]
    fields, rows = read_catalog(path)
    title_column = "Corso" if name == "courses" else "Tutorial"
    by_slug = {checker.slug_of(row["URL"]): row for row in rows}

    added, retired = [], []
    for slug in section["new"]:
        meta = course_metadata(slug) if name == "courses" else tutorial_metadata(slug)
        row = {field: TODO for field in fields}
        row[title_column] = meta["title"]
        row["URL"] = f"{checker.ACADEMY}/{name}/{slug}"
        if name == "courses":
            row["Durata"], row["Lezioni"], row["Quiz"] = (
                meta["duration"], meta["lessons"], meta["quiz"]
            )
        rows.append(row)
        added.append(slug)

    for slug in section["retired"]:
        row = by_slug.get(slug)
        if row is None:
            continue
        rows.remove(row)
        retired.append((row[title_column], row["URL"]))

    if not dry_run and (added or retired):
        write_catalog(path, fields, rows)
        if retired:
            append_retired(retired)
    return {"added": added, "retired": [url for _, url in retired], "rows": len(rows)}


def update_manifest(*, clean: bool, dry_run: bool) -> None:
    """Refresh catalog counts; touch verified_on only on a clean check.

    A `verified_on` that advances on every run is a rubber stamp: the freshness
    guard in validate_pack.py only means something while the date records a
    check that actually came back clean.
    """
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    manifest["claude_courses"] = len(read_catalog(checker.CATALOGS["courses"])[1])
    manifest["claude_tutorials"] = len(read_catalog(checker.CATALOGS["tutorials"])[1])
    if clean:
        manifest["verified_on"] = date.today().isoformat()
    if not dry_run:
        MANIFEST.write_text(
            json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--max-new",
        type=int,
        default=10,
        help="refuse to edit when a single run would add more rows than this",
    )
    parser.add_argument("--skip-link-check", action="store_true")
    args = parser.parse_args()

    report = checker.build_report(
        update_state=False, skip_link_check=args.skip_link_check
    )
    if report["check_failed"]:
        print("refusing to edit: the checker could not read a source", file=sys.stderr)
        checker.print_report(report)
        return 2

    sections = {s["name"]: s for s in report["sections"]}
    total_new = sum(len(s["new"]) for s in sections.values())
    if total_new > args.max_new:
        print(
            f"refusing to edit: {total_new} new items exceeds --max-new {args.max_new}; "
            "a bulk upstream change needs a human",
            file=sys.stderr,
        )
        return 2

    results = {}
    for name, section in sections.items():
        if name in checker.CATALOGS:
            results[name] = apply_section(name, section, dry_run=args.dry_run)

    touched = any(r["added"] or r["retired"] for r in results.values())
    if touched and not args.dry_run:
        import render_catalog
        import sync_pack

        render_catalog.KNOWLEDGE_BASE.write_text(render_catalog.render(), encoding="utf-8")
        update_manifest(clean=False, dry_run=False)
        sync_pack.main()
    elif not touched:
        update_manifest(clean=True, dry_run=args.dry_run)

    print(json.dumps({"changed": touched, "sections": results}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
