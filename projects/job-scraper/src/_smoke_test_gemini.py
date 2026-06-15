import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# Load .env from the project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / '.env')

# New SDK uses a Client object instead of module-level configure()
client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

# Generate content via the client's models attribute
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='Say hi in one word.'
)

print('Gemini said:', response.text)
