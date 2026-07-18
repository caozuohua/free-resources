#!/usr/bin/env python3
"""Copy canonical generated data into the GitHub Pages docs directory."""

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAIRS = [
    (ROOT / "data" / "resources.json", ROOT / "docs" / "resources.json"),
    (ROOT / "data" / "status.json", ROOT / "docs" / "status.json"),
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    stale = []
    for source, target in PAIRS:
        if not target.exists() or source.read_bytes() != target.read_bytes():
            stale.append(target.relative_to(ROOT))
            if not args.check:
                shutil.copyfile(source, target)
    if args.check and stale:
        raise SystemExit(f"Stale Pages data: {', '.join(map(str, stale))}")
    print("Pages data is synchronized.")


if __name__ == "__main__":
    main()
