user = input("> ")

win_map = {
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock"
}

print(f"Sorry, but the computer chose {win_map[user]}")