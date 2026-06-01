import requests
from bs4 import BeautifulSoup

# Step 1: Download the webpage
response = requests.get('http://quotes.toscrape.com')
html = response.text

# Step 2: Parse it with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Step 3: Find all quotes on the page
quotes = soup.find_all('div', class_='quote')

# Step 4: Extract and print each quote
for quote in quotes:
    text = quote.find('span', class_='text').get_text()
    author = quote.find('small', class_='author').get_text()
    print(f'{text}')
    print(f'  — {author}')
    print()
