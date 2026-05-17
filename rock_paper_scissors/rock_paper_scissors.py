import random

DEFAULT_OPTIONS = ["rock", "paper", "scissors"]
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


def build_win_map(options):
    """
    For each option, determine which options it beats.
    The 'rotated' list (items after + items before) has:
      - first half: options that beat the current one
      - second half: options beaten by the current one
    """
    win_map = {}
    n = len(options)
    half = n // 2
    for i, option in enumerate(options):
        rotated = options[i + 1:] + options[:i]
        win_map[option] = set(rotated[half:])
    return win_map


def get_outcome(user, computer, win_map):
    if user == computer:
        return "draw"
    if computer in win_map[user]:
        return "win"
    return "lose"


name = input("Enter your name: ")
print(f"Hello, {name}")

score = load_rating(name)

raw = input("> ")
options = [o.strip() for o in raw.split(",")] if raw.strip() else DEFAULT_OPTIONS
win_map = build_win_map(options)

print("Okay, let's start")

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

    computer = random.choice(options)
    outcome = get_outcome(user, computer, win_map)

    if outcome == "draw":
        print(f"There is a draw ({computer})")
    elif outcome == "lose":
        print(f"Sorry, but the computer chose {computer}")
    else:
        print(f"Well done. The computer chose {computer} and failed")

    score += SCORES[outcome]
