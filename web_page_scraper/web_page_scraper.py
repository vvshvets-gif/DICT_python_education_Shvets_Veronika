import requests
from bs4 import BeautifulSoup
import string

HEADERS = {'Accept-Language': 'en-US,en;q=0.5'}
BASE_URL = "https://www.nature.com"
LIST_URL = "https://www.nature.com/nature/articles?sort=PubDate&year=2022&page=3"

punct_table = str.maketrans("", "", string.punctuation)


def make_filename(title):
    clean = title.strip().translate(punct_table)
    return "_".join(clean.split()) + ".txt"


def fetch_article_body(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    body = soup.find('div', {'class': lambda c: c and 'body' in c})
    return body.get_text(strip=True) if body else ""


page = requests.get(LIST_URL, headers=HEADERS)
soup = BeautifulSoup(page.content, 'html.parser')

saved = []

for article in soup.find_all('article'):
    type_span = article.find('span', {'data-test': 'article.type'})
    if not type_span or type_span.get_text(strip=True) != 'News':
        continue

    link_tag = article.find('a', {'data-track-action': 'view article'})
    title_tag = article.find('h3')
    if not link_tag or not title_tag:
        continue

    title = title_tag.get_text(strip=True)
    filename = make_filename(title)
    article_url = BASE_URL + link_tag['href']

    body_text = fetch_article_body(article_url)

    with open(filename, "wb") as f:
        f.write(body_text.encode('utf-8'))

    saved.append(filename)

print(f"Saved articles: {saved}")
