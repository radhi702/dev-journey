# Job Scraper

Fetches remote jobs from remoteok.com, filters for automation/Python/n8n roles,
saves them to a log, and sends top results to Telegram.

## Setup

```bash
cd projects/job-scraper
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then fill in real values
```

## Run

```bash
python src/job_scraper.py
```

Matched jobs go to `logs/job-listings.txt`.

## Tests

Tests mock the Gemini API at the network boundary, so they run offline and
do not consume API quota.

```bash
pytest          # quiet
pytest -v       # verbose (shows each test name)
```
