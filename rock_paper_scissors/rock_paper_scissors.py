import random

win_map = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}

SCORES = {"win": 100, "draw": 50, "lose": 0}


def load_rating(name):
    try:
        with open("rating.txt") as f:
            for line in f:
                parts = line.split()
                if parts[0] == name:
                    return int(parts[1])
    except FileNotFoundError:
        pass
    return 0


name = input("Enter your name: ")
print(f"Hello, {name}")

score = load_rating(name)

while True:
    user = input("> ")

    if user == "!exit":
        print("Bye!")
        break

    if user == "!rating":
        print(f"Your rating: {score}")
        continue

    if user not in win_map:
        print("Invalid input")
        continue

    computer = random.choice(list(win_map.keys()))

    if user == computer:
        print(f"There is a draw ({computer})")
        score += SCORES["draw"]
    elif win_map[user] == computer:
        print(f"Sorry, but the computer chose {computer}")
        score += SCORES["lose"]
    else:
        print(f"Well done. The computer chose {computer} and failed")
        score += SCORES["win"]