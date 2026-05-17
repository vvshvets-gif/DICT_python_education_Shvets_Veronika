import math

MENU = (
    'What do you want to calculate?\n'
    'type "n" for number of monthly payments,\n'
    'type "a" for annuity monthly payment amount,\n'
    'type "p" for loan principal:'
)


def months_to_str(n):
    years, months = divmod(n, 12)
    parts = []
    if years:
        parts.append(f"{years} year{'s' if years > 1 else ''}")
    if months:
        parts.append(f"{months} month{'s' if months > 1 else ''}")
    return " and ".join(parts)


choice = input(f"{MENU}\n> ")

if choice == "n":
    principal = float(input("Enter the loan principal:\n> "))
    payment = float(input("Enter the monthly payment:\n> "))
    interest = float(input("Enter the loan interest:\n> "))

    i = interest / (12 * 100)
    n = math.ceil(math.log(payment / (payment - i * principal), 1 + i))
    print(f"It will take {months_to_str(n)} to repay this loan!")

elif choice == "a":
    principal = float(input("Enter the loan principal:\n> "))
    n = int(input("Enter the number of periods:\n> "))
    interest = float(input("Enter the loan interest:\n> "))

    i = interest / (12 * 100)
    payment = math.ceil(principal * (i * (1 + i) ** n) / ((1 + i) ** n - 1))
    print(f"Your monthly payment = {payment}!")

elif choice == "p":
    payment = float(input("Enter the annuity payment:\n> "))
    n = int(input("Enter the number of periods:\n> "))
    interest = float(input("Enter the loan interest:\n> "))

    i = interest / (12 * 100)
    principal = round(payment / ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))
    print(f"Your loan principal = {principal}!")
