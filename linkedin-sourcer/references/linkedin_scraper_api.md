# linkedin_scraper API Reference

## Installation

```bash
pip install linkedin-scraper
playwright install chromium
```

## Authentication & Session Management

All scraping requires an authenticated session. Create one first:

```python
from linkedin_scraper import BrowserManager, wait_for_manual_login

async with BrowserManager(headless=False) as browser:
    await browser.page.goto("https://www.linkedin.com/login")
    await wait_for_manual_login(browser.page, timeout=300)
    await browser.save_session("session.json")
```

Or use `scripts/create_session.py` directly.

Reuse sessions in subsequent runs:
```python
async with BrowserManager(headless=True) as browser:
    await browser.load_session("session.json")
    # ... scrape
```

### BrowserManager Options

```python
BrowserManager(
    headless=True,       # False to show browser
    slow_mo=100,         # ms delay between actions
    viewport={"width": 1920, "height": 1080},
    user_agent="..."
)
```

## Scrapers

### PersonScraper

```python
from linkedin_scraper import PersonScraper

scraper = PersonScraper(browser.page)
person = await scraper.scrape("https://linkedin.com/in/username")
```

Returns `Person` model.

### CompanyScraper

```python
from linkedin_scraper import CompanyScraper

scraper = CompanyScraper(browser.page)
company = await scraper.scrape("https://linkedin.com/company/name/")
```

Returns `Company` model.

### CompanyPostsScraper

```python
from linkedin_scraper import CompanyPostsScraper

scraper = CompanyPostsScraper(browser.page)
posts = await scraper.scrape("https://linkedin.com/company/name/", limit=10)
```

Returns `list[Post]`.

## Data Models (Pydantic)

### Person
| Field | Type | Description |
|-------|------|-------------|
| name | str | Full name |
| headline | Optional[str] | Professional headline |
| location | Optional[str] | Location |
| about | Optional[str] | About/summary section |
| linkedin_url | str | Profile URL |
| experiences | list[Experience] | Work history |
| educations | list[Education] | Education history |
| skills | list[str] | Listed skills |
| accomplishments | Optional[Accomplishment] | Accomplishments section |

### Experience
| Field | Type |
|-------|------|
| title | str |
| company | str |
| location | Optional[str] |
| duration | Optional[str] |
| description | Optional[str] |

### Education
| Field | Type |
|-------|------|
| institution | str |
| degree | Optional[str] |
| field_of_study | Optional[str] |
| dates | Optional[str] |

### Company
| Field | Type |
|-------|------|
| name | str |
| industry | Optional[str] |
| company_size | Optional[str] |
| headquarters | Optional[str] |
| founded | Optional[str] |
| specialties | list[str] |
| about | Optional[str] |
| linkedin_url | str |

### Post
| Field | Type |
|-------|------|
| linkedin_url | Optional[str] |
| urn | Optional[str] |
| text | Optional[str] |
| posted_date | Optional[str] |
| reactions_count | Optional[int] |
| comments_count | Optional[int] |
| reposts_count | Optional[int] |
| image_urls | list[str] |

## Error Handling

```python
from linkedin_scraper import AuthenticationError, RateLimitError, ProfileNotFoundError

try:
    person = await scraper.scrape(url)
except AuthenticationError:
    # Session expired — recreate with create_session.py
except RateLimitError:
    # Back off and retry after delay
except ProfileNotFoundError:
    # Profile doesn't exist or is private
```

## Best Practices

- Add `await asyncio.sleep(2)` between requests to avoid rate limiting
- Save and reuse sessions — don't log in repeatedly
- Use `headless=False` during development, `True` for batch runs
- Always wrap scraping calls in try/except for graceful error handling
