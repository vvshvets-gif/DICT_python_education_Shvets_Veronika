import random

win_map = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}

while True:
    user = input("> ")

    if user == "!exit":
        print("Bye!")
        break

    if user not in win_map:
        print("Invalid input")
        continue

    computer = random.choice(list(win_map.keys()))

    if user == computer:
        print(f"There is a draw ({computer})")
    elif win_map[user] == computer:
        print(f"Sorry, but the computer chose {computer}")
    else:
        print(f"Well done. The computer chose {computer} and failed")