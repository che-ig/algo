class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        """
        Заменяет каждый элемент наибольшим элементом справа от него.
        Последний элемент заменяется на -1.
        Использует один проход справа налево с поддержкой текущего максимума.
        """
        n = len(arr)

        # max_right — наибольший элемент, который мы видели справа от текущей позиции.
        # Инициализируем -1, потому что справа от последнего элемента ничего нет.
        max_right = -1

        # Идём справа налево: от последнего элемента к первому.
        # Используем reversed(range(n)) или range(n-1, -1, -1)
        for i in range(n - 1, -1, -1):
            # Запоминаем старое значение элемента — оно нужно для двух вещей:
            # 1. Чтобы обновить max_right (старое значение тоже "справа" для предыдущих)
            # 2. Его мы потеряем, когда перезапишем arr[i]
            old_value = arr[i]

            # Заменяем текущий элемент на максимум справа от него
            arr[i] = max_right

            # Обновляем максимум: если старое значение больше текущего максимума,
            # то для элементов левее именно оно будет максимумом справа
            if old_value > max_right:
                max_right = old_value

        return arr


def main():
    """Тест-кейсы для задачи Replace Elements with Greatest Element on Right Side."""
    solution = Solution()

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ЗАДАЧИ REPLACE ELEMENTS")
    print("=" * 60)

    # Тест 1: Стандартный случай из примера LeetCode
    arr = [17, 18, 5, 4, 6, 1]
    result = solution.replaceElements(arr)
    expected = [18, 6, 6, 6, 1, -1]
    print(f"\nТест 1: arr = {arr}")
    print(f"Результат: {result}")
    assert result == expected, (
        f"Тест 1 провален! Ожидалось {expected}, получено {result}"
    )
    print("✓ Пройден")

    # Тест 2: Один элемент
    arr = [400]
    result = solution.replaceElements(arr)
    expected = [-1]
    print(f"\nТест 2: arr = {arr} (один элемент)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 2 провален!"
    print("✓ Пройден")

    # Тест 3: Возрастающая последовательность
    # Каждый элемент должен замениться на следующий (он больше)
    arr = [1, 2, 3, 4, 5]
    result = solution.replaceElements(arr)
    expected = [2, 3, 4, 5, -1]
    print(f"\nТест 3: arr = {arr} (возрастающая)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 3 провален!"
    print("✓ Пройден")

    # Тест 4: Убывающая последовательность
    # Максимум справа всегда первый элемент после текущего
    arr = [5, 4, 3, 2, 1]
    result = solution.replaceElements(arr)
    expected = [4, 3, 2, 1, -1]
    print(f"\nТест 4: arr = {arr} (убывающая)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 4 провален!"
    print("✓ Пройден")

    # Тест 5: Все элементы одинаковые
    arr = [7, 7, 7, 7]
    result = solution.replaceElements(arr)
    expected = [7, 7, 7, -1]
    print(f"\nТест 5: arr = {arr} (все одинаковые)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 5 провален!"
    print("✓ Пройден")

    # Тест 6: Два элемента
    arr = [10, 20]
    result = solution.replaceElements(arr)
    expected = [20, -1]
    print(f"\nТест 6: arr = {arr} (два элемента)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 6 провален!"
    print("✓ Пройден")

    # Тест 7: Максимум в середине
    arr = [1, 2, 100, 3, 4]
    result = solution.replaceElements(arr)
    expected = [100, 100, 4, 4, -1]
    print(f"\nТест 7: arr = {arr} (максимум в середине)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 7 провален!"
    print("✓ Пройден")

    # Тест 8: Большой массив (проверка производительности)
    arr = list(range(1, 10001))  # [1, 2, 3, ..., 10000]
    result = solution.replaceElements(arr)
    # Для возрастающей последовательности: arr[i] = i+2, последний = -1
    expected = list(range(2, 10001)) + [-1]
    print(f"\nТест 8: arr = [1..10000] (большой массив)")
    print(f"Первые 5 элементов результата: {result[:5]}")
    print(f"Последние 3 элемента результата: {result[-3:]}")
    assert result == expected, f"Тест 8 провален!"
    print("✓ Пройден")

    print("\n" + "=" * 60)
    print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО! ✓")
    print("=" * 60)


if __name__ == "__main__":
    main()
