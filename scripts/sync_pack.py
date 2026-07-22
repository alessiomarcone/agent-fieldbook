#!/usr/bin/env python3
"""Copy canonical knowledge and templates into self-contained skills."""

from __future__ import annotations

import shutil

from validate_pack import MIRRORS, ROOT


def main() -> None:
    copied = 0
    for source, destinations in MIRRORS.items():
        if not source.is_file():
            raise SystemExit(f"Missing canonical file: {source.relative_to(ROOT)}")
        for destination in destinations:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)
            print(f"Synced {source.name} -> {destination.relative_to(ROOT)}")
            copied += 1
    print(f"Synced {copied} mirrored files.")


if __name__ == "__main__":
    main()
