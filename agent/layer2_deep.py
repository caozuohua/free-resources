"""Layer 2 — browser-use driven deep free-tier verification (LLM powered).

For each domain that Layer 1 marked UP, we open the site with a real
browser and let an LLM agent decide whether the FREE tier is still real.

Output is constrained to a Pydantic model so the result is machine-usable,
not free-form text. If the LLM endpoint is not configured, we return
UNKNOWN (cheap mode) instead of crashing.
"""
from __future__ import annotations

import asyncio
import os
from typing import Optional

from pydantic import BaseModel, Field

from config import LLMConfig
from schema import FreeTierCheck, FreeTierStatus, ResourceIn


# --- Structured output contract for the LLM agent -------------------------
class FreeTierVerdict(BaseModel):
    free_tier_present: bool = Field(
        description="Is a genuinely free tier (no/optional credit card) still offered?"
    )
    needs_credit_card: bool = Field(
        description="Does accessing the free tier require a credit card upfront?"
    )
    paywall_detected: bool = Field(
        description="Is the free tier now behind a hard paywall / trial-only?"
    )
    confidence: float = Field(ge=0.0, le=1.0)
    notes: str = Field(description="One short sentence of evidence.")


PROMPT_TMPL = """You are verifying whether the FREE tier of a resource still exists.
Resource: {name}
Listed free tier: {free_tier}
URL: {url}

Open the site, look at the pricing / sign-up / free-tier page, and decide:
- Is a genuinely free tier (no or optional credit card) still offered?
- Does the free tier require a credit card upfront?
- Is it now behind a hard paywall or trial-only?

Be strict: if the free offer is gone, mark it stale. Return ONLY the structured verdict.
"""


async def _deep_one(res: ResourceIn, cfg: LLMConfig) -> FreeTierCheck:
    # Imported lazily so cheap-mode (no LLM) never pulls browser-use.
    from browser_use import Agent, Browser, BrowserConfig
    from langchain_openai import ChatOpenAI

    llm = ChatOpenAI(
        model=cfg.model,
        base_url=cfg.base_url,
        api_key=cfg.api_key,
        temperature=0.0,
    )
    browser = Browser(config=BrowserConfig(headless=True))
    try:
        agent = Agent(
            task=PROMPT_TMPL.format(
                name=res.name, free_tier=res.free_tier or "n/a", url=res.url
            ),
            llm=llm,
            browser=browser,
            output_schema=FreeTierVerdict,
        )
        result = await agent.run()
        verdict = result.final_result() if hasattr(result, "final_result") else result
        if isinstance(verdict, FreeTierVerdict):
            status = (
                FreeTierStatus.ACTIVE if verdict.free_tier_present
                else FreeTierStatus.STALE
            )
            return FreeTierCheck(
                status=status, confidence=verdict.confidence,
                free_tier_present=verdict.free_tier_present,
                needs_credit_card=verdict.needs_credit_card,
                paywall_detected=verdict.paywall_detected,
                notes=verdict.notes,
            )
        return FreeTierCheck(status=FreeTierStatus.UNKNOWN,
                             notes=f"no structured result: {str(verdict)[:120]}")
    except Exception as e:
        return FreeTierCheck(status=FreeTierStatus.UNKNOWN,
                             notes=f"layer2 error: {str(e)[:160]}")
    finally:
        try:
            await browser.close()
        except Exception:
            pass


async def deep_verify(
    resources: list[ResourceIn], cfg: LLMConfig, max_runs: int
) -> dict[str, FreeTierCheck]:
    """Run Layer 2 only on up-to-`max_runs` resources. Returns name->check."""
    out: dict[str, FreeTierCheck] = {}
    ran = 0
    for res in resources:
        if ran >= max_runs:
            break
        if cfg.enabled:
            out[res.name] = await _deep_one(res, cfg)
            ran += 1
        else:
            out[res.name] = FreeTierCheck(
                status=FreeTierStatus.UNKNOWN,
                notes="LLM endpoint not configured (cheap mode)",
            )
    return out
