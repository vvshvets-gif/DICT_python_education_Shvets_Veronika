"""
Модуль гри 'Олівці' (Pencils Game) з реалізацією ігрового інтелекту (бота).

Гра проводиться за правилами Misere Play: той, хто забирає останній олівець, програє.
Бот використовує стратегію, базуючись на теорії ігор, щоб залишити суперника 
в програшній позиції (кількість олівців $4k + 1$).
"""

import random

PLAYER_1 = "John"  # Людина
BOT_NAME = "Jack"  # Бот
PLAYERS = (PLAYER_1, BOT_NAME)


# --- ДОПОМІЖНІ ФУНКЦІЇ ДЛЯ ІНІЦІАЛІЗАЦІЇ ---

def get_initial_pencils() -> int:
    """
    Запитує у користувача початкову кількість олівців та валідує її.

    Повертає:
        int: Позитивне ціле число олівців.
    """
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


def get_first_player(players: tuple) -> str:
    """
    Визначає, хто з гравців буде ходити першим.

    Аргументи:
        players (tuple): Кортеж з іменами доступних гравців.

    Повертає:
        str: Ім'я обраного гравця.
    """
    while True:
        print(f"Who will be the first ({players[0]}, {players[1]}):")
        player_name = input()
        if player_name in players:
            return player_name
        print(f"Choose between '{players[0]}' and '{players[1]}'")


# --- ФУНКЦІЇ ХОДІВ ---

def get_human_move(pencils_count: int) -> int:
    """
    Обробляє та валідує хід гравця-людини.

    Аргументи:
        pencils_count (int): Поточна кількість олівців на столі.

    Повертає:
        int: Кількість олівців, які забирає людина (1, 2 або 3).
    """
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


def get_bot_move(pencils_count: int) -> int:
    """
    Розраховує хід бота згідно з виграшною стратегією.

    Стратегія полягає в тому, щоб залишити супернику кількість олівців $N$, 
    де $N \equiv 1 \pmod 4$. Це гарантує боту перемогу, якщо він діє без помилок.

    Аргументи:
        pencils_count (int): Поточна кількість олівців на столі.

    Повертає:
        int: Оптимальна кількість олівців (1, 2 або 3).
    """
    # 1. Програшна позиція для бота (N % 4 == 1)
    if pencils_count % 4 == 1:
        if pencils_count == 1:
            move = 1
        else:
            # Якщо бот у програшній позиції, він робить випадковий хід
            move = random.randint(1, 3)

    # 2. Виграшна позиція (N % 4 == 0, 2, 3)
    else:
        if pencils_count % 4 == 0:
            move = 3
        elif pencils_count % 4 == 3:
            move = 2
        elif pencils_count % 4 == 2:
            move = 1
        else:
            move = 1

    # Захист від забирання більшої кількості, ніж залишилось
    move = min(move, pencils_count)
    print(move)
    return move


def main():
    """
    Головний цикл гри, що керує послідовністю ходів та визначає переможця.
    """
    pencils_count = get_initial_pencils()
    current_player = get_first_player(PLAYERS)

    # Визначаємо, хто опонент для кожного гравця
    # (next_player - це той, хто виграє, якщо current_player забере останній олівець)
    players_list = list(PLAYERS)

    while pencils_count > 0:
        print("|" * pencils_count)
        print(f"{current_player}'s turn:")

        if current_player == BOT_NAME:
            take_count = get_bot_move(pencils_count)
        else:
            take_count = get_human_move(pencils_count)

        pencils_count -= take_count

        # Отримуємо ім'я іншого гравця
        other_player = PLAYERS[1] if current_player == PLAYERS[0] else PLAYERS[0]

        if pencils_count == 0:
            print(f"{other_player} won!")
            break

        current_player = other_player


if __name__ == "__main__":
    main()