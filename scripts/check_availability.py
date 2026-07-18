#!/usr/bin/env python3
"""Check resource reachability with GET fallback and failure hysteresis."""

import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

import yaml


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "..", "data")
RESOURCES_FILE = os.path.join(DATA_DIR, "resources.yaml")
OUTPUT_FILE = os.path.join(DATA_DIR, "status.json")
HEADERS = {"User-Agent": "FreeResourcesBot/2.0 (+https://github.com/caozuohua/free-resources)"}
TIMEOUT = 10
MAX_WORKERS = 10


def request_url(url, method):
    start = time.time()
    request = Request(url, headers=HEADERS, method=method)
    with urlopen(request, timeout=TIMEOUT) as response:
        return response.status, (time.time() - start) * 1000


def check_url(url):
    """Return (reachable, response_time_ms, error), retrying HEAD failures with GET."""
    head_error = None
    try:
        code, elapsed = request_url(url, "HEAD")
        return 200 <= code < 400, elapsed, None
    except HTTPError as error:
        if error.code in (401, 403):
            return True, 0, f"HTTP {error.code} (reachable, access restricted)"
        head_error = f"HEAD HTTP {error.code}"
    except (URLError, TimeoutError, OSError) as error:
        head_error = f"HEAD {error}"

    try:
        code, elapsed = request_url(url, "GET")
        return 200 <= code < 400, elapsed, None
    except HTTPError as error:
        if error.code in (401, 403):
            return True, 0, f"HTTP {error.code} (reachable, access restricted)"
        return False, 0, f"{head_error}; GET HTTP {error.code}"
    except (URLError, TimeoutError, OSError) as error:
        return False, 0, f"{head_error}; GET {error}"


def resolve_status(reachable, previous=None):
    """Require two consecutive failed checks before declaring a resource dead."""
    previous = previous or {}
    if reachable:
        return "active", 0
    failures = int(previous.get("failure_count", 0)) + 1
    return ("dead" if failures >= 2 else "unknown"), failures


def load_previous_results():
    if not os.path.exists(OUTPUT_FILE):
        return {}
    try:
        with open(OUTPUT_FILE, encoding="utf-8") as source:
            return json.load(source).get("results", {})
    except (OSError, ValueError):
        return {}


def main():
    if not os.path.exists(RESOURCES_FILE):
        print(f"ERROR: {RESOURCES_FILE} not found")
        return 1

    with open(RESOURCES_FILE, encoding="utf-8") as source:
        data = yaml.safe_load(source)
    resources = [resource for category in data.get("categories", []) for resource in category.get("resources", [])]
    previous = load_previous_results()
    checked_at = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    results = {}

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(check_url, resource["url"]): resource for resource in resources if resource.get("url")}
        for index, future in enumerate(as_completed(futures), start=1):
            resource = futures[future]
            name = resource["name"]
            try:
                reachable, response_time, error = future.result()
            except Exception as exception:  # Keep one bad check from cancelling the batch.
                reachable, response_time, error = False, 0, str(exception)
            status, failure_count = resolve_status(reachable, previous.get(name))
            results[name] = {
                "status": status,
                "response_time_ms": round(response_time),
                "failure_count": failure_count,
                "error": error,
                "checked_at": checked_at,
            }
            if index % 10 == 0:
                print(f"Checked {index}/{len(resources)} resources")

    counts = {status: sum(item["status"] == status for item in results.values()) for status in ("active", "unknown", "dead")}
    output = {
        "generated_at": checked_at,
        "total": len(resources),
        "alive": counts["active"],
        "dead": counts["dead"],
        "unknown": counts["unknown"],
        "results": results,
    }
    with open(OUTPUT_FILE, "w", encoding="utf-8") as target:
        json.dump(output, target, ensure_ascii=False, indent=2)
        target.write("\n")
    print(f"Done: {counts['active']} active, {counts['unknown']} unknown, {counts['dead']} dead")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
