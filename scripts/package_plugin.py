#!/usr/bin/env python3
"""Build a deterministic ZIP of the self-contained knowledge-pack plugin."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "knowledge-pack"
MANIFEST = PLUGIN / ".claude-plugin" / "plugin.json"
FIXED_TIMESTAMP = (2020, 1, 1, 0, 0, 0)
ALLOWED_ROOT_FILES = {
    Path(".claude-plugin/plugin.json"),
    Path(".codex-plugin/plugin.json"),
    Path("LICENSE"),
    Path("PRIVACY.md"),
    Path("README.md"),
    Path("SECURITY.md"),
    Path("SUPPORT.md"),
    Path("TERMS.md"),
}
ALLOWED_ROOT_DIRS = {".claude-plugin", ".codex-plugin", "assets", "skills"}
FORBIDDEN_NAMES = {
    ".DS_Store",
    ".env",
    "__pycache__",
    "credentials.json",
    "secrets.json",
}
FORBIDDEN_SUFFIXES = {".key", ".p12", ".pem", ".pfx", ".pyc"}


def version() -> str:
    payload = json.loads(MANIFEST.read_text(encoding="utf-8"))
    return str(payload["version"])


def collect_files() -> list[Path]:
    """Return the release allowlist, rejecting scratch or sensitive files."""
    missing = sorted(
        path.as_posix()
        for path in ALLOWED_ROOT_FILES
        if not (PLUGIN / path).is_file()
    )
    if missing:
        raise ValueError(f"missing required release file(s): {', '.join(missing)}")

    files: list[Path] = []
    for path in sorted(PLUGIN.rglob("*")):
        relative = path.relative_to(PLUGIN)
        if path.is_symlink():
            raise ValueError(f"symlinks are not allowed: {relative.as_posix()}")
        if relative in ALLOWED_ROOT_FILES:
            files.append(path)
            continue
        if relative.parts[0] not in ALLOWED_ROOT_DIRS:
            raise ValueError(f"unexpected plugin entry: {relative.as_posix()}")
        if any(
            part in FORBIDDEN_NAMES or part.startswith(".env.")
            for part in relative.parts
        ):
            raise ValueError(f"unsafe plugin entry: {relative.as_posix()}")
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            raise ValueError(f"unsafe plugin entry: {relative.as_posix()}")
        if not path.is_file():
            continue
        if relative.parts[0] in {"assets", "skills"}:
            files.append(path)
        else:
            raise ValueError(f"unexpected plugin file: {relative.as_posix()}")
    return files


def build(output_dir: Path) -> tuple[Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    archive = output_dir / f"knowledge-pack-{version()}.zip"
    files = collect_files()

    with zipfile.ZipFile(
        archive,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as bundle:
        for path in files:
            relative = path.relative_to(PLUGIN).as_posix()
            info = zipfile.ZipInfo(relative, date_time=FIXED_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            bundle.writestr(info, path.read_bytes())

    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    checksum = archive.with_suffix(".zip.sha256")
    checksum.write_text(f"{digest}  {archive.name}\n", encoding="utf-8")
    return archive, checksum


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "dist",
        help="Destination directory (default: dist).",
    )
    args = parser.parse_args()
    try:
        archive, checksum = build(args.output_dir.resolve())
    except ValueError as exc:
        print(f"Packaging refused: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
    print(f"Created {archive}")
    print(f"Created {checksum}")


if __name__ == "__main__":
    main()
