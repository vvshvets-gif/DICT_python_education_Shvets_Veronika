import random

choices = ["rock", "paper", "scissors"]

user = input("> ")
computer = random.choice(choices)

if user == computer:
    print(f"There is a draw ({computer})")
elif (
    (user == "rock" and computer == "scissors") or
    (user == "scissors" and computer == "paper") or
    (user == "paper" and computer == "rock")
):
    print(f"Well done. The computer chose {computer} and failed")
else:
    print(f"Sorry, but the computer chose {computer}")