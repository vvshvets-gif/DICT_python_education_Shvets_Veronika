import random

score = 0

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

operations = {
    '+': add,
    '-': sub,
    '*': mul
}

def generate_task(level):
    if level == 1:
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        op = random.choice(list(operations.keys()))

        question = f"{a} {op} {b}"
        answer = operations[op](a, b)
        
        return question, answer

    if level == 2:
        a = random.randint(11, 29)
        question = f"{a}"
        answer = a * a
        return question, answer

def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Incorrect format.")
            
while True:
    try:
        level = int(input(
            "Which level do you want? Enter a number:\n"
            "1 - simple operations with numbers 2-9\n"
            "2 - integral squares of 11-29\n> "
        ))
        if level in (1, 2):
            break
    except ValueError:
        pass
    print("Incorrect format.")
    
for _ in range(5):
    q, correct = generate_task(level)
    print(q)

    while True:
        try:
            user = int(input("> "))
            break
        except ValueError:
            print("Incorrect format.")

    if user == correct:
        print("Right!")
        score += 1
    else:
        print("Wrong!")

print(f"Your mark is {score}/5.")

save = input("Would you like to save your result to the file?\nEnter yes or no.\n> ")

if save.lower() in ("yes", "y"):
    name = input("What is your name?\n> ")
    description = (
        "simple operations with numbers 2-9"
        if level == 1
        else "integral squares of 11-29"
    )
    with open("results.txt", "a") as f:
        f.write(f"{name}: {score}/5 in level {level} ({description}).\n")
else:
    exit()