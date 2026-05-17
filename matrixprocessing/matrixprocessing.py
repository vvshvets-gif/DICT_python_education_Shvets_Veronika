"""
Matrix Operations Processor.
Реалізація за стандартом PEP 8. Підтримує базову лінійну алгебру.
"""

class MatrixProcessor:
    """
    Клас-процесор для виконання операцій над матрицями.
    Групує математичну логіку та консольний інтерфейс.
    """

    def __init__(self):
        self._menu = (
            "\n1. Add matrices\n2. Multiply matrix by a constant\n"
            "3. Multiply matrices\n4. Transpose matrix\n"
            "5. Calculate a determinant\n6. Inverse matrix\n0. Exit"
        )

    # --- МАТЕМАТИЧНА ЛОГІКА (Static Methods) ---

    @staticmethod
    def _get_minor(m, i, j):
        """Повертає мінор матриці без i-го рядка та j-го стовпця."""
        return [row[:j] + row[j+1:] for row in (m[:i] + m[i+1:])]

    @staticmethod
    def add_matrices(a, b):
        """Додає дві матриці однакового розміру."""
        if len(a) != len(b) or len(a[0]) != len(b[0]):
            return None
        return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

    @staticmethod
    def multiply_by_constant(matrix, constant):
        """Множить матрицю на скаляр."""
        return [[cell * constant for cell in row] for row in matrix]

    @staticmethod
    def multiply_matrices(a, b):
        """Виконує матричне множення $C = A \times B$."""
        if len(a[0]) != len(b):
            return None
        result = [[0.0 for _ in range(len(b[0]))] for _ in range(len(a))]
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    result[i][j] += a[i][k] * b[k][j]
        return result

    @staticmethod
    def transpose(m, mode='1'):
        """
        Транспонує матрицю за 4 режимами:
        1: Головна, 2: Побічна, 3: Вертикальна, 4: Горизонтальна.
        """
        if mode == '1':
            return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
        elif mode == '2':
            n, cols = len(m), len(m[0])
            return [[m[n - 1 - j][cols - 1 - i] for j in range(n)] for i in range(cols)]
        elif mode == '3':
            return [row[::-1] for row in m]
        elif mode == '4':
            return m[::-1]
        return m

    def determinant(self, m):
        """Обчислює визначник через розклад Лапласа."""
        n = len(m)
        if n == 1: return m[0][0]
        if n == 2: return m[0][0] * m[1][1] - m[0][1] * m[1][0]

        det = 0
        for j in range(n):
            det += ((-1) ** j) * m[0][j] * self.determinant(self._get_minor(m, 0, j))
        return det

    def inverse(self, m):
        """Обчислює зворотну матрицю через приєднану матрицю."""
        n = len(m)
        if n != len(m[0]): return None

        det = self.determinant(m)
        if abs(det) < 1e-12: return None
        if n == 1: return [[1 / m[0][0]]]

        cofactors = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(((-1) ** (i + j)) * self.determinant(self._get_minor(m, i, j)))
            cofactors.append(row)

        adjugate = self.transpose(cofactors, mode='1')
        return self.multiply_by_constant(adjugate, 1 / det)

    # --- UI МЕТОДИ ---

    def _read_matrix(self, label="matrix"):
        """Зчитує дані матриці. Повертає None при некоректному вводі."""
        try:
            prompt = input(f"Enter size of {label}: > ").split()
            if not prompt: return None
            r, c = map(int, prompt)
            print(f"Enter {label}:")
            return [[float(x) for x in input("> ").split()] for _ in range(r)]
        except (ValueError, IndexError):
            return None

    def _print(self, m):
        """Виводить матрицю з округленням до 2 знаків для дробів."""
        print("The result is:")
        for row in m:
            print(*(f"{x:g}" if x == int(x) else f"{round(x, 2):g}" for x in row))

    def run(self):
        """Головний цикл взаємодії з користувачем."""
        while True:
            print(self._menu)
            choice = input("Your choice: > ")
            if choice == '0': break

            if choice in ('1', '3'):
                m1, m2 = self._read_matrix("first"), self._read_matrix("second")
                if m1 and m2:
                    res = self.add_matrices(m1, m2) if choice == '1' else self.multiply_matrices(m1, m2)
                    self._print(res) if res else print("The operation cannot be performed.")
                else: print("Invalid input.")

            elif choice == '2':
                m = self._read_matrix()
                if m:
                    c = float(input("Enter constant: > "))
                    self._print(self.multiply_by_constant(m, c))

            elif choice == '4':
                print("\n1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
                mode = input("Your choice: > ")
                m = self._read_matrix()
                if m: self._print(self.transpose(m, mode))

            elif choice == '5':
                m = self._read_matrix()
                if m and len(m) == len(m[0]):
                    print(f"The result is:\n{self.determinant(m)}")
                else: print("Error: Matrix must be square.")

            elif choice == '6':
                m = self._read_matrix()
                if m:
                    res = self.inverse(m)
                    self._print(res) if res else print("This matrix doesn't have an inverse.")

if __name__ == "__main__":
    MatrixProcessor().run()