# API Health Checker

Pings a list of APIs, logs status to a file, and sends a Telegram alert if any are down.

## Setup

```bash
cd projects/api-health-checker
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then fill in real values
```

## Run

```bash
python src/api_health_checker.py
```

Logs go to `logs/api-health-log.txt`.
