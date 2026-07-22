#!/usr/bin/env python3
"""
Download official subtitles/auto-captions for videos listed in youtube_videos.csv
and convert VTT files into Markdown transcripts suitable for Claude Projects.

Run update_youtube_catalog.py first.

Requirements:
    python3 -m pip install -U yt-dlp

Examples:
    python3 download_youtube_transcripts.py
    python3 download_youtube_transcripts.py --category "Claude Code"
    python3 download_youtube_transcripts.py --limit 10
"""
from __future__ import annotations

import argparse
import csv
import html
import importlib.util
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

def slugify(value: str, max_len: int = 80) -> str:
    value = value.lower()
    value = re.sub(r"[^\w\s-]", "", value, flags=re.UNICODE)
    value = re.sub(r"[-\s]+", "-", value).strip("-")
    return (value or "video")[:max_len].rstrip("-")

def clean_vtt(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    lines: list[str] = []
    previous = ""
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line == "WEBVTT" or line.startswith(("Kind:", "Language:", "NOTE")):
            continue
        if "-->" in line:
            continue
        if re.fullmatch(r"\d+", line):
            continue
        line = re.sub(r"<\d{2}:\d{2}:\d{2}\.\d{3}>", "", line)
        line = re.sub(r"<[^>]+>", "", line)
        line = html.unescape(line).strip()
        if not line:
            continue

        # YouTube VTT cues often repeat and extend the previous line.
        if line == previous:
            continue
        if previous and line.startswith(previous):
            if lines:
                lines[-1] = line
        elif previous and previous.startswith(line):
            pass
        else:
            lines.append(line)
        previous = line

    # Paragraphs of manageable size for ingestion.
    paragraphs: list[str] = []
    buffer: list[str] = []
    char_count = 0
    for line in lines:
        buffer.append(line)
        char_count += len(line) + 1
        if char_count >= 900:
            paragraphs.append(" ".join(buffer))
            buffer, char_count = [], 0
    if buffer:
        paragraphs.append(" ".join(buffer))
    return "\n\n".join(paragraphs)

def find_best_vtt(raw_dir: Path, video_id: str) -> Path | None:
    files = list(raw_dir.glob(f"{video_id}*.vtt"))
    if not files:
        return None
    def priority(path: Path) -> tuple[int, str]:
        name = path.name.lower()
        if ".en" in name:
            return (0, name)
        if ".it" in name:
            return (1, name)
        return (2, name)
    return sorted(files, key=priority)[0]

def download(ytdlp: list[str], url: str, video_id: str, raw_dir: Path) -> None:
    template = str(raw_dir / f"{video_id}.%(language)s.%(ext)s")
    cmd = [
        *ytdlp,
        "--skip-download",
        "--write-subs",
        "--write-auto-subs",
        "--sub-langs", "en.*,it.*",
        "--sub-format", "vtt",
        "--no-warnings",
        "-o", template,
        url,
    ]
    subprocess.run(cmd, check=False)

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--category", help="Elabora solo la categoria esatta indicata.")
    parser.add_argument("--limit", type=int, help="Numero massimo di video.")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    catalog = root / "knowledge" / "claude" / "youtube_videos.csv"
    if not catalog.exists():
        raise SystemExit(
            "Manca knowledge/claude/youtube_videos.csv. "
            "Esegui prima update_youtube_catalog.py."
        )

    executable = shutil.which("yt-dlp")
    if executable:
        ytdlp = [executable]
    elif importlib.util.find_spec("yt_dlp") is not None:
        ytdlp = [sys.executable, "-m", "yt_dlp"]
    else:
        raise SystemExit("yt-dlp non trovato. Installa con: python3 -m pip install -U yt-dlp")

    raw_dir = root / "transcripts" / "_raw"
    out_dir = root / "transcripts" / "markdown"
    raw_dir.mkdir(parents=True, exist_ok=True)
    out_dir.mkdir(parents=True, exist_ok=True)

    with catalog.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if args.category:
        rows = [r for r in rows if r.get("Categoria") == args.category]
    if args.limit:
        rows = rows[:args.limit]

    manifest_rows: list[dict[str, str]] = []
    for index, row in enumerate(rows, start=1):
        video_id = (row.get("Video ID") or "").strip()
        title = (row.get("Titolo") or "Senza titolo").strip()
        url = (row.get("URL") or "").strip()
        category = (row.get("Categoria") or "Altro").strip()
        if not video_id or not url:
            continue

        output = out_dir / f"{video_id}-{slugify(title)}.md"
        status = "esistente"
        if args.overwrite or not output.exists():
            download(ytdlp, url, video_id, raw_dir)
            vtt = find_best_vtt(raw_dir, video_id)
            if vtt:
                transcript = clean_vtt(vtt)
                fetched = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
                output.write_text(
                    "---\n"
                    f'title: "{title.replace(chr(34), chr(39))}"\n'
                    f'category: "{category.replace(chr(34), chr(39))}"\n'
                    f"video_id: {video_id}\n"
                    f"url: {url}\n"
                    f"transcript_fetched: {fetched}\n"
                    "---\n\n"
                    f"# {title}\n\n"
                    f"Fonte: {url}\n\n"
                    "## Transcript\n\n"
                    f"{transcript}\n",
                    encoding="utf-8",
                )
                status = "scaricato"
            else:
                status = "sottotitoli non disponibili"

        manifest_rows.append({
            "Categoria": category,
            "Titolo": title,
            "URL": url,
            "File": str(output.relative_to(root)) if output.exists() else "",
            "Stato": status,
        })
        print(f"[{index}/{len(rows)}] {status}: {title}")

    manifest = root / "transcripts" / "manifest.csv"
    with manifest.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["Categoria", "Titolo", "URL", "File", "Stato"]
        )
        writer.writeheader()
        writer.writerows(manifest_rows)
    print(f"Manifest: {manifest}")

if __name__ == "__main__":
    main()
