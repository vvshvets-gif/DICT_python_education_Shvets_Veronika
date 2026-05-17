import requests

url = input("Input the URL:\n> ")

response = requests.get(url)

if response.status_code != 200:
    print(f"The URL returned {response.status_code}!")
else:
    with open("source.html", "wb") as f:
        f.write(response.content)
    print("Content saved.")
