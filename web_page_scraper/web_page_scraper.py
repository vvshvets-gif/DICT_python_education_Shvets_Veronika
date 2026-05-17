import requests

url = input("Input the URL:\n> ")

response = requests.get(url)

if response.status_code != 200:
    print("Invalid quote resource!")
else:
    data = response.json()
    content = data.get("content")
    if not content:
        print("Invalid quote resource!")
    else:
        print(content)
