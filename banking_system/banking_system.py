import random
import sqlite3
import sys

IIN = "400000"
DB_FILE = sys.argv[1] if len(sys.argv) > 1 else "card.s3db"

MAIN_MENU = """
1. Create an account
2. Log into account
0. Exit"""

ACCOUNT_MENU = """
1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit"""


def init_db(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS card (
            id      INTEGER PRIMARY KEY,
            number  TEXT    NOT NULL,
            pin     TEXT    NOT NULL,
            balance INTEGER DEFAULT 0
        )
    """)
    conn.commit()


def luhn_check_digit(first_15):
    digits = [int(d) for d in first_15]
    for i in range(0, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    return (10 - sum(digits) % 10) % 10


def generate_card(conn):
    while True:
        account_number = str(random.randint(0, 999999999)).zfill(9)
        first_15 = IIN + account_number
        card = first_15 + str(luhn_check_digit(first_15))
        if not conn.execute("SELECT 1 FROM card WHERE number = ?", (card,)).fetchone():
            return card


def create_account(conn):
    card = generate_card(conn)
    pin = str(random.randint(0, 9999)).zfill(4)
    conn.execute("INSERT INTO card (number, pin) VALUES (?, ?)", (card, pin))
    conn.commit()
    print(f"\nYour card has been created\nYour card number:\n{card}\nYour card PIN:\n{pin}")


def login(conn):
    card = input("\nEnter your card number:\n>")
    row = conn.execute("SELECT pin, balance FROM card WHERE number = ?", (card,)).fetchone()

    if not row:
        print("\nWrong card number!")
        return

    pin = input("Enter your PIN:\n>")
    if row[0] != pin:
        print("\nWrong PIN!")
        return

    print("\nYou have successfully logged in!")
    account_session(conn, card)


def is_luhn_valid(card_number):
    digits = [int(d) for d in card_number]
    check = digits.pop()
    for i in range(0, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    return (sum(digits) + check) % 10 == 0


def add_income(conn, card):
    amount = int(input("\nEnter income:\n>"))
    conn.execute("UPDATE card SET balance = balance + ? WHERE number = ?", (amount, card))
    conn.commit()
    print("Income was added!")


def do_transfer(conn, card):
    print("\nTransfer")
    target = input("Enter card number:\n>")

    if target == card:
        print("You can't transfer money to the same account!")
        return
    if not is_luhn_valid(target):
        print("Probably you made a mistake in the card number. Please try again!")
        return
    if not conn.execute("SELECT 1 FROM card WHERE number = ?", (target,)).fetchone():
        print("Such a card does not exist.")
        return

    amount = int(input("Enter how much money you want to transfer:\n>"))
    balance = conn.execute("SELECT balance FROM card WHERE number = ?", (card,)).fetchone()[0]

    if amount > balance:
        print("Not enough money!")
        return

    conn.execute("UPDATE card SET balance = balance - ? WHERE number = ?", (amount, card))
    conn.execute("UPDATE card SET balance = balance + ? WHERE number = ?", (amount, target))
    conn.commit()
    print("Success!")


def account_session(conn, card):
    while True:
        print(ACCOUNT_MENU)
        choice = input(">")

        if choice == "1":
            row = conn.execute("SELECT balance FROM card WHERE number = ?", (card,)).fetchone()
            print(f"\nBalance: {row[0]}")
        elif choice == "2":
            add_income(conn, card)
        elif choice == "3":
            do_transfer(conn, card)
        elif choice == "4":
            conn.execute("DELETE FROM card WHERE number = ?", (card,))
            conn.commit()
            print("\nThe account has been closed!")
            return
        elif choice == "5":
            print("\nYou have successfully logged out!")
            return
        elif choice == "0":
            print("\nBye!")
            exit()


conn = sqlite3.connect(DB_FILE)
init_db(conn)

while True:
    print(MAIN_MENU)
    choice = input(">")

    if choice == "1":
        create_account(conn)
    elif choice == "2":
        login(conn)
    elif choice == "0":
        print("\nBye!")
        conn.close()
        break
