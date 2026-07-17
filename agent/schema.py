"""Pydantic schemas for the Free-Resources deep-verification agent.

Three real states (fixes the old check_availability.py bug where any
domain that returned 200/403 was marked `active` even when the free
tier was long gone):

  active : domain up AND free tier still present
  stale  : domain up but free tier gone / now paywalled
  dead   : domain unreachable / DNS/HTTP dead
"""
from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class DomainStatus(str, Enum):
    UP = "up"
    DOWN = "down"


class FreeTierStatus(str, Enum):
    ACTIVE = "active"
    STALE = "stale"
    DEAD = "dead"
    UNKNOWN = "unknown"   # layer-2 skipped / failed


class ResourceIn(BaseModel):
    """One resource as it appears in data/resources.yaml."""
    name: str
    url: str
    description: Optional[str] = None
    free_tier: Optional[str] = None
    limitations: Optional[str] = None
    rating: Optional[int] = None
    tags: list[str] = Field(default_factory=list)
    category_id: Optional[str] = None   # filled by loader


class DomainCheck(BaseModel):
    """Layer 1 — deterministic Playwright probe (no LLM)."""
    status: DomainStatus
    http_code: Optional[int] = None
    final_url: Optional[str] = None
    response_time_ms: Optional[float] = None
    error: Optional[str] = None
    evidence: str = ""   # short deterministic signal (title / banner text hit)


class FreeTierCheck(BaseModel):
    """Layer 2 — LLM-driven browser-use deep verification."""
    status: FreeTierStatus
    confidence: float = Field(ge=0.0, le=1.0, default=0.0)
    free_tier_present: Optional[bool] = None
    needs_credit_card: Optional[bool] = None
    paywall_detected: Optional[bool] = None
    notes: str = ""
    screenshot_path: Optional[str] = None


class VerificationResult(BaseModel):
    """Merged output written back to data/status.json."""
    name: str
    url: str
    category_id: Optional[str] = None
    domain: DomainCheck
    free_tier: FreeTierCheck
    # merged top-level status used by the docs site
    status: FreeTierStatus
    checked_at: str = Field(
        default_factory=lambda: datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    )

    @classmethod
    def merge(cls, res: "ResourceIn", dom: DomainCheck,
              ft: FreeTierCheck) -> "VerificationResult":
        # If domain is down, free tier is dead regardless of layer-2.
        if dom.status == DomainStatus.DOWN:
            status = FreeTierStatus.DEAD
            ft = ft.model_copy(update={"status": FreeTierStatus.DEAD})
        else:
            status = ft.status
        return cls(
            name=res.name, url=res.url, category_id=res.category_id,
            domain=dom, free_tier=ft, status=status,
        )
