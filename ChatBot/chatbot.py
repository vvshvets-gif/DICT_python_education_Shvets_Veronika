print('Hello! My name is DICT_Bot')
print('I was created in 2025')
print('Please, remind me your name.')

name_input = input()

print(f"What a great name you have, {name_input}!")

print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

remainder3_input = int(input())
remainder5_input = int(input())
remainder7_input = int(input())

remainder3 = remainder3_input % 3
remainder5 = remainder5_input % 5
remainder7 = remainder7_input % 7

age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

print(f"Your age is {age}; that's a good time to start programming")

print('Now I will prove to you that I can count to any number you want.')

number_input = int(input()) + 1

for number in range(number_input):
    print(f" {number} !")

print('Completed, have a nice day!')

print("Let's test your programming knowledge.")

questions = [
    ('Why do we use methods?',
     [
        ('To repeat a statement multiple times.', False),
        ('To decompose a program into several small subroutines.', True),
        ('To determine the execution time of a program.', False),
        ('To interrupt the execution of a program.', False)
     ]
    )
]

for question, answers in questions:
    print(f"Question: {question}")
    for index, (answer, condition) in enumerate(answers):
        print(f"{index + 1}. {answer}")

while True:
    print(f"Please enter your answer.")
    answer_input = int(input())
    (question, answers) = questions[0]
    (answer, condition) = answers[answer_input - 1]

    if condition:
        print("Completed, have a nice day!")
        break
    else:
        print("Please, try again.")

print("Congratulations, have a nice day!")
print('Hello! My name is DICT_Bot')
print('I was created in 2025')
print('Please, remind me your name.')
