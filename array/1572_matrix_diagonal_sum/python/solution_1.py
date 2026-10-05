class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        """
        Возвращает сумму элементов главной и побочной диагоналей матрицы.
        Центральный элемент (если матрица нечётного размера) учитывается только один раз.
        """
        n = len(mat)
        total_sum = 0

        # Проходим по всем строкам матрицы
        for i in range(n):
            # 1. Всегда добавляем элемент главной диагонали
            total_sum += mat[i][i]

            # 2. Проверяем, не является ли текущий элемент центральным.
            # Элемент побочной диагонали находится в столбце (n - 1 - i).
            # Если i == n - 1 - i, значит мы в центре матрицы,
            # и этот элемент мы уже добавили на шаге 1.
            if i != n - 1 - i:
                total_sum += mat[i][n - 1 - i]

        return total_sum


def main():
    """Тест-кейсы для задачи Matrix Diagonal Sum."""
    solution = Solution()

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ЗАДАЧИ MATRIX DIAGONAL SUM")
    print("=" * 60)

    # Тест 1: Стандартный случай из примера LeetCode (нечётный размер 3x3)
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = solution.diagonalSum(mat)
    expected = 25  # 1 + 5 + 9 (главная) + 3 + 7 (побочная, без 5) = 25
    print(f"\nТест 1: Матрица 3x3 (нечётный размер)")
    print(f"Результат: {result}")
    assert result == expected, (
        f"Тест 1 провален! Ожидалось {expected}, получено {result}"
    )
    print("✓ Пройден")

    # Тест 2: Чётный размер 4x4 (центрального элемента нет)
    mat = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
    result = solution.diagonalSum(mat)
    expected = 8  # 4 элемента главной + 4 элемента побочной = 8
    print(f"\nТест 2: Матрица 4x4 (чётный размер)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 2 провален!"
    print("✓ Пройден")

    # Тест 3: Минимальный размер 1x1
    mat = [[5]]
    result = solution.diagonalSum(mat)
    expected = 5
    print(f"\nТест 3: Матрица 1x1 (минимальный размер)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 3 провален!"
    print("✓ Пройден")

    # Тест 4: Размер 2x2 (чётный, нет центра)
    mat = [[1, 2], [3, 4]]
    result = solution.diagonalSum(mat)
    expected = 10  # 1 + 4 + 2 + 3 = 10
    print(f"\nТест 4: Матрица 2x2")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 4 провален!"
    print("✓ Пройден")

    # Тест 5: Большой нечётный размер 5x5
    mat = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]
    result = solution.diagonalSum(mat)
    # Главная: 1 + 7 + 13 + 19 + 25 = 65
    # Побочная: 5 + 9 + 13 + 17 + 21 = 65
    # Центр (13) вычитаем один раз: 65 + 65 - 13 = 117
    expected = 117
    print(f"\nТест 5: Матрица 5x5 (большой нечётный размер)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 5 провален!"
    print("✓ Пройден")

    print("\n" + "=" * 60)
    print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО! ✓")
    print("=" * 60)


if __name__ == "__main__":
    main()
