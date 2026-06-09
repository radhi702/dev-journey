"""
Extractor - pulls plain text from a YouTube video OR an article URL.
"""
import re
import requests
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound


def is_youtube_url(url: str) -> bool:
    # Covers youtube.com, youtu.be, m.youtube.com, music.youtube.com
    return "youtube.com" in url or "youtu.be" in url


def extract_youtube_id(url: str) -> str:
    # Video ID is always 11 characters: letters, digits, _ or -
    match = re.search(r"(?:v=|youtu\.be/|/shorts/|/embed/)([A-Za-z0-9_-]{11})", url)
    if not match:
        raise ValueError("Could not find a YouTube video ID in that link.")
    return match.group(1)


def get_youtube_text(url: str) -> str:
    video_id = extract_youtube_id(url)
    try:
        api = YouTubeTranscriptApi()
        fetched = api.fetch(video_id)
        # Each snippet has .text, .start, .duration
        return " ".join(snippet.text for snippet in fetched)
    except (TranscriptsDisabled, NoTranscriptFound):
        raise ValueError("This video has no captions, so I cannot read it.")
    except Exception as e:
        raise ValueError(f"Could not get YouTube transcript: {e}")


def get_article_text(url: str) -> str:
    # Pretend to be a real browser so sites do not block us
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }
    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Drop non-content tags so we keep only readable text
    for tag in soup(["script", "style", "nav", "footer", "header", "aside", "noscript"]):
        tag.decompose()

    # Prefer the main article/main tag if the site uses one
    container = soup.find("article") or soup.find("main") or soup.body or soup
    text = container.get_text(separator=" ", strip=True)

    # Collapse repeated whitespace into single spaces
    text = re.sub(r"\s+", " ", text).strip()

    if len(text) < 100:
        raise ValueError("The article page returned almost no readable text.")
    return text


def extract(url: str) -> dict:
    """Returns {'kind': 'youtube'|'article', 'text': '...'}."""
    if is_youtube_url(url):
        return {"kind": "youtube", "text": get_youtube_text(url)}
    return {"kind": "article", "text": get_article_text(url)}
