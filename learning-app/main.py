"""
Learning App - FastAPI server.
Paste a YouTube or article link, get 3 versions: full, notes, simplified.
"""
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from extractor import extract
from ai import summarize

app = FastAPI(title="Learning App")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    # Show the paste-link form
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/learn", response_class=HTMLResponse)
def learn(request: Request, url: str = Form(...)):
    # Form(...) means "this comes from a posted HTML form, required"
    try:
        extracted = extract(url)
        result = summarize(extracted["text"])
        ctx = {
            "request": request,
            "url": url,
            "kind": extracted["kind"],
            "full": result["full"],
            "notes": result["notes"],
            "simplified": result["simplified"],
            "brain_used": result["brain_used"],
            "error": None,
        }
    except Exception as e:
        ctx = {
            "request": request,
            "url": url,
            "kind": None,
            "full": None,
            "notes": None,
            "simplified": None,
            "brain_used": None,
            "error": str(e),
        }
    return templates.TemplateResponse("results.html", ctx)
