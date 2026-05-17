import math

principal = int(input("Enter the loan principal:\n> "))

print('What do you want to calculate?\ntype "m" – for number of monthly payments,\ntype "p" – for the monthly payment:')
choice = input("> ")

if choice == "m":
    payment = int(input("Enter the monthly payment:\n> "))
    months = math.ceil(principal / payment)
    print(f"It will take {months} month{'s' if months > 1 else ''} to repay the loan")

elif choice == "p":
    months = int(input("Enter the number of months:\n> "))
    payment = math.ceil(principal / months)
    last_payment = principal - (months - 1) * payment
    if last_payment == payment:
        print(f"Your monthly payment = {payment}")
    else:
        print(f"Your monthly payment = {payment} and the last payment = {last_payment}.")
