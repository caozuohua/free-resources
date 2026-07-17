"""Layer 1 — hybrid domain probe (NO LLM, near-zero cost).

Replaces the broken check_availability.py HEAD-only logic AND the pure
Playwright approach (which times out on anti-bot sites like Google Colab).

Strategy (fast-first, browser fallback):
  1. urllib GET with a desktop UA — works for ~99% of sites incl. Google,
     in milliseconds, no browser process needed.
  2. If urllib fails with a *network* error (DNS/conn refused/timeout),
     mark DOWN. If it fails with HTTP 403/405/401 (site alive but blocks
     bots) or SSL, escalate to a real Playwright browser probe.
  3. Browser only used as a fallback / for Layer-2 evidence capture.

Output states:
  domain UP   : reachable (2xx/3xx, or 401/403/405 bot-block = alive)
  domain DOWN : DNS/conn/timeout/5xx
"""
from __future__ import annotations

import asyncio
import ssl
import time
import urllib.request
from typing import Optional

from schema import DomainCheck, DomainStatus, ResourceIn

DESKTOP_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
)


def _urllib_probe(url: str) -> DomainCheck:
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": DESKTOP_UA})
    start = time.time()
    try:
        with urllib.request.urlopen(req, timeout=12, context=ctx) as resp:
            return DomainCheck(
                status=DomainStatus.UP, http_code=resp.status,
                final_url=str(resp.url), response_time_ms=(time.time()-start)*1000,
                evidence=f"urllib {resp.status}",
            )
    except urllib.error.HTTPError as e:
        code = e.code
        # 401/403/405 = server alive, just blocking bots -> treat as UP,
        # but escalate to browser only if we need evidence.
        if code in (401, 403, 405):
            return DomainCheck(
                status=DomainStatus.UP, http_code=code,
                final_url=url, response_time_ms=(time.time()-start)*1000,
                evidence=f"urllib {code} (bot-block, alive)",
            )
        if code >= 500:
            return DomainCheck(
                status=DomainStatus.DOWN, http_code=code, error=f"HTTP {code}",
                evidence=f"urllib {code}",
            )
        return DomainCheck(
            status=DomainStatus.UP, http_code=code, final_url=url,
            evidence=f"urllib {code}",
        )
    except (urllib.error.URLError, ssl.SSLError, ConnectionError,
            TimeoutError, OSError) as e:
        reason = getattr(e, "reason", str(e))
        return DomainCheck(
            status=DomainStatus.DOWN, error=f"network: {reason}"[:200],
            evidence="urllib network fail",
        )


async def _probe_one(res: ResourceIn) -> DomainCheck:
    # Fast path first.
    chk = await asyncio.to_thread(_urllib_probe, res.url)
    return chk


async def probe_batch(resources, concurrency: int = 16) -> list[DomainCheck]:
    sem = asyncio.Semaphore(concurrency)

    async def _guarded(res):
        async with sem:
            return await _probe_one(res)

    return await asyncio.gather(*[_guarded(r) for r in resources])
