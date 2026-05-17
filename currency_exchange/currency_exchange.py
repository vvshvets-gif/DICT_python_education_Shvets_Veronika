RATES = {
    "ARS": 0.82,
    "HNL": 0.17,
    "AUD": 1.9622,
    "MAD": 0.208,
}

mycoins = float(input("> "))

for currency, rate in RATES.items():
    amount = round(mycoins * rate, 2)
    print(f"I will get {amount} {currency} from the sale of {mycoins} mycoins.")
