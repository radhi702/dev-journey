# GitHub Tracker

Summarises a GitHub user's public pushes in the last 24 hours.
Logs the summary and sends it to Telegram.

## Setup

```bash
cd projects/github-tracker
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then fill in real values
```

## Run

```bash
python src/github_tracker.py
```

Activity log goes to `logs/github-activity-log.txt`.
