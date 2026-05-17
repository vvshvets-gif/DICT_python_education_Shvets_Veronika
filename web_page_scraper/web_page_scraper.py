import requests
from bs4 import BeautifulSoup
import json
import re

HEADERS = {'Accept-Language': 'en-US,en;q=0.5'}

url = input("Input the URL:\n> ")

if 'title' not in url:
    print("Invalid movie page!")
else:
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print("Invalid movie page!")
    else:
        soup = BeautifulSoup(response.content, 'html.parser')

        title_tag = soup.find('title')
        description_tag = soup.find('meta', {'name': 'description'})

        if not title_tag or not description_tag:
            print("Invalid movie page!")
        else:
            # strip " (year) - IMDb" suffix from title
            title = re.sub(r'\s*\(\d{4}\).*$', '', title_tag.text.strip())
            description = description_tag['content'].strip()

            print(json.dumps({"title": title, "description": description}))
