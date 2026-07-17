#!/usr/bin/env python3
"""Deep-verification harness for free-resources.

Pipeline:
  Layer 1 (always, cheap) : Playwright domain probe  -> up / down
  Layer 2 (optional, LLM) : browser-use deep free-tier check -> active / stale / unknown
  Merge                    : domain DOWN forces status=dead
  Write-back               : data/status.json (new 3-state schema)

Usage (cheap mode, no LLM):
  . .venv/bin/activate
  python agent/verify.py --mode batch --batch-size 5

Full LLM mode (needs env: NEW_API_BASE_URL, NEW_API_KEY, NEW_API_MODEL):
  NEW_API_BASE_URL=http://GCP:3000/v1 NEW_API_KEY=sk-... NEW_API_MODEL=tencent/hy3:free \
    python agent/verify.py --mode all --max-llm-per-batch 8
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(__file__))

from config import load_llm_config, load_batch_config  # noqa: E402
from loader import load_resources  # noqa: E402
from schema import VerificationResult  # noqa: E402
from layer1_probe import probe_batch  # noqa: E402
from layer2_deep import deep_verify  # noqa: E402

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
STATUS_OUT = os.path.join(DATA_DIR, "status.json")


def write_status(results: list[VerificationResult], mode: str) -> None:
    payload = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "mode": mode,
        "total": len(results),
        "counts": _count(results),
        "results": {r.name: r.model_dump(mode="json") for r in results},
    }
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(STATUS_OUT, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)


def _count(results: list[VerificationResult]) -> dict:
    c = {"active": 0, "stale": 0, "dead": 0, "unknown": 0}
    for r in results:
        c[r.status.value] = c.get(r.status.value, 0) + 1
    return c


async def run(mode: str, batch_size: int, max_llm: int, bcfg) -> list[VerificationResult]:
    resources = load_resources()
    if mode == "batch":
        resources = resources[:batch_size]
    print(f"[verify] {len(resources)} resources | mode={mode} | llm_enabled={cfg.enabled}")

    # Layer 1 — deterministic, always runs.
    dom = await probe_batch(resources, concurrency=bcfg.layer1_concurrency)
    domain_map = {r.name: d for r, d in zip(resources, dom)}
    up = [r for r, d in zip(resources, dom) if d.status.value == "up"]
    print(f"[verify] Layer1: {len(up)} up / {len(resources)-len(up)} down")

    # Layer 2 — LLM deep check on up domains.
    if cfg.enabled and up:
        ft = await deep_verify(up, cfg, max_llm)
    else:
        ft = {r.name: __import__("layer2_deep").FreeTierCheck(
            status=__import__("schema").FreeTierStatus.UNKNOWN,
            notes="LLM disabled (cheap mode)" if not cfg.enabled
            else "skipped (no up domains)") for r in up}

    results = []
    for r, d in zip(resources, dom):
        ftc = ft.get(r.name) or __import__("schema").FreeTierCheck(
            status=__import__("schema").FreeTierStatus.UNKNOWN)
        results.append(VerificationResult.merge(r, d, ftc))
    return results


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["all", "batch"], default="batch")
    ap.add_argument("--batch-size", type=int, default=5)
    ap.add_argument("--max-llm-per-batch", type=int, default=5)
    args = ap.parse_args()

    global cfg
    cfg = load_llm_config()
    bcfg = load_batch_config()
    if args.mode == "all":
        args.batch_size = 10**9

    t0 = time.time()
    results = asyncio.run(run(args.mode, args.batch_size, args.max_llm_per_batch, bcfg))
    write_status(results, args.mode)
    elapsed = time.time() - t0

    print(f"\n[verify] done in {elapsed:.1f}s")
    print(f"[verify] {json.dumps(_count(results), ensure_ascii=False)}")
    print(f"[verify] wrote {STATUS_OUT}")


if __name__ == "__main__":
    main()
