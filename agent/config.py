"""Runtime configuration for the deep-verification agent.

LLM endpoint is configurable via env. Default points at the GCP new-api
(per deployment notes). Falls back to Nous if NEW_API_BASE_URL is unset,
but the harness NEVER hard-codes a secret — the key comes from env.
"""
from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass
class LLMConfig:
    base_url: str
    api_key: str
    model: str
    # If False, Layer 2 is skipped (dom.reasoning only) -> cheap mode.
    enabled: bool


def load_llm_config() -> LLMConfig:
    base = os.environ.get("NEW_API_BASE_URL", "").strip()
    key = os.environ.get("NEW_API_KEY", "").strip()
    model = os.environ.get("NEW_API_MODEL", "tencent/hy3:free").strip()
    enabled = bool(base and key)
    return LLMConfig(base_url=base, api_key=key, model=model, enabled=enabled)


@dataclass
class BatchConfig:
    # Total resources in the repo is ~97. We verify in batches to bound
    # LLM cost + Playwright runtime on CI.
    batch_size: int = int(os.environ.get("BATCH_SIZE", "10"))
    # concurrency for Layer 1 (cheap); Layer 2 is serial-ish per browser.
    layer1_concurrency: int = int(os.environ.get("L1_CONCURRENCY", "8"))
    # "all" -> every resource; "batch" -> only first BATCH_SIZE.
    mode: str = os.environ.get("VERIFY_MODE", "batch")
    # Limit Layer-2 (LLM) runs per batch to control spend.
    max_llm_per_batch: int = int(os.environ.get("MAX_LLM_PER_BATCH", "5"))


def load_batch_config() -> BatchConfig:
    return BatchConfig()
