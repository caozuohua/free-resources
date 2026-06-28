#!/usr/bin/env python3
"""
Convert resources.yaml to resources.json for frontend consumption.
Run this after editing the YAML.
"""

import yaml
import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "..", "data")
YAML_FILE = os.path.join(DATA_DIR, "resources.yaml")
JSON_FILE = os.path.join(DATA_DIR, "resources.json")


def main():
    if not os.path.exists(YAML_FILE):
        print(f"ERROR: {YAML_FILE} not found. Run from scripts/ directory.")
        sys.exit(1)

    with open(YAML_FILE, "r") as f:
        data = yaml.safe_load(f)

    # Add computed fields
    for cat in data.get("categories", []):
        for r in cat.get("resources", []):
            r.setdefault("status", "unknown")
            r.setdefault("tags", [])
            r.setdefault("rating", 0)

    with open(JSON_FILE, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    total = sum(len(cat.get("resources", [])) for cat in data.get("categories", []))
    print(f"Converted {total} resources from YAML -> JSON")
    print(f"Output: {JSON_FILE}")


if __name__ == "__main__":
    main()
