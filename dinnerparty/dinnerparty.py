# Етап 4: Фінальна версія з перерахунком
import random

# 1. Запитуємо кількість людей
try:
    num_friends = int(input("Enter the number of friends joining (including you):\n"))
except ValueError:
    num_friends = 0

friends_dict = {}

if num_friends <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(num_friends):
        name = input()
        friends_dict[name] = 0

    # 2. Зчитуємо загальну суму
    try:
        total_amount = float(input("Enter the total amount:\n"))
    except ValueError:
        total_amount = 0

    # 3. Запитуємо, чи потрібен "щасливчик"
    lucky_choice = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n').lower()

    lucky_one = None

    if lucky_choice == 'yes':
        # 4. Випадковий вибір імені
        lucky_one = random.choice(list(friends_dict.keys()))
        print(f"{lucky_one} is the lucky one!")

        # --- ЛОГІКА ПЕРЕРАХУНКУ ЕТАПУ 4 ---

        # 5. Перерахунок на n - 1 людей
        if num_friends > 1:
            new_num_friends = num_friends - 1
            new_split_amount = total_amount / new_num_friends

            # 6. Округлення
            new_rounded_amount = round(new_split_amount, 2)

            # 7. Оновлення словника
            for name in friends_dict:
                if name == lucky_one:
                    friends_dict[name] = 0.00 # Щасливчик платить 0
                else:
                    friends_dict[name] = new_rounded_amount
        elif num_friends == 1:
             # Якщо тільки 1 людина, вона платить все, і не може бути "щасливчиком" у сенсі поділу
             friends_dict[lucky_one] = round(total_amount, 2)

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