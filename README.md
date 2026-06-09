# dev-journey

Radhika's 6-month automation engineer roadmap. Daily practice files + portfolio projects + n8n workflows.

## Layout

```
learning/           Daily practice (Python, JavaScript, notes).
learning-app/       Active project: FastAPI web app — paste a YouTube/article link, get AI-generated notes.
projects/           Portfolio projects. Each has src/, tests/, requirements.txt, README, .env.example.
n8n-workflows/      Exported n8n workflow JSONs.
notes/              Cheatsheets, roadmap, git notes.
```

## Projects

| Folder | What it does |
|---|---|
| `learning-app/` (root) | FastAPI web app with AI summaries. Currently in active development. |
| `projects/fastapi-app` | Practice REST API built with FastAPI. |
| `projects/api-health-checker` | Pings APIs, alerts via Telegram if any go down. |
| `projects/job-scraper` | Pulls remote automation jobs from remoteok.com. |
| `projects/github-tracker` | Summarises GitHub activity, sends to Telegram. |
| `projects/data-processor` | Cleans JSON data (called from n8n). |
| `projects/learning-app` | Yesterday's empty stub scaffold (kept for reference). |

Each project's README has its own setup and run instructions.
