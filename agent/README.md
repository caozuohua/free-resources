# Free-Resources Deep-Verification Agent

Replaces the old `scripts/check_availability.py` (HEAD-only, marked any
live domain `active` even when the free tier was long gone). This harness
does a real three-state check:

| State   | Meaning                                                   |
|---------|-----------------------------------------------------------|
| active  | domain up AND free tier still present (Layer 2)           |
| stale   | domain up but free tier gone / now paywalled (Layer 2)    |
| dead    | domain unreachable / DNS / 5xx (Layer 1)                  |
| unknown | Layer 2 skipped (LLM endpoint not configured = cheap mode)|

## Layers
- **Layer 1 — hybrid domain probe** (`layer1_probe.py`, no LLM, ~ms/call)
  Fast `urllib` GET with desktop UA; 401/403/405 = alive (bot-block);
  DNS/conn/timeout/5xx = down. Catches real 404s the old script missed.
- **Layer 2 — browser-use deep check** (`layer2_deep.py`, LLM powered)
  Opens the site in a real browser and an LLM agent decides whether the
  free tier is still real. Output is constrained to a Pydantic schema
  (`FreeTierVerdict`) so results are machine-usable.

## Setup
```bash
cd free-resources
python3 -m venv .venv && . .venv/bin/activate
pip install browser-use playwright pyyaml pydantic httpx
python -m playwright install chromium
playwright install-deps chromium   # needs apt/root
```

## Run — cheap mode (Layer 1 only, zero LLM cost)
```bash
. .venv/bin/activate
python agent/verify.py --mode all --max-llm-per-batch 0
```

## Run — full LLM mode (needs reachable OpenAI-compatible endpoint)
```bash
export NEW_API_BASE_URL="http://<host>:3000/v1"
export NEW_API_KEY="sk-..."
export NEW_API_MODEL="tencent/hy3:free"
python agent/verify.py --mode all --max-llm-per-batch 8
```
`--mode batch --batch-size N` limits to the first N resources (cost cap).

## Notes / production gaps (not yet closed)
- **LLM endpoint not reachable from this host** — GCP new-api (:3000) and
  Vertex proxy (:18999) were unreachable from az-vps at build time. Run
  Layer 2 from the GCP host (or anywhere the new-api is reachable).
- **Per-run LLM cost** must be bounded: `BATCH_SIZE` + `MAX_LLM_PER_BATCH`
  env vars exist; wire into the GitHub Action with concurrency limits.
- **Regression set** (`promptfoo`) and **tracing** (`cozeloop`) from the
  design are not yet wired — add before declaring production-grade.
- **Anti-bot sites**: Layer 1 uses urllib (not browser) precisely because
  headless chromium times out on Google Colab etc. Keep it that way.
