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

for _ in range(5):
    a = random.randint(2, 9)
    b = random.randint(2, 9)

    op = random.choice(list(operations.keys()))

    print(f"{a} {op} {b}")

    while True:
        try:
            answer = int(input())
            break
        except ValueError:
            print("Incorrect format.")

    if answer == operations[op]:
        print("Right!")
        score += 1
    else:
        print("Wrong!")

print(f"Your mark is {score}/5.")