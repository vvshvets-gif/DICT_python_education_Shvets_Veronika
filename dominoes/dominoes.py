import random


def make_full_set():
    return [[i, j] for i in range(7) for j in range(i, 7)]


def deal():
    pieces = make_full_set()
    random.shuffle(pieces)
    return pieces[:14], pieces[14:21], pieces[21:]


def find_starting_piece(computer, player):
    for double in range(6, -1, -1):
        if [double, double] in computer:
            computer.remove([double, double])
            return [double, double], "player"
        if [double, double] in player:
            player.remove([double, double])
            return [double, double], "computer"
    return None, None


STATUS_MESSAGES = {
    "player": "It's your turn to make a move. Enter your command.",
    "computer": "Computer is about to make a move. Press Enter to continue...",
}


def display(stock, computer, player, snake, status):
    print("=" * 70)
    print(f"Stock size: {len(stock)}")
    print(f"Computer pieces: {len(computer)}")
    print()
    print(*snake)
    print()
    print("Your pieces:")
    for i, piece in enumerate(player, 1):
        print(f"{i}:{piece}")
    print(f"\nStatus: {STATUS_MESSAGES[status]}")


while True:
    stock, computer, player = deal()
    snake, status = find_starting_piece(computer, player)
    if snake:
        break

display(stock, computer, player, [snake], status)
