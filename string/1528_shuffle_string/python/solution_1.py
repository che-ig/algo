class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        """
        Перемешивает строку s согласно массиву indices.
        Символ s[i] перемещается на позицию indices[i] в результате.

        :param s: исходная строка
        :param indices: массив индексов той же длины, что и s
        :return: перемешанная строка
        """
        n = len(s)

        # Создаём список-результат нужной длины.
        # Инициализируем пустыми строками (или любыми плейсхолдерами) —
        # все позиции будут перезаписаны, так как indices содержит
        # все числа от 0 до n-1 ровно по одному разу.
        result = [""] * n

        # Проходим по всем символам исходной строки
        for i in range(n):
            # Помещаем символ s[i] на позицию indices[i] в результате.
            # Это прямое применение правила из условия задачи.
            result[indices[i]] = s[i]

        # Соединяем список символов в одну строку.
        # ''.join(list) — стандартный и эффективный способ конкатенации
        # строк в Python (работает за O(n), в отличие от многократного +).
        return "".join(result)


def main():
    """Тест-кейсы для задачи Shuffle String."""
    solution = Solution()

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ЗАДАЧИ SHUFFLE STRING")
    print("=" * 60)

    # Тест 1: Стандартный случай из примера LeetCode
    s = "codeleet"
    indices = [4, 5, 6, 7, 0, 2, 1, 3]
    result = solution.restoreString(s, indices)
    expected = "leetcode"
    print(f"\nТест 1: s = '{s}', indices = {indices}")
    print(f"Результат: '{result}'")
    assert result == expected, (
        f"Тест 1 провален! Ожидалось '{expected}', получено '{result}'"
    )
    print("✓ Пройден")

    # Тест 2: Индексы не меняют порядок (тождественная перестановка)
    s = "abc"
    indices = [0, 1, 2]
    result = solution.restoreString(s, indices)
    expected = "abc"
    print(f"\nТест 2: s = '{s}', indices = {indices} (порядок не меняется)")
    print(f"Результат: '{result}'")
    assert result == expected, f"Тест 2 провален!"
    print("✓ Пройден")

    # Тест 3: Обратный порядок
    s = "abc"
    indices = [2, 1, 0]
    result = solution.restoreString(s, indices)
    expected = "cba"
    print(f"\nТест 3: s = '{s}', indices = {indices} (обратный порядок)")
    print(f"Результат: '{result}'")
    assert result == expected, f"Тест 3 провален!"
    print("✓ Пройден")

    # Тест 4: Один символ
    s = "z"
    indices = [0]
    result = solution.restoreString(s, indices)
    expected = "z"
    print(f"\nТест 4: s = '{s}', indices = {indices} (один символ)")
    print(f"Результат: '{result}'")
    assert result == expected, f"Тест 4 провален!"
    print("✓ Пройден")

    # Тест 5: Циклический сдвиг
    s = "abcd"
    indices = [1, 2, 3, 0]
    result = solution.restoreString(s, indices)
    expected = "dabc"
    print(f"\nТест 5: s = '{s}', indices = {indices} (циклический сдвиг)")
    print(f"Результат: '{result}'")
    assert result == expected, f"Тест 5 провален!"
    print("✓ Пройден")

    # Тест 6: Все одинаковые символы
    s = "aaaa"
    indices = [3, 2, 1, 0]
    result = solution.restoreString(s, indices)
    expected = "aaaa"
    print(f"\nТест 6: s = '{s}', indices = {indices} (все одинаковые)")
    print(f"Результат: '{result}'")
    assert result == expected, f"Тест 6 провален!"
    print("✓ Пройден")

    print("\n" + "=" * 60)
    print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО! ✓")
    print("=" * 60)


if __name__ == "__main__":
    main()
