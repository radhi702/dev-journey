import os
import json
import time
import requests
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

from job_scorer import score_job

# Anchor paths to this script's own location so the code is cwd-independent.
SCRIPT_DIR = Path(__file__).resolve().parent           # projects/job-scraper/src/
PROJECT_ROOT = SCRIPT_DIR.parent                       # projects/job-scraper/
LOGS_DIR = PROJECT_ROOT / 'logs'
LOG_FILE = LOGS_DIR / 'job-listings.txt'

# Ensure logs/ exists. mkdir is idempotent with exist_ok=True.
LOGS_DIR.mkdir(parents=True, exist_ok=True)

# Load env from the project's own .env, not the root .env or the cwd.
load_dotenv(PROJECT_ROOT / '.env')

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

# Tunables (constants at the top — easy to change without hunting through code).
REMOTEOK_URL = 'https://remoteok.com/api'
TELEGRAM_URL = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
KEYWORDS = ['automation', 'python', 'n8n', 'zapier', 'integrations', 'api', 'scripting', 'bot']
MAX_JOBS_TO_SCORE = 10           # cap per run to respect Gemini free-tier rate limit
SLEEP_BETWEEN_SCORES = 1.0       # seconds; defensive pacing under rate limit
MIN_SCORE_TO_ALERT = 7           # only jobs scoring >= this go to Telegram


def get_jobs():
    """Fetch jobs from RemoteOK, filter by keywords. Returns [] on any failure."""
    try:
        response = requests.get(
            REMOTEOK_URL,
            headers={'User-Agent': 'Mozilla/5.0'},
            timeout=15,
        )
        response.raise_for_status()
        all_jobs = response.json()
    except requests.RequestException as e:
        print(f'RemoteOK fetch failed: {type(e).__name__}: {e}')
        return []

    # First item is API metadata, skip it.
    all_jobs = all_jobs[1:]

    matching_jobs = []
    for job in all_jobs:
        title = job.get('position', '').lower()
        tags = [tag.lower() for tag in job.get('tags', [])]
        company = job.get('company', '')
        url = job.get('url', '')

        for keyword in KEYWORDS:
            if keyword in title or keyword in tags:
                matching_jobs.append({
                    'title': job.get('position', ''),
                    'company': company,
                    'tags': job.get('tags', []),
                    'url': f'https://remoteok.com{url}',
                    'date': job.get('date', ''),
                })
                break

    return matching_jobs


def save_to_file(jobs):
    """Append job listings with scores/reasons to the log file."""
    date = datetime.now().strftime('%Y-%m-%d %H:%M')
    entry = f'\n--- {date} | Found {len(jobs)} high-fit jobs ---\n'

    for job in jobs:
        score = job.get('score', '?')
        reason = job.get('score_reason', '')
        entry += f'Title: {job["title"]}\n'
        entry += f'Company: {job["company"]}\n'
        entry += f'Score: {score}/10\n'
        if reason:
            entry += f'Reason: {reason}\n'
        entry += f'Tags: {", ".join(job["tags"])}\n'
        entry += f'Link: {job["url"]}\n\n'

    with open(LOG_FILE, 'a') as f:
        f.write(entry)


def send_telegram(jobs):
    """Send high-fit jobs (or 'none found' notice) to Telegram. Logs but doesn't raise on failure."""
    if len(jobs) == 0:
        message = 'Job Search: No matching remote jobs found today.'
    else:
        message = f'Found {len(jobs)} high-fit remote jobs:\n\n'
        for job in jobs[:5]:
            score = job.get('score', '?')
            message += f'[{score}/10] {job["title"]} at {job["company"]}\n'
            message += f'{job["url"]}\n\n'

    try:
        response = requests.post(
            TELEGRAM_URL,
            json={'chat_id': CHAT_ID, 'text': message},
            timeout=10,
        )
        response.raise_for_status()
    except requests.RequestException as e:
        # Log but don't crash — the run already succeeded as far as scoring goes.
        print(f'Telegram send failed: {type(e).__name__}: {e}')


def main():
    print('Searching for remote automation jobs...\n')
    jobs = get_jobs()
    print(f'Found {len(jobs)} keyword-matching jobs.\n')

    # Cap to stay well under Gemini's free-tier rate limit (15 req/min).
    jobs_to_score = jobs[:MAX_JOBS_TO_SCORE]

    print(f'Scoring {len(jobs_to_score)} jobs with Gemini...')
    scored_jobs = []
    for i, job in enumerate(jobs_to_score):
        result = score_job(job)
        job_with_score = {**job, 'score': result['score'], 'score_reason': result['reason']}
        scored_jobs.append(job_with_score)
        print(f'  [{result["score"]}] {job["title"][:60]}')
        # Pacing between calls — defensive under the rate limit, prevents bursts.
        if i < len(jobs_to_score) - 1:
            time.sleep(SLEEP_BETWEEN_SCORES)

    # Keep only high-fit. Drop None scores (failed API calls).
    high_fit_jobs = [
        j for j in scored_jobs
        if j['score'] is not None and j['score'] >= MIN_SCORE_TO_ALERT
    ]
    print(f'\nKept {len(high_fit_jobs)} high-fit jobs (score >= {MIN_SCORE_TO_ALERT}) out of {len(scored_jobs)}.')

    save_to_file(high_fit_jobs)
    print('Saved to logs/job-listings.txt')

    send_telegram(high_fit_jobs)
    print('Sent to Telegram!')


if __name__ == '__main__':
    main()
