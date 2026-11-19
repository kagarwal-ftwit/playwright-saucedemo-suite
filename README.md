# Playwright SauceDemo Test Suite

Automated UI tests for SauceDemo (https://www.saucedemo.com), built with
Playwright (Python) and pytest. A learn-as-you-build QA portfolio project.

## Stack

- Python 3.12
- Playwright (Python), pinned to 1.61.0 — the last version whose Chromium
  still supports macOS 12 (Monterey); newer versions require macOS 13+
- pytest + pytest-playwright

## How to run

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    playwright install chromium
    pytest -v

## What it covers (so far)

- [x] Login with a valid user lands on the Products page
