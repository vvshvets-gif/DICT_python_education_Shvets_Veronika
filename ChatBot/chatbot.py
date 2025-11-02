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