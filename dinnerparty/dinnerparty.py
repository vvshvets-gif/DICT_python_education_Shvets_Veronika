# Етап 4: Фінальна версія з перерахунком
import random

def get_number_of_friends() -> int:
    try:
        return int(input("Enter the number of friends joining (including you):\n"))
    except ValueError:
        return 0

def get_total_amount() -> float:
    try:
        return float(input("Enter the total amount:\n"))
    except ValueError:
        return 0

def get_friends_dict(num_friends: int):
    friends_dict = {}
    for _ in range(num_friends):
        name = input()
        friends_dict[name] = 0

    return friends_dict

def get_lucky_one(friends_dict):
    return random.choice(list(friends_dict.keys()))

def calculate_bill_with_lucky(lucky_one, friends_dict, total_amount):
    num_friends = len(friends_dict)
    if num_friends > 1:
        new_num_friends = num_friends - 1
        new_split_amount = total_amount / new_num_friends

        # 6. Округлення
        new_rounded_amount = round(new_split_amount, 2)

        # 7. Оновлення словника
        for name in friends_dict:
            if name == lucky_one:
                friends_dict[name] = 0.00  # Щасливчик платить 0
            else:
                friends_dict[name] = new_rounded_amount
    elif num_friends == 1:
        # Якщо тільки 1 людина, вона платить все, і не може бути "щасливчиком" у сенсі поділу
        friends_dict[lucky_one] = round(total_amount, 2)

def start():
    # 1. Запитуємо кількість людей
    num_friends = get_number_of_friends()

    # 1.1 Виходимо з програми, якщо число меьше 1
    if num_friends <= 0:
        print("No one is joining for the party")
        return

    # 2. Зчитуємо імена друзів
    print("Enter the name of every friend (including you), each on a new line:")
    friends_dict = get_friends_dict(num_friends)

    # 3. Зчитуємо загальну суму
    total_amount = get_total_amount()

    # 4. Запитуємо, чи потрібен "щасливчик"
    lucky_choice = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n').lower()

    if lucky_choice == 'yes':
        # 4.1 Випадковий вибір імені
        lucky_one = get_lucky_one(friends_dict)
        print(f"{lucky_one} is the lucky one!")

        # --- ЛОГІКА ПЕРЕРАХУНКУ ЕТАПУ 4 ---

        # 5. Перерахунок на n - 1 людей
        calculate_bill_with_lucky(lucky_one, friends_dict, total_amount)
    else:
        # Якщо користувач не вибрав "щасливчика" (No або інше)
        print("No one is going to be lucky")

        # 8. Якщо "щасливчика" немає, використовуємо рівний поділ (Етап 2)
        if total_amount > 0 and num_friends > 0:
            split_amount = total_amount / num_friends
            rounded_amount = round(split_amount, 2)
            for name in friends_dict:
                friends_dict[name] = rounded_amount

    # 9. Виведення фінального словника
    print(friends_dict)

start()