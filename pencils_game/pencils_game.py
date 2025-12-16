# Етап 4: Впровадження бота
import random

PLAYER_1 = "John" # Людина
BOT_NAME = "Jack"  # Бот
PLAYERS = (PLAYER_1, BOT_NAME)

# --- ДОПОМІЖНІ ФУНКЦІЇ ДЛЯ ІНІЦІАЛІЗАЦІЇ ---

def get_initial_pencils():
    """Отримує валідну початкову кількість олівців."""
    while True:
        print("How many pencils would you like to use:")
        pencils_input = input()
        try:
            pencils_count = int(pencils_input)
            if pencils_count <= 0:
                print("The number of pencils should be positive")
                continue
            return pencils_count
        except ValueError:
            print("The number of pencils should be numeric")

def get_first_player(players):
    """Отримує валідного першого гравця."""
    while True:
        print(f"Who will be the first ({players[0]}, {players[1]}):")
        player_name = input()
        if player_name in players:
            return player_name
        print(f"Choose between '{players[0]}' and '{players[1]}'")

# --- ФУНКЦІЇ ХОДІВ ---

def get_human_move(pencils_count):
    """Отримує валідний хід людини (1, 2 або 3)."""
    while True:
        move_input = input()
        try:
            take_count = int(move_input)
            if take_count not in [1, 2, 3]:
                print("Possible values: '1', '2' or '3'")
                continue
            if take_count > pencils_count:
                print("Too many pencils were taken")
                continue
            return take_count
        except ValueError:
            print("Possible values: '1', '2' or '3'")

def get_bot_move(pencils_count):
    """Розраховує виграшний хід бота або робить випадковий хід."""

    # 1. Програшні позиції (N = 1, 5, 9, 13, ...)
    # N % 4 == 1 (крім N=1, де бот має взяти останній і програти)
    if pencils_count % 4 == 1 and pencils_count > 1:
        # Програшна позиція: беремо випадкову кількість (1, 2 або 3)
        # Всі ходи призводять до виграшної позиції для опонента
        move = random.randint(1, 3)
        # Переконаємось, що не беремо більше, ніж є
        move = min(move, pencils_count)

    # 2. Виграшні позиції (N = 2, 3, 4, 6, 7, 8, ...)
    else:
        # Мета: залишити опоненту N' таке, що N' % 4 == 1.
        # Необхідна кількість олівців для взяття: N - (N' = N % 4 - 1)

        # Якщо N % 4 == 0 (4, 8, 12, ...): залишити 1. Взяти 3.
        if pencils_count % 4 == 0:
            move = 3
        # Якщо N % 4 == 3 (3, 7, 11, ...): залишити 1. Взяти 2.
        elif pencils_count % 4 == 3:
            move = 2
        # Якщо N % 4 == 2 (2, 6, 10, ...): залишити 1. Взяти 1.
        elif pencils_count % 4 == 2:
            move = 1
        # Якщо N == 1: бот бере 1 і програє (це виняток, оскільки це програшна позиція)
        else: # pencils_count % 4 == 1
            move = 1

        # Переконаємось, що не беремо більше, ніж є
        move = min(move, pencils_count)

    print(move)
    return move

# --- ОСНОВНИЙ ЦИКЛ ГРИ ---

# 1. Ініціалізація
pencils_count = get_initial_pencils()
current_player = get_first_player(PLAYERS)
next_player = BOT_NAME if current_player == PLAYER_1 else PLAYER_1

# 2. Основний цикл гри
while pencils_count > 0:
    print("|" * pencils_count)

    print(f"{current_player}'s turn:")

    # 3. Виконання ходу
    if current_player == BOT_NAME:
        take_count = get_bot_move(pencils_count)
    else:
        take_count = get_human_move(pencils_count)

    pencils_count -= take_count

    # 4. Перевірка на завершення гри
    if pencils_count == 0:
        # Переможець - наступний гравець (той, хто не брав останній олівець)
        print(f"{next_player} won!")
        break

    # 5. Зміна гравця
    current_player, next_player = next_player, current_player