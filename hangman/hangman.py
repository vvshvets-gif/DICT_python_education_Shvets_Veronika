# Етап 8 - ФІНАЛЬНА ВЕРСІЯ
import random
import string

def play_game():
    """Логіка гри 'Шибениця'."""
    words = ['python', 'java', 'javascript', 'php']
    secret_word = random.choice(words)

    attempts_left = 8
    current_hint = '-' * len(secret_word)
    guessed_letters = set()

    print(current_hint)

    # Головний цикл гри
    while attempts_left > 0 and current_hint != secret_word:
        letter = input("Input a letter: ").lower()

        # --- 1. ВАЛІДАЦІЯ ВВОДУ ---

        if len(letter) != 1:
            print("You should input a single letter")
            continue

        if letter not in string.ascii_lowercase:
            print("Please enter a lowercase English letter")
            continue

        # --- 2. ЛОГІКА ГРИ ---

        # Якщо літера вже була вгадана
        if letter in guessed_letters:
            print("You've already guessed this letter")
            continue # Не зменшуємо спроби

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
            print("That letter doesn't appear in the word")
            attempts_left -= 1 # Зменшення життя

        print(current_hint)

    # Фінальний результат
    if current_hint == secret_word:
        print(f"You guessed the word {secret_word}!")
        print("You survived!")
    else:
        print("You lost!")


# --- ГОЛОВНЕ МЕНЮ ПРОГРАМИ ---

print("HANGMAN")

while True:
    menu_choice = input('Type "play" to play the game, "exit" to quit: ').lower()

    if menu_choice == 'play':
        play_game()
    elif menu_choice == 'exit':
        break
    else:
        continue