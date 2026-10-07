class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        """
        Возвращает транспонированную матрицу.
        Строки и столбцы меняются местами: matrix[i][j] -> result[j][i]
        """
        # Получаем размеры исходной матрицы
        m = len(matrix)  # количество строк
        n = len(matrix[0])  # количество столбцов

        # Создаём результирующую матрицу размером n × m
        # (меняем строки и столбцы местами)
        # Инициализируем нулями, хотя значения будут перезаписаны
        result = [[0] * m for _ in range(n)]

        # Заполняем транспонированную матрицу
        # Для каждого элемента matrix[i][j] записываем его в result[j][i]
        for i in range(m):
            for j in range(n):
                result[j][i] = matrix[i][j]

        return result


def main():
    """Тест-кейсы для задачи Transpose Matrix."""
    solution = Solution()

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ЗАДАЧИ TRANSPOSE MATRIX")
    print("=" * 60)

    # Тест 1: Квадратная матрица 3x3
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = solution.transpose(matrix)
    expected = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    print(f"\nТест 1: Квадратная матрица 3x3")
    print(f"Исходная: {matrix}")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 1 провален!"
    print("✓ Пройден")

    # Тест 2: Прямоугольная матрица 2x3 (неквадратная)
    matrix = [[1, 2, 3], [4, 5, 6]]
    result = solution.transpose(matrix)
    expected = [[1, 4], [2, 5], [3, 6]]
    print(f"\nТест 2: Прямоугольная матрица 2x3 → 3x2")
    print(f"Исходная: {matrix}")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 2 провален!"
    print("✓ Пройден")

    # Тест 3: Матрица 1x1
    matrix = [[42]]
    result = solution.transpose(matrix)
    expected = [[42]]
    print(f"\nТест 3: Матрица 1x1")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 3 провален!"
    print("✓ Пройден")

    # Тест 4: Матрица 1xN (одна строка)
    matrix = [[1, 2, 3, 4, 5]]
    result = solution.transpose(matrix)
    expected = [[1], [2], [3], [4], [5]]
    print(f"\nТест 4: Матрица 1x5 → 5x1")
    print(f"Исходная: {matrix}")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 4 провален!"
    print("✓ Пройден")

    # Тест 5: Матрица Nx1 (один столбец)
    matrix = [[1], [2], [3]]
    result = solution.transpose(matrix)
    expected = [[1, 2, 3]]
    print(f"\nТест 5: Матрица 3x1 → 1x3")
    print(f"Исходная: {matrix}")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 5 провален!"
    print("✓ Пройден")

    # Тест 6: Матрица с отрицательными числами
    matrix = [[-1, -2], [-3, -4], [-5, -6]]
    result = solution.transpose(matrix)
    expected = [[-1, -3, -5], [-2, -4, -6]]
    print(f"\nТест 6: Матрица с отрицательными числами")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 6 провален!"
    print("✓ Пройден")

    print("\n" + "=" * 60)
    print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО! ✓")
    print("=" * 60)


if __name__ == "__main__":
    main()
