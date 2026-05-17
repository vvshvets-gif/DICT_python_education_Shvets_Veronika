"""
Модуль гри 'Хрестики-нулики' (Tic-Tac-Toe).

Цей скрипт реалізує повний цикл гри для двох гравців на одному пристрої.
Включає візуалізацію поля 3x3, перевірку на виграш/нічию та валідацію 
координат введення.
"""


def display_grid(cells: str):
    """
    Виводить ігрове поле 3x3 у консоль.

    Args:
        cells (str): Рядок з 9 символів ('X', 'O' або '_'), 
                     що представляє поточний стан поля.
    """
    print("---------")
    # Замінюємо '_' на пробіл для кращого візуального сприйняття
    display_cells = cells.replace('_', ' ')
    print(f"| {display_cells[0]} {display_cells[1]} {display_cells[2]} |")
    print(f"| {display_cells[3]} {display_cells[4]} {display_cells[5]} |")
    print(f"| {display_cells[6]} {display_cells[7]} {display_cells[8]} |")
    print("---------")


def check_win(cells: str, player: str) -> bool:
    """
    Перевіряє, чи зібрав вказаний гравець переможну комбінацію.

    Args:
        cells (str): Поточний стан поля.
        player (str): Символ гравця ('X' або 'O').

    Returns:
        bool: True, якщо гравець виграв, інакше False.
    """
    win_coords = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Горизонталі
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Вертикалі
        (0, 4, 8), (2, 4, 6)  # Діагоналі
    ]
    for combo in win_coords:
        if all(cells[i] == player for i in combo):
            return True
    return False


def analyze_state(cells: str) -> str:
    """
    Аналізує поточний стан гри та визначає результат.

    Args:
        cells (str): Поточний стан поля.

    Returns:
        str: Один зі станів: "X wins", "O wins", "Draw" або "Game not finished".
    """
    x_wins = check_win(cells, 'X')
    o_wins = check_win(cells, 'O')

    if x_wins:
        return "X wins"
    if o_wins:
        return "O wins"
    if '_' not in cells:
        return "Draw"

    return "Game not finished"


def get_valid_move(cells: str) -> int:
    """
    Запитує у користувача координати ходу та перевіряє їх на валідність.

    Функція перевіряє:
    1. Чи є введені дані числами.
    2. Чи знаходяться вони в межах 1-3.
    3. Чи не зайнята обрана клітинка.

    Args:
        cells (str): Поточний стан поля для перевірки зайнятості клітинок.

    Returns:
        int: Індекс у рядку (0-8), що відповідає обраним координатам.
    """
    while True:
        coordinates_str = input("Enter the coordinates: ")
        coords = coordinates_str.split()

        # Перевірка на наявність чисел
        if len(coords) != 2 or not all(c.isdigit() for c in coords):
            print("You should enter numbers!")
            continue

        # Координати: x (стовпчик), y (рядок)
        x, y = int(coords[0]), int(coords[1])

        # Перевірка діапазону
        if not (1 <= x <= 3 and 1 <= y <= 3):
            print("Coordinates should be from 1 to 3!")
            continue

        # Формула перетворення (col, row) -> index:
        # У вашій логіці (1,1) це верхній лівий кут (індекс 0)
        index = (y - 1) * 3 + (x - 1)

        # Перевірка на зайнятість
        if cells[index] != '_':
            print("This cell is occupied! Choose another one!")
            continue

        return index


def main():
    """
    Головна функція, що запускає ігровий цикл.
    """
    current_cells = '_________'
    current_player = 'X'

    display_grid(current_cells)

    while True:
        # Отримуємо хід
        move_index = get_valid_move(current_cells)

        # Оновлюємо поле
        cells_list = list(current_cells)
        cells_list[move_index] = current_player
        current_cells = "".join(cells_list)

        display_grid(current_cells)

        # Аналіз стану
        game_state = analyze_state(current_cells)

        if game_state in ["X wins", "O wins", "Draw"]:
            print(game_state)
            break

        # Зміна гравця
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    main()