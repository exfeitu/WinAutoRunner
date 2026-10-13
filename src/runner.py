"""Local demonstration of resilient, scheduled Chrome automation.

No real user sites, accounts, or credentials. Python 3.10+; test on 3.12 before production.
"""
import argparse
import json
import logging
import os
from pathlib import Path
import signal
import sys
import time
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
STOP = False

def handle_stop(_signum, _frame):
    global STOP
    STOP = True

def load_config(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data.get("url"), str) or not data["url"].startswith(("https://", "http://")):
        raise ValueError("url must begin with http:// or https://")
    for key in ("interval_seconds", "timeout_ms"):
        if not isinstance(data.get(key), int) or data[key] < 1:
            raise ValueError(key + " must be a positive integer")
    return data

def setup_logging():
    logdir = ROOT / "logs"
    logdir.mkdir(exist_ok=True)
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s",
       handlers=[logging.StreamHandler(sys.stdout), logging.FileHandler(logdir / "runner.log", encoding="utf-8")])

def run_once(config):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = None
        # Default launches a dedicated Chrome with a new context (no personal profile).
        # CDP mode is optional and attaches only to an explicitly configured local endpoint.
        try:
            if config.get("cdp_url"):
                browser = p.chromium.connect_over_cdp(config["cdp_url"])
                page = browser.contexts[0].new_page()
                context = None
            else:
                browser = p.chromium.launch(channel="chrome", headless=bool(config.get("headless", False)))
                context = browser.new_context()
                page = context.new_page()
            page.goto(config["url"], wait_until="domcontentloaded", timeout=config["timeout_ms"])
            result = {"timestamp": datetime.now(timezone.utc).isoformat(), "title": page.title(), "url": page.url, "ok": True}
            if context:
                context.close()
            else:
                page.close()
            return result
        finally:
            if browser:
                # Do not close a customer's externally managed CDP browser.
                if not config.get("cdp_url"):
                    browser.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default=str(ROOT / "config" / "config.example.json"))
    parser.add_argument("--once", action="store_true")
    args = parser.parse_args()
    setup_logging()
    config = load_config(args.config)
    signal.signal(signal.SIGINT, handle_stop)
    if hasattr(signal, "SIGTERM"):
        signal.signal(signal.SIGTERM, handle_stop)
    while not STOP:
        try:
            result = run_once(config)
            logging.info("Result: %s", json.dumps(result, ensure_ascii=False))
            (ROOT / "logs" / "status.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
        except Exception:
            logging.exception("Automation cycle failed")
            (ROOT / "logs" / "status.json").write_text(json.dumps({"ok": False, "timestamp": datetime.now(timezone.utc).isoformat()}, indent=2), encoding="utf-8")
            if args.once:
                return 1
        if args.once:
            return 0
        end = time.monotonic() + config["interval_seconds"]
        while time.monotonic() < end and not STOP:
            time.sleep(min(0.5, end - time.monotonic()))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
