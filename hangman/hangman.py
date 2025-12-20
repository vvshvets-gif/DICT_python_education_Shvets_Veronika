# Етап 8 - ФІНАЛЬНА ВЕРСІЯ
from IO import ConsoleIO
from game import Game

console_io = ConsoleIO()
game = Game(words=['python', 'java', 'javascript', 'php'], attempts_left=8, io_handler=console_io)

console_io.print_output("HANGMAN")

while True:
    menu_choice = console_io.get_input('Type "play" to play the game, "exit" to quit: ').lower()

    if menu_choice == 'play':
        game.start()
    elif menu_choice == 'exit':
        break
    else:
        continue