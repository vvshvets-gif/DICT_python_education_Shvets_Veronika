import requests

base = input("> ").lower()

data = requests.get(f"http://www.floatrates.com/daily/{base}.json").json()

cache = {
    "usd": data["usd"]["rate"],
    "eur": data["eur"]["rate"],
}

while True:
    target = input("> ").lower()
    if not target:
        break

    amount = float(input("> "))

    print("Checking the cache...")

    if target not in cache:
        print("Sorry, but it is not in the cache!")
        cache[target] = data[target]["rate"]
    else:
        print("It is in the cache!")

    result = round(amount * cache[target], 2)
    print(f"You received {result} {target.upper()}.")
