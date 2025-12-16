# Етап 5: Фінальний варіант гри

def display_grid(cells):
    """Виводить ігрове поле 3x3 на основі рядка з 9 символів."""
    print("---------")
    # Замінюємо '_' на пробіл для виведення
    cells = cells.replace('_', ' ')
    print(f"| {cells[0]} {cells[1]} {cells[2]} |")
    print(f"| {cells[3]} {cells[4]} {cells[5]} |")
    print(f"| {cells[6]} {cells[7]} {cells[8]} |")
    print("---------")

def check_win(cells, player):
    """Перевіряє, чи виграв гравець (X або O)."""
    win_coords = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Горизонталі
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Вертикалі
        (0, 4, 8), (2, 4, 6)             # Діагоналі
    ]
    for combo in win_coords:
        if all(cells[i] == player for i in combo):
            return True
    return False

def analyze_state(cells):
    """Аналізує ігровий стан і повертає результат."""

    x_wins = check_win(cells, 'X')
    o_wins = check_win(cells, 'O')

    # Перевірка на перемогу
    if x_wins:
        return "X wins"
    if o_wins:
        return "O wins"

    # Перевірка на Game not finished
    if '_' in cells:
        return "Game not finished"

    # Нічия
    return "Draw"

def get_valid_move(cells, current_player):
    """Просить користувача зробити хід, перевіряє коректність і повертає індекс."""

    while True:
        coordinates_str = input("Enter the coordinates: ")
        coords = coordinates_str.split()

        # 1. Перевірка: You should enter numbers!
        if len(coords) != 2 or not all(c.isdigit() for c in coords):
            print("You should enter numbers!")
            continue

        x, y = int(coords[0]), int(coords[1])

        # 2. Перевірка: Coordinates should be from 1 to 3!
        if not (1 <= x <= 3 and 1 <= y <= 3):
            print("Coordinates should be from 1 to 3!")
            continue

        # Перетворення координат (col, row) на 1D індекс
        # Формула: (row-1) * 3 + (col-1)
        index = (y - 1) * 3 + (x - 1)

        # 3. Перевірка: This cell is occupied! Choose another one!
        if cells[index] != '_':
            print("This cell is occupied! Choose another one!")
            continue

        # Якщо всі перевірки пройдені, повертаємо індекс
        return index

# --- ГОЛОВНА ЛОГІКА ГРИ ---

# Починаємо з порожнього поля (9 символів '_')
current_cells = '_________'
current_player = 'X' # X ходить першим

display_grid(current_cells)

while True:
    # 1. Отримуємо валідний хід від поточного гравця
    move_index = get_valid_move(current_cells, current_player)

    # 2. Оновлюємо поле
    cells_list = list(current_cells)
    cells_list[move_index] = current_player
    current_cells = "".join(cells_list)

    # 3. Виводимо оновлене поле
    display_grid(current_cells)

    # 4. Перевіряємо стан гри
    game_state = analyze_state(current_cells)

    # 5. Перевірка на завершення гри
    if game_state == "X wins" or game_state == "O wins" or game_state == "Draw":
        print(game_state)
        break

    # 6. Зміна гравця
    current_player = 'O' if current_player == 'X' else 'X'