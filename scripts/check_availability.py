#!/usr/bin/env python3
"""
Resource Availability Checker
Pings each resource URL and checks if it's still alive.
Outputs a status JSON file for the GitHub Pages site.
"""

import yaml
import json
import time
import sys
import os
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from concurrent.futures import ThreadPoolExecutor, as_completed

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "..", "data")
RESOURCES_FILE = os.path.join(DATA_DIR, "resources.yaml")
OUTPUT_FILE = os.path.join(DATA_DIR, "status.json")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; FreeResourcesBot/1.0; +https://github.com/caozuohua/free-resources)"
}

# Timeout per request (seconds)
TIMEOUT = 10
# Max concurrent workers
MAX_WORKERS = 10


def check_url(url):
    """Check if a URL is reachable. Returns (status, response_time_ms, error)."""
    try:
        req = Request(url, headers=HEADERS, method="HEAD")
        start = time.time()
        resp = urlopen(req, timeout=TIMEOUT)
        elapsed = (time.time() - start) * 1000
        return "active", elapsed, None
    except HTTPError as e:
        # 403/405 is often "HEAD not allowed" — site is alive
        if e.code in (403, 405, 401):
            return "active", 0, None
        return "dead", 0, f"HTTP {e.code}"
    except URLError as e:
        return "dead", 0, str(e.reason)
    except Exception as e:
        return "dead", 0, str(e)


def main():
    if not os.path.exists(RESOURCES_FILE):
        print(f"ERROR: {RESOURCES_FILE} not found")
        sys.exit(1)

    with open(RESOURCES_FILE, "r") as f:
        data = yaml.safe_load(f)

    resources = []
    for cat in data.get("categories", []):
        for r in cat.get("resources", []):
            resources.append(r)

    print(f"Checking {len(resources)} resources...")
    results = {}
    checked = 0
    alive = 0

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_map = {}
        for r in resources:
            url = r.get("url", "")
            if url:
                future = executor.submit(check_url, url)
                future_map[future] = r["name"]

        for future in as_completed(future_map):
            name = future_map[future]
            try:
                status, resp_time, error = future.result()
            except Exception as e:
                status, resp_time, error = "dead", 0, str(e)

            results[name] = {
                "status": status,
                "response_time_ms": round(resp_time, 0),
                "error": error,
                "checked_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            }
            checked += 1
            if status == "active":
                alive += 1
            if checked % 10 == 0:
                print(f"  Progress: {checked}/{len(resources)} checked, {alive} alive")

    output = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "total": len(resources),
        "alive": alive,
        "dead": len(resources) - alive,
        "results": results
    }

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\nDone! {alive}/{len(resources)} resources are alive.")
    print(f"Status written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
