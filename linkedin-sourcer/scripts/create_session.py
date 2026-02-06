#!/usr/bin/env python3
"""
Create and save a LinkedIn authenticated session for reuse.

Usage:
    Manual login (opens browser window):
        python3 scripts/create_session.py

    Programmatic login (uses credentials):
        python3 scripts/create_session.py --email USER@EXAMPLE.COM --password PASS

    Using environment variables:
        export LINKEDIN_EMAIL=user@example.com
        export LINKEDIN_PASSWORD=mypassword
        python3 scripts/create_session.py

Options:
    --email         LinkedIn email (or set LINKEDIN_EMAIL env var)
    --password      LinkedIn password (or set LINKEDIN_PASSWORD env var)
    --session-path  Path to save session file (default: session.json)
    --timeout       Seconds to wait for manual login (default: 300)

If --email and --password are provided (or env vars are set), programmatic
login is used. Otherwise, a browser window opens for manual login.
"""

import argparse
import asyncio
import os
import sys

try:
    from linkedin_scraper import BrowserManager, wait_for_manual_login, login_with_credentials
except ImportError:
    print("Error: linkedin_scraper not installed. Run: pip install linkedin-scraper && playwright install chromium")
    sys.exit(1)


async def manual_login(session_path: str, timeout: int) -> None:
    async with BrowserManager(headless=False) as browser:
        await browser.page.goto("https://www.linkedin.com/login")
        print(f"Please log in to LinkedIn in the browser window. You have {timeout} seconds.")
        await wait_for_manual_login(browser.page, timeout=timeout)
        await browser.save_session(session_path)
        print(f"Session saved to {session_path}")


async def programmatic_login(email: str, password: str, session_path: str) -> None:
    async with BrowserManager(headless=False) as browser:
        print("Logging in to LinkedIn...")
        await login_with_credentials(browser.page, username=email, password=password)
        await browser.save_session(session_path)
        print(f"Session saved to {session_path}")


def main():
    parser = argparse.ArgumentParser(description="Create a LinkedIn session")
    parser.add_argument("--email", default=None, help="LinkedIn email (or set LINKEDIN_EMAIL env var)")
    parser.add_argument("--password", default=None, help="LinkedIn password (or set LINKEDIN_PASSWORD env var)")
    parser.add_argument("--session-path", default="session.json", help="Path to save session file")
    parser.add_argument("--timeout", type=int, default=300, help="Seconds to wait for manual login")
    args = parser.parse_args()

    email = args.email or os.getenv("LINKEDIN_EMAIL")
    password = args.password or os.getenv("LINKEDIN_PASSWORD")

    if email and password:
        asyncio.run(programmatic_login(email, password, args.session_path))
    else:
        asyncio.run(manual_login(args.session_path, args.timeout))


if __name__ == "__main__":
    main()
