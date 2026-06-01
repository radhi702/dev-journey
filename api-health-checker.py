import os
import requests
from datetime import datetime
from dotenv import load_dotenv
import json
import urllib.request

load_dotenv()

APIS = os.getenv('APIS').split(',')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

def check_api(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return {'url': url, 'status': 'UP', 'code': 200}
        else:
            return {'url': url, 'status': 'DOWN', 'code': response.status_code}
    except Exception as e:
        return {'url': url, 'status': 'DOWN', 'code': str(e)}

def check_all_apis():
    results = []
    for api in APIS:
        print(f'Checking {api}...')
        result = check_api(api)
        results.append(result)
        if result['status'] == 'UP':
            print(f'  ✅ UP (200)')
        else:
            print(f'  ❌ DOWN ({result["code"]})')
    return results

def save_to_file(results):
    date = datetime.now().strftime('%Y-%m-%d %H:%M')
    entry = f'\n--- {date} ---\n'
    for r in results:
        entry += f'{r["status"]} | {r["url"]} | {r["code"]}\n'
    with open('api-health-log.txt', 'a') as f:
        f.write(entry)

def send_telegram(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    data = json.dumps({'chat_id': CHAT_ID, 'text': message}).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    urllib.request.urlopen(req)

def create_alert(results):
    down_apis = [r for r in results if r['status'] == 'DOWN']
    if len(down_apis) == 0:
        return None
    message = 'API ALERT - Some APIs are down:\n'
    for api in down_apis:
        message += f'❌ {api["url"]} ({api["code"]})\n'
    return message

print('API Health Checker starting...\n')
results = check_all_apis()
save_to_file(results)
print('\nSaved to api-health-log.txt')

alert = create_alert(results)
if alert:
    send_telegram(alert)
    print('Alert sent to Telegram!')
else:
    print('All APIs are up! No alert needed.')
