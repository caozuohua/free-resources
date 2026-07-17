"""Load data/resources.yaml into typed ResourceIn objects."""
from __future__ import annotations

import os
from typing import Optional

import yaml

from schema import ResourceIn

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
RESOURCES_YAML = os.path.join(DATA_DIR, "resources.yaml")


def load_resources(path: Optional[str] = None) -> list[ResourceIn]:
    path = path or RESOURCES_YAML
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    out: list[ResourceIn] = []
    for cat in data.get("categories", []):
        cat_id = cat.get("id")
        for r in cat.get("resources", []):
            res = ResourceIn(
                name=r["name"], url=r["url"],
                description=r.get("description"),
                free_tier=r.get("free_tier"),
                limitations=r.get("limitations"),
                rating=r.get("rating"),
                tags=r.get("tags", []),
                category_id=cat_id,
            )
            out.append(res)
    return out
