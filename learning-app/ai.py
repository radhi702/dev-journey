"""
AI brain - Gemini primary, Groq backup.
Returns 3 versions of the content: full, notes, simplified.
"""
import os
import re
from dotenv import load_dotenv
import google.generativeai as genai
from groq import Groq

load_dotenv()

GEMINI_KEY = os.getenv("GEMINI_API_KEY", "").strip()
GROQ_KEY = os.getenv("GROQ_API_KEY", "").strip()

# Only set up Gemini if a real key is present
if GEMINI_KEY and not GEMINI_KEY.startswith("paste-"):
    genai.configure(api_key=GEMINI_KEY)


PROMPT = """You are a friendly teacher helping a beginner learner.
Take the content below and produce EXACTLY three sections,
separated by these exact marker lines:

===FULL===
A clean rewrite of the entire content as readable paragraphs.
Keep all the important information. No bullet points here.

===NOTES===
Structured study notes. Use markdown headings like '## Topic Name' for
each different topic. Under each heading write a short paragraph plus
bullet points where helpful. Cover everything important.

===SIMPLIFIED===
A super beginner-friendly explanation in very simple English.
When you use a hard or technical word, put a short meaning in
brackets right after the word. Example:
"An API (a way for apps to talk to each other) sends data."
Feel like a kind teacher explaining to a kid.

Here is the content:
\"\"\"
{content}
\"\"\"
"""


def _call_gemini(text: str) -> str:
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(PROMPT.format(content=text))
    return response.text


def _call_groq(text: str) -> str:
    client = Groq(api_key=GROQ_KEY)
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": PROMPT.format(content=text)}],
    )
    return response.choices[0].message.content


def _parse_three_sections(raw: str) -> dict:
    sections = {"full": "", "notes": "", "simplified": ""}
    parts = re.split(r"===\s*(FULL|NOTES|SIMPLIFIED)\s*===", raw)
    # parts = ['', 'FULL', '<body>', 'NOTES', '<body>', 'SIMPLIFIED', '<body>']
    for i in range(1, len(parts), 2):
        name = parts[i].lower()
        body = parts[i + 1].strip() if i + 1 < len(parts) else ""
        if name in sections:
            sections[name] = body

    # If the AI did not follow the format, dump everything in 'full'
    if not any(sections.values()):
        sections["full"] = raw.strip()
        sections["notes"] = "(The AI did not return notes in the expected format.)"
        sections["simplified"] = "(The AI did not return simplified text in the expected format.)"

    return sections


def summarize(text: str) -> dict:
    """Returns {'full', 'notes', 'simplified', 'brain_used'}."""
    # Cap input length so we do not blow past free-tier token limits
    if len(text) > 30000:
        text = text[:30000]

    brain_used = "gemini"
    gemini_error = None
    groq_error = None
    raw = None

    try:
        if not GEMINI_KEY or GEMINI_KEY.startswith("paste-"):
            raise RuntimeError("No Gemini key found in .env")
        raw = _call_gemini(text)
    except Exception as e:
        gemini_error = str(e)
        try:
            if not GROQ_KEY or GROQ_KEY.startswith("paste-"):
                raise RuntimeError("No Groq key found in .env")
            raw = _call_groq(text)
            brain_used = "groq (fallback)"
        except Exception as e2:
            groq_error = str(e2)

    if raw is None:
        raise RuntimeError(
            f"Both AI brains failed.\nGemini: {gemini_error}\nGroq: {groq_error}"
        )

    result = _parse_three_sections(raw)
    result["brain_used"] = brain_used
    return result
