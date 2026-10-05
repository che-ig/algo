class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        """
        Проверяет, можно ли посадить n новых цветов в клумбу
        без нарушения правила "никаких соседних цветов".
        Использует жадный алгоритм: сажаем цветок везде, где это возможно.
        """
        # Оптимизация: если n = 0, цветы сажать не нужно — ответ всегда True
        if n == 0:
            return True

        # Проходим по всей клумбе
        for i in range(len(flowerbed)):
            # Если текущая грядка пуста
            if flowerbed[i] == 0:
                # Проверяем левого соседа:
                # либо мы на левом краю (i == 0), либо сосед пуст
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)

                # Проверяем правого соседа:
                # либо мы на правом краю (i == len - 1), либо сосед пуст
                right_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                # Если оба соседа пусты — сажаем цветок
                if left_empty and right_empty:
                    flowerbed[i] = 1  # Помечаем грядку как занятую
                    n -= 1  # Уменьшаем счётчик нужных цветов

                    # Ранний выход: если посадили все нужные цветы
                    if n == 0:
                        return True

        # Если прошли всю клумбу и не посадили все цветы
        return n == 0


def main():
    """Тест-кейсы для задачи Can Place Flowers."""
    solution = Solution()

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ЗАДАЧИ CAN PLACE FLOWERS")
    print("=" * 60)

    # Тест 1: Стандартный случай из примера LeetCode
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    result = solution.canPlaceFlowers(flowerbed, n)
    expected = True
    print(f"\nТест 1: flowerbed = {flowerbed}, n = {n}")
    print(f"Результат: {result} (можно посадить в центр)")
    assert result == expected, f"Тест 1 провален!"
    print("✓ Пройден")

    # Тест 2: Нельзя посадить 2 цветка
    flowerbed = [1, 0, 0, 0, 1]
    n = 2
    result = solution.canPlaceFlowers(flowerbed, n)
    expected = False
    print(f"\nТест 2: flowerbed = {flowerbed}, n = {n}")
    print(f"Результат: {result} (можно посадить только 1)")
    assert result == expected, f"Тест 2 провален!"
    print("✓ Пройден")

    # Тест 3: n = 0 (не нужно сажать)
    flowerbed = [1, 0, 0, 0, 1]
    n = 0
    result = solution.canPlaceFlowers(flowerbed, n)
    expected = True
    print(f"\nТест 3: flowerbed = {flowerbed}, n = {n} (нужно 0 цветов)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 3 провален!"
    print("✓ Пройден")

    # Тест 4: Пустая клумба (один элемент)
    flowerbed = [0]
    n = 1
    result = solution.canPlaceFlowers(flowerbed, n)
    expected = True
    print(f"\nТест 4: flowerbed = {flowerbed}, n = {n} (одна грядка)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 4 провален!"
    print("✓ Пройден")

    # Тест 5: Две пустые грядки подряд
    flowerbed = [0, 0]
    n = 1
    result = solution.canPlaceFlowers(flowerbed, n)
    expected = True
    print(f"\nТест 5: flowerbed = {flowerbed}, n = {n}")
    print(f"Результат: {result} (можно посадить на любую)")
    assert result == expected, f"Тест 5 провален!"
    print("✓ Пройден")

    # Тест 6: Две пустые грядки, нужно 2 цветка
    flowerbed = [0, 0]
    n = 2
    result = solution.canPlaceFlowers(flowerbed, n)
    expected = False
    print(f"\nТест 6: flowerbed = {flowerbed}, n = {n}")
    print(f"Результат: {result} (можно посадить только 1)")
    assert result == expected, f"Тест 6 провален!"
    print("✓ Пройден")

    # Тест 7: Все грядки пусты
    flowerbed = [0, 0, 0, 0, 0]
    n = 3
    result = solution.canPlaceFlowers(flowerbed, n)
    expected = True
    print(f"\nТест 7: flowerbed = {flowerbed}, n = {n}")
    print(f"Результат: {result} (посадим на 0, 2, 4)")
    assert result == expected, f"Тест 7 провален!"
    print("✓ Пройден")

    # Тест 8: Все грядки заняты
    flowerbed = [1, 0, 1, 0, 1]
    n = 1
    result = solution.canPlaceFlowers(flowerbed, n)
    expected = False
    print(f"\nТест 8: flowerbed = {flowerbed}, n = {n} (нет места)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 8 провален!"
    print("✓ Пройден")

    # Тест 9: Посадка на краю клумбы
    flowerbed = [0, 0, 1]
    n = 1
    result = solution.canPlaceFlowers(flowerbed, n)
    expected = True
    print(f"\nТест 9: flowerbed = {flowerbed}, n = {n} (посадка на левом краю)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 9 провален!"
    print("✓ Пройден")

    # Тест 10: Посадка на правом краю
    flowerbed = [1, 0, 0]
    n = 1
    result = solution.canPlaceFlowers(flowerbed, n)
    expected = True
    print(f"\nТест 10: flowerbed = {flowerbed}, n = {n} (посадка на правом краю)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 10 провален!"
    print("✓ Пройден")

    print("\n" + "=" * 60)
    print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО! ✓")
    print("=" * 60)


if __name__ == "__main__":
    main()
