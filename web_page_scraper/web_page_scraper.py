import requests
from bs4 import BeautifulSoup
import string
import os

HEADERS = {'Accept-Language': 'en-US,en;q=0.5'}
BASE_URL = "https://www.nature.com"

punct_table = str.maketrans("", "", string.punctuation)


def make_filename(title):
    clean = title.strip().translate(punct_table)
    return "_".join(clean.split()) + ".txt"


def fetch_article_body(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    for selector in [
        {'class': lambda c: c and 'body' in c.split()},
        {'class': lambda c: c and 'article' in c.split()},
        {'id': 'content'},
    ]:
        body = soup.find('div', selector)
        if body:
            return body.get_text(strip=True)
    return ""


num_pages = int(input())
article_type = input()

for page_num in range(1, num_pages + 1):
    url = f"https://www.nature.com/nature/articles?sort=PubDate&year=2022&page={page_num}"
    page = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')

    directory = f"Page_{page_num}"
    os.makedirs(directory, exist_ok=True)

    for article in soup.find_all('article'):
        type_span = article.find('span', {'data-test': 'article.type'})
        if not type_span or type_span.get_text(strip=True) != article_type:
            continue

        link_tag = article.find('a', {'data-track-action': 'view article'})
        title_tag = article.find('h3')
        if not link_tag or not title_tag:
            continue

        title = title_tag.get_text(strip=True)
        filename = make_filename(title)
        article_url = BASE_URL + link_tag['href']

        body_text = fetch_article_body(article_url)

        with open(os.path.join(directory, filename), "wb") as f:
            f.write(body_text.encode('utf-8'))

print("Saved all articles.")
