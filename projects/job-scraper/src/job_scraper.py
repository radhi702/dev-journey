import os
import json
import requests
import urllib.request
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

def get_jobs():
    response = requests.get('https://remoteok.com/api', headers={'User-Agent': 'Mozilla/5.0'})
    all_jobs = response.json()

    # First item is info about the API, skip it
    all_jobs = all_jobs[1:]

    # Filter jobs related to automation, python, or n8n
    keywords = ['automation', 'python', 'n8n', 'zapier', 'integrations', 'api', 'scripting', 'bot']
    matching_jobs = []

    for job in all_jobs:
        title = job.get('position', '').lower()
        tags = [tag.lower() for tag in job.get('tags', [])]
        company = job.get('company', '')
        url = job.get('url', '')

        for keyword in keywords:
            if keyword in title or keyword in tags:
                matching_jobs.append({
                    'title': job.get('position', ''),
                    'company': company,
                    'tags': job.get('tags', []),
                    'url': f'https://remoteok.com{url}',
                    'date': job.get('date', '')
                })
                break

    return matching_jobs

def save_to_file(jobs):
    date = datetime.now().strftime('%Y-%m-%d %H:%M')
    entry = f'\n--- {date} | Found {len(jobs)} jobs ---\n'

    for job in jobs:
        entry += f'Title: {job["title"]}\n'
        entry += f'Company: {job["company"]}\n'
        entry += f'Tags: {", ".join(job["tags"])}\n'
        entry += f'Link: {job["url"]}\n\n'

    with open('job-listings.txt', 'a') as f:
        f.write(entry)

def send_telegram(jobs):
    if len(jobs) == 0:
        message = 'Job Search: No matching remote jobs found today.'
    else:
        message = f'Found {len(jobs)} remote jobs:\n\n'
        for job in jobs[:5]:
            message += f'{job["title"]} at {job["company"]}\n'
            message += f'{job["url"]}\n\n'

    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    data = json.dumps({'chat_id': CHAT_ID, 'text': message}).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    urllib.request.urlopen(req)

print('Searching for remote automation jobs...\n')
jobs = get_jobs()
print(f'Found {len(jobs)} matching jobs!\n')

for job in jobs[:5]:
    print(f'{job["title"]} at {job["company"]}')
    print(f'  Tags: {", ".join(job["tags"])}')
    print(f'  Link: {job["url"]}')
    print()

save_to_file(jobs)
print('Saved to job-listings.txt')
send_telegram(jobs)
print('Sent to Telegram!')
