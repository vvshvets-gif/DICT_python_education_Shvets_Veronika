"""
Модуль 'Bill Splitter' з функцією 'Щасливчик'.

Цей скрипт дозволяє групі друзів розділити рахунок. Він включає функцію
вибору випадкової людини, яка не платитиме нічого, тоді як сума
розподіляється порівну між іншими.
"""

import random


def get_number_of_friends() -> int:
    """
    Запитує у користувача кількість друзів.

    Returns:
        int: Кількість друзів або 0, якщо введення некоректне.
    """
    try:
        return int(input("Enter the number of friends joining (including you):\n"))
    except ValueError:
        return 0


def get_total_amount() -> float:
    """
    Запитує загальну суму чека.

    Returns:
        float: Сума чека або 0.0, якщо введення некоректне.
    """
    try:
        return float(input("Enter the total amount:\n"))
    except ValueError:
        return 0


def get_friends_dict(num_friends: int) -> dict:
    """
    Створює словник друзів, де ключі — імена, а значення — початковий баланс 0.

    Args:
        num_friends (int): Кількість друзів, яких треба додати.

    Returns:
        dict: Словник формату {'Ім'я': 0.0}.
    """
    friends_dict = {}
    for _ in range(num_friends):
        name = input()
        friends_dict[name] = 0
    return friends_dict


def get_lucky_one(friends_dict: dict) -> str:
    """
    Випадковим чином обирає одного "щасливчика" зі списку друзів.

    Args:
        friends_dict (dict): Словник із іменами друзів.

    Returns:
        str: Ім'я обраного друга.
    """
    return random.choice(list(friends_dict.keys()))


def calculate_bill_with_lucky(lucky_one: str, friends_dict: dict, total_amount: float):
    """
    Перераховує суму для кожного друга, враховуючи, що щасливчик платить 0.

    Args:
        lucky_one (str): Ім'я друга, який не платить.
        friends_dict (dict): Словник, який буде оновлено новими сумами.
        total_amount (float): Загальна сума чека.
    """
    num_friends = len(friends_dict)
    if num_friends > 1:
        new_num_friends = num_friends - 1
        new_split_amount = total_amount / new_num_friends
        new_rounded_amount = round(new_split_amount, 2)

        for name in friends_dict:
            if name == lucky_one:
                friends_dict[name] = 0.00
            else:
                friends_dict[name] = new_rounded_amount
    elif num_friends == 1:
        friends_dict[lucky_one] = round(total_amount, 2)


def start():
    """
    Головна функція для запуску логіки розділення рахунку.

    Координує введення даних, вибір щасливчика, розрахунки та виведення результату.
    """
    num_friends = get_number_of_friends()

    if num_friends <= 0:
        print("No one is joining for the party")
        return

    print("Enter the name of every friend (including you), each on a new line:")
    friends_dict = get_friends_dict(num_friends)
    total_amount = get_total_amount()

    lucky_choice = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n').lower()

    if lucky_choice == 'yes':
        lucky_one = get_lucky_one(friends_dict)
        print(f"{lucky_one} is the lucky one!")
        calculate_bill_with_lucky(lucky_one, friends_dict, total_amount)
    else:
        print("No one is going to be lucky")
        if total_amount > 0 and num_friends > 0:
            split_amount = total_amount / num_friends
            rounded_amount = round(split_amount, 2)
            for name in friends_dict:
                friends_dict[name] = rounded_amount

    print(friends_dict)


if __name__ == "__main__":
    start()