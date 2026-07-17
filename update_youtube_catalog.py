#!/usr/bin/env python3
"""
Generate a categorized, current catalog of every video exposed by the official
Anthropic YouTube channel.

Requirements:
    python -m pip install -U yt-dlp

Usage:
    python update_youtube_catalog.py
    python update_youtube_catalog.py --archive
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

CHANNEL_URL = "https://www.youtube.com/@anthropic-ai/videos"

CATEGORY_RULES: list[tuple[str, list[str]]] = [
    ("Claude Code", [
        r"\bclaude code\b", r"\bcode with claude\b", r"\bcoding\b",
        r"\bgithub\b", r"\bterminal\b", r"\bdeveloper workflow\b",
    ]),
    ("Skills / Subagents / MCP / Agents", [
        r"\bskill(s)?\b", r"\bsub-?agent(s)?\b", r"\bmcp\b",
        r"\bmodel context protocol\b", r"\bagent(ic|s)?\b",
        r"\bplugin(s)?\b", r"\bconnector(s)?\b", r"\bcowork\b",
    ]),
    ("API / Developer Platform", [
        r"\bapi\b", r"\bdeveloper platform\b", r"\btool use\b",
        r"\bfunction calling\b", r"\bbedrock\b", r"\bvertex\b",
        r"\bprompt caching\b", r"\bbatch\b", r"\bconsole\b",
    ]),
    ("Claude.ai / Productivity / Artifacts", [
        r"\bclaude\.ai\b", r"\bartifact(s)?\b", r"\bproject(s)?\b",
        r"\bexcel\b", r"\bchrome\b", r"\bdesktop\b",
        r"\bproductivity\b", r"\bdesign\b", r"\bpresentation(s)?\b",
    ]),
    ("AI Fluency / Prompting", [
        r"\bprompt(ing|s)?\b", r"\bai fluency\b", r"\b4d\b",
        r"\beffective.*claude\b", r"\bgetting started\b",
        r"\bhow to use claude\b", r"\bcapabilit(y|ies)\b",
    ]),
    ("Research / Safety", [
        r"\bsafety\b", r"\balignment\b", r"\bresearch\b",
        r"\binterpretability\b", r"\bconstitutional ai\b",
        r"\bresponsible\b", r"\bevaluation(s)?\b", r"\bsecurity\b",
    ]),
    ("Events / Interviews / Customer stories", [
        r"\binterview\b", r"\bkeynote\b", r"\bevent\b", r"\bsummit\b",
        r"\bcustomer\b", r"\bstory\b", r"\bfireside\b", r"\bpanel\b",
        r"\bconversation\b", r"\bcase study\b",
    ]),
]

def require_ytdlp() -> str:
    executable = shutil.which("yt-dlp")
    if executable:
        return executable
    raise SystemExit(
        "yt-dlp non trovato.\n"
        "Installa con: python -m pip install -U yt-dlp"
    )

def fetch_catalog(ytdlp: str) -> dict[str, Any]:
    cmd = [
        ytdlp,
        "--flat-playlist",
        "--dump-single-json",
        "--no-warnings",
        CHANNEL_URL,
    ]
    try:
        proc = subprocess.run(
            cmd, capture_output=True, text=True, check=True, encoding="utf-8"
        )
    except subprocess.CalledProcessError as exc:
        message = exc.stderr.strip() or exc.stdout.strip()
        raise SystemExit(f"Errore durante il recupero del canale:\n{message}") from exc
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        raise SystemExit("La risposta di yt-dlp non è JSON valido.") from exc

def categorize(title: str) -> str:
    normalized = title.lower()
    for category, patterns in CATEGORY_RULES:
        if any(re.search(pattern, normalized, flags=re.I) for pattern in patterns):
            return category
    return "Altro"

def normalize_entry(entry: dict[str, Any]) -> dict[str, str]:
    video_id = str(entry.get("id") or "").strip()
    title = str(entry.get("title") or "Senza titolo").strip()
    direct_url = (
        entry.get("webpage_url")
        or entry.get("url")
        or (f"https://www.youtube.com/watch?v={video_id}" if video_id else "")
    )
    if video_id and not str(direct_url).startswith("http"):
        direct_url = f"https://www.youtube.com/watch?v={video_id}"

    duration = entry.get("duration")
    if isinstance(duration, (int, float)):
        mins, secs = divmod(int(duration), 60)
        duration_display = f"{mins}:{secs:02d}"
    else:
        duration_display = ""

    upload_date = str(entry.get("upload_date") or "")
    if len(upload_date) == 8 and upload_date.isdigit():
        upload_date = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:]}"

    return {
        "Categoria": categorize(title),
        "Titolo": title,
        "URL": str(direct_url),
        "Video ID": video_id,
        "Durata": duration_display,
        "Data pubblicazione": upload_date,
    }

def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    fields = ["Categoria", "Titolo", "URL", "Video ID", "Durata", "Data pubblicazione"]
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

def write_markdown(path: Path, rows: list[dict[str, str]], checked_at: str) -> None:
    counts = Counter(row["Categoria"] for row in rows)
    lines = [
        "# Catalogo YouTube Anthropic",
        "",
        f"**Aggiornato:** {checked_at}",
        f"**Video catalogati:** {len(rows)}",
        f"**Canale:** {CHANNEL_URL}",
        "",
        "## Riepilogo",
        "",
    ]
    for category, count in sorted(counts.items()):
        lines.append(f"- **{category}:** {count}")
    lines.extend(["", "## Video", ""])

    order = [name for name, _ in CATEGORY_RULES] + ["Altro"]
    for category in order:
        category_rows = [row for row in rows if row["Categoria"] == category]
        if not category_rows:
            continue
        lines.extend([f"### {category}", ""])
        for row in category_rows:
            meta = " · ".join(x for x in [row["Data pubblicazione"], row["Durata"]] if x)
            suffix = f" — {meta}" if meta else ""
            lines.append(f"- [{row['Titolo']}]({row['URL']}){suffix}")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--archive",
        action="store_true",
        help="Conserva anche copie datate dei file generati.",
    )
    args = parser.parse_args()

    ytdlp = require_ytdlp()
    payload = fetch_catalog(ytdlp)
    raw_entries = payload.get("entries") or []
    rows = [normalize_entry(entry) for entry in raw_entries if isinstance(entry, dict)]
    rows = [row for row in rows if row["URL"]]
    if not rows:
        raise SystemExit("Nessun video trovato nel feed del canale.")

    # Remove duplicates while preserving channel order.
    seen: set[str] = set()
    deduped: list[dict[str, str]] = []
    for row in rows:
        key = row["Video ID"] or row["URL"]
        if key in seen:
            continue
        seen.add(key)
        deduped.append(row)

    checked_at = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    out_dir = Path(__file__).resolve().parent
    csv_path = out_dir / "youtube_videos.csv"
    md_path = out_dir / "youtube_videos.md"
    write_csv(csv_path, deduped)
    write_markdown(md_path, deduped, checked_at)

    if args.archive:
        stamp = datetime.now().strftime("%Y-%m-%d")
        archive_dir = out_dir / "archive" / stamp
        archive_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(csv_path, archive_dir / csv_path.name)
        shutil.copy2(md_path, archive_dir / md_path.name)

    print(f"Creati {csv_path.name} e {md_path.name}: {len(deduped)} video.")

if __name__ == "__main__":
    main()
