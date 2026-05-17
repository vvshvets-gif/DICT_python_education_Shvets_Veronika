import requests

currency = input("Enter the currency code: ").lower()

response = requests.get(f"http://www.floatrates.com/daily/{currency}.json")
data = response.json()

print(data["usd"])
print(data["eur"])
