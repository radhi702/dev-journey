import os
import json
import urllib.request
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv('GITHUB_USERNAME')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

def get_github_activity():
    url = f'https://api.github.com/users/{USERNAME}/events/public'
    req = urllib.request.Request(url, headers={'User-Agent': 'Python'})
    response = urllib.request.urlopen(req)
    events = json.loads(response.read())

    one_day_ago = datetime.now() - timedelta(hours=24)
    recent_pushes = [
        event for event in events
        if event['type'] == 'PushEvent'
        and datetime.strptime(event['created_at'], '%Y-%m-%dT%H:%M:%SZ') > one_day_ago
    ]
    return recent_pushes

def create_summary(pushes):
    if len(pushes) == 0:
        return 'No GitHub activity in the last 24 hours.'

    total_pushes = 0
    repos = set()

    for push in pushes:
        total_pushes += 1
        repos.add(push['repo']['name'])

    repo_list = ', '.join(repos)
    return f'GitHub Activity Summary:\nTotal pushes: {total_pushes}\nRepos: {repo_list}'

def save_to_file(summary):
    date = datetime.now().strftime('%Y-%m-%d')
    entry = f'\n--- {date} ---\n{summary}\n'
    with open('github-activity-log.txt', 'a') as f:
        f.write(entry)

def send_telegram(summary):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    data = json.dumps({'chat_id': CHAT_ID, 'text': summary}).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    urllib.request.urlopen(req)

print('Checking GitHub activity...')
pushes = get_github_activity()
summary = create_summary(pushes)
save_to_file(summary)
print('Saved to file!')
send_telegram(summary)
print('Sent to Telegram!')
print(summary)
