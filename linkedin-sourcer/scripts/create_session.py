#!/usr/bin/env python3
"""
Create and save a LinkedIn authenticated session for reuse.

Usage:
    python3 scripts/create_session.py [--session-path SESSION_PATH] [--timeout SECONDS]

Options:
    --session-path  Path to save session file (default: session.json in cwd)
    --timeout       Seconds to wait for manual login (default: 300)

This opens a browser window for manual LinkedIn login, then saves
the session for reuse by other scraping scripts.
"""

import argparse
import asyncio
import sys
from pathlib import Path

try:
    from linkedin_scraper import BrowserManager, wait_for_manual_login
except ImportError:
    print("Error: linkedin_scraper not installed. Run: pip install linkedin-scraper && playwright install chromium")
    sys.exit(1)


async def create_session(session_path: str, timeout: int) -> None:
    async with BrowserManager(headless=False) as browser:
        await browser.page.goto("https://www.linkedin.com/login")
        print(f"Please log in to LinkedIn in the browser window. You have {timeout} seconds.")
        await wait_for_manual_login(browser.page, timeout=timeout)
        await browser.save_session(session_path)
        print(f"Session saved to {session_path}")


def main():
    parser = argparse.ArgumentParser(description="Create a LinkedIn session")
    parser.add_argument("--session-path", default="session.json", help="Path to save session file")
    parser.add_argument("--timeout", type=int, default=300, help="Seconds to wait for login")
    args = parser.parse_args()

    asyncio.run(create_session(args.session_path, args.timeout))


if __name__ == "__main__":
    main()
