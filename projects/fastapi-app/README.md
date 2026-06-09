# FastAPI App

Practice API built with FastAPI. Exposes home, about, greet, and add endpoints.

## Setup

```bash
cd projects/fastapi-app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn src.main:app --reload
```

Open http://localhost:8000 in the browser.
Open http://localhost:8000/docs for the auto-generated API docs.
