#!/usr/bin/env python3
"""
Scrape one or more LinkedIn company pages and output structured JSON.

Usage:
    python3 scripts/scrape_company.py URL [URL ...] [--session SESSION] [--output FILE] [--delay SECONDS]

Options:
    --session  Path to session.json (default: session.json)
    --output   Output file path; prints to stdout if omitted
    --delay    Delay in seconds between requests (default: 2)

Output is a JSON array of company objects with fields:
    name, industry, company_size, headquarters, founded,
    specialties[], about, linkedin_url
"""

import argparse
import asyncio
import json
import sys

try:
    from linkedin_scraper import BrowserManager, CompanyScraper
except ImportError:
    print("Error: linkedin_scraper not installed. Run: pip install linkedin-scraper && playwright install chromium")
    sys.exit(1)


async def scrape_companies(urls: list[str], session_path: str, delay: float) -> list[dict]:
    results = []
    async with BrowserManager(headless=True) as browser:
        await browser.load_session(session_path)
        scraper = CompanyScraper(browser.page)

        for i, url in enumerate(urls):
            try:
                company = await scraper.scrape(url)
                results.append(company.model_dump())
            except Exception as e:
                results.append({"linkedin_url": url, "error": str(e)})

            if i < len(urls) - 1:
                await asyncio.sleep(delay)

    return results


def main():
    parser = argparse.ArgumentParser(description="Scrape LinkedIn company pages")
    parser.add_argument("urls", nargs="+", help="LinkedIn company page URLs")
    parser.add_argument("--session", default="session.json", help="Session file path")
    parser.add_argument("--output", help="Output JSON file path")
    parser.add_argument("--delay", type=float, default=2.0, help="Delay between requests in seconds")
    args = parser.parse_args()

    results = asyncio.run(scrape_companies(args.urls, args.session, args.delay))
    output = json.dumps(results, indent=2, default=str)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Results written to {args.output}")
    else:
        print(output)


if __name__ == "__main__":
    main()
