# --- ЕТАП 6: ЗВОРОТНА МАТРИЦЯ ---

def matrix_of_cofactors(matrix):
    """Обчислює матрицю кофакторів."""
    n = len(matrix)
    cofactors = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # Мінор (cofactor_matrix)
            minor = get_cofactor(matrix, i, j)

            # Визначник мінора
            minor_det = determinant(minor)

            # Обчислення кофактора: C[i][j] = (-1)^(i+j) * det(Minor)
            sign = 1 if (i + j) % 2 == 0 else -1
            cofactors[i][j] = sign * minor_det

    return cofactors


def inverse_matrix(matrix):
    """Знаходить зворотну матрицю."""
    n = len(matrix)

    # 1. Обчислення визначника
    det_val = determinant(matrix)

    if det_val == 0:
        return None  # Зворотна матриця не існує

    # 2. Обчислення матриці кофакторів
    cofactors = matrix_of_cofactors(matrix)

    # 3. Транспонування матриці кофакторів (отримання приєднаної матриці)
    adjugate = transpose_main_diagonal(cofactors)

    # 4. Множення на 1 / det(A)
    inverse = multiply_by_constant(adjugate, 1.0 / det_val)

    return inverse


# Оновлення функції start_matrix_processing для включення зворотної матриці (додаємо option 6)
def handle_inverse():
    print("Enter matrix size:")
    size_input = input("> ").split()

    try:
        rows, cols = int(size_input[0]), int(size_input[1])
        if rows != cols:
            print("The matrix must be square to find the inverse.")
            return

        print("Enter matrix:")
        matrix = []
        for _ in range(rows):
            row_input = input("> ").split()
            matrix.append([float(x) for x in row_input])

    except:
        print("\nInvalid input for matrix.")
        return

    # Перевірка для матриці 1x1
    if rows == 1:
        if matrix[0][0] == 0:
            print("This matrix doesn't have an inverse.")
            return
        else:
            result = [[1.0 / matrix[0][0]]]
            print("The result is:")
            print_matrix(result)
            return

    result = inverse_matrix(matrix)

    if result:
        print("The result is:")
        print_matrix(result)
    else:
        print("This matrix doesn't have an inverse.")


# --- ФІНАЛЬНА ФУНКЦІЯ MAIN LOOP (Оновлена) ---

def start_matrix_processing():
    while True:
        print("\n1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")
        choice = input("Your choice: > ")

        if choice == '0':
            break
        elif choice == '1':
            # ... (Логіка додавання, як у Етапі 3)
            pass
        elif choice == '2':
            # ... (Логіка множення на константу, як у Етапі 3)
            pass
        elif choice == '3':
            # ... (Логіка множення матриць, як у Етапі 3)
            pass
        elif choice == '4':
            handle_transpose()
        elif choice == '5':
            handle_determinant()
        elif choice == '6':
            handle_inverse()
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    start_matrix_processing()