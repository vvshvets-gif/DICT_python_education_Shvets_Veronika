import random
import string

from typing import List
from IO import IO

class Game:
    def __init__(self, words: List[str], attempts_left: int, io_handler: IO):
        self._words = words
        self._attempts_left = attempts_left
        self._io_handler = io_handler

    def start(self):
        """Логіка гри 'Шибениця'."""
        words = self._words
        attempts_left = self._attempts_left

        secret_word = random.choice(words)

        current_hint = '-' * len(secret_word)
        guessed_letters = set()

        self._io_handler.print_output(current_hint)

        # Головний цикл гри
        while attempts_left > 0 and current_hint != secret_word:
            letter = self._io_handler.get_input("Input a letter: ").lower()

            # --- 1. ВАЛІДАЦІЯ ВВОДУ ---

            if len(letter) != 1:
                self._io_handler.print_output("You should input a single letter")
                continue

            if letter not in string.ascii_lowercase:
                self._io_handler.print_output("Please enter a lowercase English letter")
                continue

            # --- 2. ЛОГІКА ГРИ ---

            # Якщо літера вже була вгадана
            if letter in guessed_letters:
                self._io_handler.print_output("You've already guessed this letter")
                continue  # Не зменшуємо спроби

            # Додаємо літеру до списку вгаданих
            guessed_letters.add(letter)

            # Якщо літера правильна
            if letter in secret_word:
                # Оновлення підказки
                new_hint = list(current_hint)
                for i, char in enumerate(secret_word):
                    if char == letter:
                        new_hint[i] = letter
                current_hint = "".join(new_hint)

            # Якщо літера неправильна
            else:
                self._io_handler.print_output("That letter doesn't appear in the word")
                attempts_left -= 1  # Зменшення життя

            self._io_handler.print_output(current_hint)

        # Фінальний результат
        if current_hint == secret_word:
            self._io_handler.print_output(f"You guessed the word {secret_word}!")
            self._io_handler.print_output("You survived!")
        else:
            self._io_handler.print_output("You lost!")