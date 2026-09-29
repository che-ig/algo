class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        """
        Находит все возможные расстановки N ферзей на доске N x N.
        """
        result = []
        # Инициализируем доску точками
        board = [["."] * n for _ in range(n)]

        # Множества для отслеживания занятых столбцов и диагоналей за O(1)
        cols = set()  # Занятые столбцы
        pos_diagonals = set()  # Занятые побочные диагонали (row + col)
        neg_diagonals = set()  # Занятые главные диагонали (row - col)

        def backtrack(row: int) -> None:
            """
            Рекурсивно пытается поставить ферзя в каждую строку.
            """
            # Базовый случай: мы успешно поставили ферзей во все N строк
            if row == n:
                # Преобразуем доску из списка списков в список строк
                copy = ["".join(r) for r in board]
                result.append(copy)
                return

            # Пробуем поставить ферзя в каждый столбец текущей строки
            for col in range(n):
                # Проверяем, не находится ли клетка под боем
                if (
                    col in cols
                    or (row + col) in pos_diagonals
                    or (row - col) in neg_diagonals
                ):
                    continue

                # 1. Выбираем: ставим ферзя и помечаем линии как занятые
                cols.add(col)
                pos_diagonals.add(row + col)
                neg_diagonals.add(row - col)
                board[row][col] = "Q"

                # 2. Исследуем: переходим к следующей строке
                backtrack(row + 1)

                # 3. Отменяем выбор (Backtrack): убираем ферзя и освобождаем линии
                cols.remove(col)
                pos_diagonals.remove(row + col)
                neg_diagonals.remove(row - col)
                board[row][col] = "."

        # Запускаем бэктрекинг с первой строки (row = 0)
        backtrack(0)

        return result


def main():
    """Тест-кейсы для задачи N-Queens."""
    solution = Solution()

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ЗАДАЧИ N-QUEENS")
    print("=" * 60)

    # Тест 1: Базовый случай n = 1
    n = 1
    result = solution.solveNQueens(n)
    expected = [["Q"]]
    print(f"\nТест 1: n = {n}")
    print(f"Результат: {result}")
    assert result == expected, "Тест 1 провален!"
    print("✓ Пройден")

    # Тест 2: Классический случай n = 4
    n = 4
    result = solution.solveNQueens(n)
    expected = [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
    print(f"\nТест 2: n = {n}")
    print(f"Количество решений: {len(result)}")
    # Сортируем для надежного сравнения, так как порядок может отличаться
    assert sorted(result) == sorted(expected), "Тест 2 провален!"
    print("✓ Пройден")

    # Тест 3: Случай n = 8 (классическая шахматная доска)
    n = 8
    result = solution.solveNQueens(n)
    print(f"\nТест 3: n = {n}")
    print(f"Количество решений: {len(result)}")
    # Для 8 ферзей существует ровно 92 различных решения
    assert len(result) == 92, f"Тест 3 провален! Ожидалось 92, получено {len(result)}"
    print("✓ Пройден")

    # Тест 4: Максимальное ограничение LeetCode n = 9
    n = 9
    result = solution.solveNQueens(n)
    print(f"\nТест 4: n = {n} (максимальное ограничение)")
    print(f"Количество решений: {len(result)}")
    # Для 9 ферзей существует 352 решения
    assert len(result) == 352, f"Тест 4 провален! Ожидалось 352, получено {len(result)}"
    print("✓ Пройден")

    print("\n" + "=" * 60)
    print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО! ✓")
    print("=" * 60)


if __name__ == "__main__":
    main()
