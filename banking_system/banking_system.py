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
2. Log out
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


def account_session(conn, card):
    while True:
        print(ACCOUNT_MENU)
        choice = input(">")

        if choice == "1":
            row = conn.execute("SELECT balance FROM card WHERE number = ?", (card,)).fetchone()
            print(f"\nBalance: {row[0]}")
        elif choice == "2":
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
