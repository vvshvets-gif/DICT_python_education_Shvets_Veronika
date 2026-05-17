import random

a = random.randint(2, 9)
b = random.randint(2, 9)

operations = {
    '+': a + b,
    '-': a - b,
    '*': a * b
}

op = random.choice(list(operations.keys()))

print(f"{a} {op} {b}")

answer = int(input())

if answer == operations[op]:
    print("Right!")
else:
    print("Wrong!")