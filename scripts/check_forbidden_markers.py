#!/usr/bin/env python3
"""Scan a portable vault package for markers that should not be exported."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


FORBIDDEN_PATTERNS = [
    r"/Users/a11",
    r"GDrive",
    r"obd_pers",
    r"johov",
    r"Zhokhov",
    r"Dmitr",
    r"click\.ru",
    r"Promopult",
    r"promopult",
    r"trustRDP",
    r"trustrdp",
    r"Renovizija",
    r"Novi",
    r"novi",
    r"japan",
    r"Japan",
    r"minyadi",
    r"motcheck",
    r"Telegram",
    r"salary",
    r"payroll",
    r"wage",
    r"api[_-]?key",
    r"Keychain",
    r"01_now/(ops|projects)/2026-",
    r"90_archive/2026-",
    r"employee-directory",
    r"Super CEO",
    r"amoCRM",
    r"Kommo",
    r"YouTrack",
]

SKIP_PARTS = {".git", "__pycache__"}
SKIP_SUFFIXES = {".pyc"}
ALLOWED_PUBLIC_REPO_MARKERS = {
    "dzhokhov/markdown-agent-vault",
    "github.com/dzhokhov/markdown-agent-vault",
}


def iter_text_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.name == "check_forbidden_markers.py":
            continue
        if any(part in SKIP_PARTS for part in path.parts):
            continue
        if path.suffix in SKIP_SUFFIXES:
            continue
        if path.name == ".DS_Store":
            continue
        yield path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".", help="Vault root, default: current directory")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    patterns = [re.compile(pattern, re.IGNORECASE) for pattern in FORBIDDEN_PATTERNS]
    hits: list[tuple[Path, int, str]] = []

    for path in iter_text_files(root):
        text = path.read_text(encoding="utf-8", errors="ignore")
        for lineno, line in enumerate(text.splitlines(), 1):
            if any(marker in line for marker in ALLOWED_PUBLIC_REPO_MARKERS):
                continue
            if any(pattern.search(line) for pattern in patterns):
                hits.append((path.relative_to(root), lineno, line.strip()))

    if hits:
        print(f"FORBIDDEN_MARKERS {len(hits)}")
        for path, lineno, line in hits[:200]:
            print(f"{path}:{lineno}: {line}")
        return 1

    print("OK forbidden markers")
    return 0


if __name__ == "__main__":
    sys.exit(main())
