import random


def make_full_set():
    return [[i, j] for i in range(7) for j in range(i, 7)]


def deal():
    pieces = make_full_set()
    random.shuffle(pieces)
    stock = pieces[:14]
    computer = pieces[14:21]
    player = pieces[21:]
    return stock, computer, player


def find_starting_piece(computer, player):
    for double in range(6, -1, -1):
        if [double, double] in computer:
            computer.remove([double, double])
            return [double, double], "player"
        if [double, double] in player:
            player.remove([double, double])
            return [double, double], "computer"
    return None, None


while True:
    stock, computer, player = deal()
    snake, status = find_starting_piece(computer, player)
    if snake:
        break

print(f"Stock pieces: {stock}")
print(f"Computer pieces: {computer}")
print(f"Player pieces: {player}")
print(f"Domino snake: [{snake}]")
print(f"Status: {status}")
