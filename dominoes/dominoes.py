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
    "player_won": "The game is over. You won!",
    "computer_won": "The game is over. The computer won!",
    "draw": "The game is over. It's a draw!",
}

NEXT_TURN = {"player": "computer", "computer": "player"}


def format_snake(snake):
    pieces = [str(p) for p in snake]
    if len(pieces) <= 6:
        return "".join(pieces)
    return "".join(pieces[:3]) + "..." + "".join(pieces[-3:])


def display(stock, computer, player, snake, status):
    print("=" * 70)
    print(f"Stock size: {len(stock)}")
    print(f"Computer pieces: {len(computer)}")
    print(format_snake(snake))
    print("Your pieces:")
    for i, piece in enumerate(player, 1):
        print(f"{i}:{piece}")
    print(f"Status: {STATUS_MESSAGES[status]}")


def check_end(player, computer, snake):
    if not player:
        return "player_won"
    if not computer:
        return "computer_won"
    left, right = snake[0][0], snake[-1][1]
    if left == right and sum(p.count(left) for p in snake) >= 8:
        return "draw"
    return None


def is_valid_move(move, pieces, snake):
    if move == 0:
        return True
    piece = pieces[abs(move) - 1]
    if move > 0:
        return snake[-1][1] in piece
    else:
        return snake[0][0] in piece


def apply_move(move, pieces, snake, stock):
    if move == 0:
        if stock:
            pieces.append(stock.pop())
        return
    piece = pieces.pop(abs(move) - 1)
    if move > 0:
        if piece[0] != snake[-1][1]:
            piece = piece[::-1]
        snake.append(piece)
    else:
        if piece[1] != snake[0][0]:
            piece = piece[::-1]
        snake.insert(0, piece)


while True:
    stock, computer, player = deal()
    snake, status = find_starting_piece(computer, player)
    if snake:
        break

snake = [snake]

while True:
    end = check_end(player, computer, snake)
    if end:
        display(stock, computer, player, snake, end)
        break

    display(stock, computer, player, snake, status)

    if status == "player":
        while True:
            try:
                move = int(input("> "))
                if abs(move) > len(player):
                    raise ValueError
                if not is_valid_move(move, player, snake):
                    print("Illegal move. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please try again.")
        apply_move(move, player, snake, stock)
    else:
        input("> ")
        while True:
            move = random.randint(-len(computer), len(computer))
            if is_valid_move(move, computer, snake):
                break
        apply_move(move, computer, snake, stock)

    status = NEXT_TURN[status]
