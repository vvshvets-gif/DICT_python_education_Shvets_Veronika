"""
Модуль для запуску гри 'Шибениця' (Hangman).

Цей скрипт ініціалізує ігровий процес, налаштовує обробник введення-виведення
та керує головним меню гри.
"""

from IO import ConsoleIO
from game import Game


def main():
    """
    Головна функція, яка керує життєвим циклом програми.

    Створює екземпляри ConsoleIO та Game, відображає вітальне повідомлення
    та обробляє вибір користувача в меню (грати або вийти).
    """
    console_io = ConsoleIO()

    # Ініціалізація гри з набором слів та кількістю спроб
    game = Game(
        words=['python', 'java', 'javascript', 'php'],
        attempts_left=8,
        io_handler=console_io
    )

    console_io.print_output("--- HANGMAN ---")

    while True:
        menu_choice = console_io.get_input('Type "play" to play the game, "exit" to quit: ').lower()

        if menu_choice == 'play':
            game.start()
        elif menu_choice == 'exit':
            console_io.print_output("Goodbye!")
            break
        else:
            # Якщо введення некоректне, цикл просто повторюється
            continue


if __name__ == "__main__":
    main()