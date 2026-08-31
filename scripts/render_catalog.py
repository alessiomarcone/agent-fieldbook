#!/usr/bin/env python3
"""Render the Claude catalog tables in knowledge-base.md from the canonical CSVs.

The markdown tables between the catalog markers are generated, never edited by
hand: courses.csv and tutorials.csv are the single source of truth.

Usage:
    python3 scripts/render_catalog.py           # rewrite the tables
    python3 scripts/render_catalog.py --check   # fail if the tables are stale
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE_BASE = ROOT / "knowledge" / "claude" / "knowledge-base.md"
COURSES = ROOT / "knowledge" / "claude" / "courses.csv"
TUTORIALS = ROOT / "knowledge" / "claude" / "tutorials.csv"


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def cell(value: str) -> str:
    return value.replace("|", "\\|").strip()


def courses_table() -> str:
    lines = [
        "| Categoria | Corso | Livello | Durata | Lezioni | Utilità |",
        "|---|---|---|---|---|---|",
    ]
    for row in read_rows(COURSES):
        lines.append(
            f"| {cell(row['Categoria'])} "
            f"| [{cell(row['Corso'])}]({cell(row['URL'])}) "
            f"| {cell(row['Livello'])} "
            f"| {cell(row['Durata'])} "
            f"| {cell(row['Lezioni'])} "
            f"| {cell(row['Perché è utile'])} |"
        )
    return "\n".join(lines)


def tutorials_table() -> str:
    lines = [
        "| Categoria | Tutorial | Funzione | Obiettivo |",
        "|---|---|---|---|",
    ]
    for row in read_rows(TUTORIALS):
        lines.append(
            f"| {cell(row['Categoria'])} "
            f"| [{cell(row['Tutorial'])}]({cell(row['URL'])}) "
            f"| {cell(row['Prodotto/Funzione'])} "
            f"| {cell(row['Obiettivo'])} |"
        )
    return "\n".join(lines)


SECTIONS = {"courses": courses_table, "tutorials": tutorials_table}


def replace_section(text: str, name: str, table: str) -> str:
    start = f"<!-- catalog:{name}:start -->"
    end = f"<!-- catalog:{name}:end -->"
    head, _, rest = text.partition(start)
    if not rest:
        raise SystemExit(f"missing marker {start} in {KNOWLEDGE_BASE.name}")
    _, _, tail = rest.partition(end)
    if not tail:
        raise SystemExit(f"missing marker {end} in {KNOWLEDGE_BASE.name}")
    return f"{head}{start}\n{table}\n{end}{tail}"


def render() -> str:
    text = KNOWLEDGE_BASE.read_text(encoding="utf-8")
    for name, build in SECTIONS.items():
        text = replace_section(text, name, build())
    return text


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    rendered = render()
    current = KNOWLEDGE_BASE.read_text(encoding="utf-8")
    if rendered == current:
        print("knowledge-base.md catalog tables are up to date.")
        return 0
    if args.check:
        print(
            "knowledge-base.md catalog tables are stale; "
            "run `python3 scripts/render_catalog.py`.",
            file=sys.stderr,
        )
        return 1
    KNOWLEDGE_BASE.write_text(rendered, encoding="utf-8")
    print(f"Rewrote catalog tables in {KNOWLEDGE_BASE.relative_to(ROOT)}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
