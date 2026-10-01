class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Проверяет, содержит ли s2 перестановку s1 как подстроку.
        Использует скользящее окно фиксированного размера с оптимизацией через счётчик совпадений.
        """
        # Если s1 длиннее s2, перестановка невозможна
        if len(s1) > len(s2):
            return False

        # Массивы частот для 26 букв английского алфавита
        s1_freq = [0] * 26
        window_freq = [0] * 26

        # Заполняем частоты для s1 и первого окна в s2
        for i in range(len(s1)):
            s1_freq[ord(s1[i]) - ord("a")] += 1
            window_freq[ord(s2[i]) - ord("a")] += 1

        # Считаем начальное количество совпадений частот
        matches = 0
        for i in range(26):
            if s1_freq[i] == window_freq[i]:
                matches += 1

        # Скользим окном по s2, начиная с позиции len(s1)
        for right in range(len(s1), len(s2)):
            # Если все 26 частот совпали — нашли перестановку
            if matches == 26:
                return True

            # Добавляем новый символ справа в окно
            right_char_index = ord(s2[right]) - ord("a")

            # Обновляем matches ДО изменения частоты
            if window_freq[right_char_index] == s1_freq[right_char_index]:
                matches -= 1  # Было совпадение, станет несовпадение
            elif window_freq[right_char_index] + 1 == s1_freq[right_char_index]:
                matches += 1  # Было несовпадение, станет совпадение

            window_freq[right_char_index] += 1

            # Удаляем старый символ слева из окна
            left = right - len(s1)
            left_char_index = ord(s2[left]) - ord("a")

            # Обновляем matches ДО изменения частоты
            if window_freq[left_char_index] == s1_freq[left_char_index]:
                matches -= 1  # Было совпадение, станет несовпадение
            elif window_freq[left_char_index] - 1 == s1_freq[left_char_index]:
                matches += 1  # Было несовпадение, станет совпадение

            window_freq[left_char_index] -= 1

        # Проверяем последнее положение окна
        return matches == 26


def main():
    """Тест-кейсы для задачи Permutation in String."""
    solution = Solution()

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ЗАДАЧИ PERMUTATION IN STRING")
    print("=" * 60)

    # Тест 1: Стандартный случай из примера LeetCode
    s1 = "ab"
    s2 = "eidbaooo"
    result = solution.checkInclusion(s1, s2)
    expected = True
    print(f"\nТест 1: s1 = '{s1}', s2 = '{s2}'")
    print(f"Результат: {result} (подстрока 'ba' — перестановка 'ab')")
    assert result == expected, f"Тест 1 провален!"
    print("✓ Пройден")

    # Тест 2: Перестановки нет
    s1 = "ab"
    s2 = "eidboaoo"
    result = solution.checkInclusion(s1, s2)
    expected = False
    print(f"\nТест 2: s1 = '{s1}', s2 = '{s2}'")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 2 провален!"
    print("✓ Пройден")

    # Тест 3: s1 длиннее s2
    s1 = "abc"
    s2 = "ab"
    result = solution.checkInclusion(s1, s2)
    expected = False
    print(f"\nТест 3: s1 = '{s1}', s2 = '{s2}' (s1 длиннее)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 3 провален!"
    print("✓ Пройден")

    # Тест 4: s1 и s2 одинаковые
    s1 = "abc"
    s2 = "abc"
    result = solution.checkInclusion(s1, s2)
    expected = True
    print(f"\nТест 4: s1 = '{s1}', s2 = '{s2}' (одинаковые)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 4 провален!"
    print("✓ Пройден")

    # Тест 5: Перестановка в самом начале
    s1 = "ab"
    s2 = "abx"
    result = solution.checkInclusion(s1, s2)
    expected = True
    print(f"\nТест 5: s1 = '{s1}', s2 = '{s2}' (перестановка в начале)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 5 провален!"
    print("✓ Пройден")

    # Тест 6: Перестановка в самом конце
    s1 = "ab"
    s2 = "xba"
    result = solution.checkInclusion(s1, s2)
    expected = True
    print(f"\nТест 6: s1 = '{s1}', s2 = '{s2}' (перестановка в конце)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 6 провален!"
    print("✓ Пройден")

    # Тест 7: Одиночные символы
    s1 = "a"
    s2 = "a"
    result = solution.checkInclusion(s1, s2)
    expected = True
    print(f"\nТест 7: s1 = '{s1}', s2 = '{s2}' (одиночные)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 7 провален!"
    print("✓ Пройден")

    # Тест 8: Длинная строка с перестановкой в середине
    s1 = "abc"
    s2 = "xyz" + "bca" + "www"
    result = solution.checkInclusion(s1, s2)
    expected = True
    print(f"\nТест 8: s1 = '{s1}', s2 = '{s2}' (перестановка 'bca' в середине)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 8 провален!"
    print("✓ Пройден")

    # Тест 9: Все символы одинаковые
    s1 = "aa"
    s2 = "baab"
    result = solution.checkInclusion(s1, s2)
    expected = True
    print(f"\nТест 9: s1 = '{s1}', s2 = '{s2}' (одинаковые символы)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 9 провален!"
    print("✓ Пройден")

    print("\n" + "=" * 60)
    print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО! ✓")
    print("=" * 60)


if __name__ == "__main__":
    main()
