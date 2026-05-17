import random

IIN = "400000"
accounts = {}

MAIN_MENU = """
1. Create an account
2. Log into account
0. Exit"""

ACCOUNT_MENU = """
1. Balance
2. Log out
0. Exit"""


def generate_card():
    while True:
        account_number = str(random.randint(0, 999999999)).zfill(9)
        card = IIN + account_number + "0"  # placeholder check digit
        if card not in accounts:
            return card


def generate_pin():
    return str(random.randint(0, 9999)).zfill(4)


def create_account():
    card = generate_card()
    pin = generate_pin()
    accounts[card] = {"pin": pin, "balance": 0}
    print(f"\nYour card has been created\nYour card number:\n{card}\nYour card PIN:\n{pin}")


def login():
    card = input("\nEnter your card number:\n>")
    pin = input("Enter your PIN:\n>")

    if card not in accounts or accounts[card]["pin"] != pin:
        print("\nWrong PIN!")
        return

    print("\nYou have successfully logged in!")
    account_session(card)


def account_session(card):
    while True:
        print(ACCOUNT_MENU)
        choice = input(">")

        if choice == "1":
            print(f"\nBalance: {accounts[card]['balance']}")
        elif choice == "2":
            print("\nYou have successfully logged out!")
            return
        elif choice == "0":
            print("\nBye!")
            exit()


while True:
    print(MAIN_MENU)
    choice = input(">")

    if choice == "1":
        create_account()
    elif choice == "2":
        login()
    elif choice == "0":
        print("\nBye!")
        break
