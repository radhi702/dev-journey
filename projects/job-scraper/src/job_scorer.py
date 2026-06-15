import os
import json
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import types

  # Anchor paths to this script's location (cwd-independent).
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

  # Load environment variables from the project's own .env.
load_dotenv(PROJECT_ROOT / '.env')

  # Load the prompt template once at module load (not per call).
PROMPT_PATH = SCRIPT_DIR / 'prompts' / 'score_v1.txt'
PROMPT_TEMPLATE = PROMPT_PATH.read_text(encoding='utf-8')

  # Initialize the Gemini client once at module load.
client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))


def score_job(job: dict) -> dict:
    """
    Score a single job dict for fit to the candidate profile.

    Args:
        job: dict with keys 'title' (str), 'company' (str), 'tags' (list of str)

    Returns:
        dict with keys 'score' (int 1-10 or None on failure) and 'reason' (str)
    """
    try:
          # Build the filled prompt by substituting the job fields into the template.
        filled_prompt = PROMPT_TEMPLATE.format(
            title=job.get('title', ''),
            company=job.get('company', ''),
            tags=', '.join(job.get('tags', [])),
        )

          # Call Gemini, forcing JSON-shaped output.
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=filled_prompt,
            config=types.GenerateContentConfig(
                response_mime_type='application/json',
            ),
        )

          # Parse the JSON response into a Python dict.
        parsed = json.loads(response.text)
        return {
            'score': int(parsed['score']),
            'reason': str(parsed['reason']),
        }

    except Exception as e:
          # Fail-safe: never let one bad call crash the pipeline.
        return {
            'score': None,
            'reason': f'scoring failed: {type(e).__name__}: {e}',
        }


  # Test block — runs only when this file is executed directly,
  # not when it's imported by another file (like job_scraper.py).


if __name__ == '__main__':
    sample = {
        'title': 'iOS Mobile Engineer',
        'company': 'Acme',
        'tags': ['ios', 'swift', 'mobile'],
    }
    result = score_job(sample)
    print(result)
