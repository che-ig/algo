class Solution_2:
    # time: O(n)
    # mem:  O(k), где k - число уникальных символов в строке
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        result = 0

        l = 0
        r = 0
        # r - включительно идет, т е наше плавающее окно это [l, r]
        # включительно, т к r = 0, значит 0 символ уже входит в окно,
        # поэтому добавляем в windowChars
        windowChars = {
            s[0],
        }

        # a b c a b a

        while l < len(s):
            # before
            # l
            # a b c a b a
            # r

            # бежим правым указателем пока в интервале [l, r]
            # находятся все последовательные числа
            while r + 1 < len(s) and s[r + 1] not in windowChars:
                windowChars.add(s[r + 1])
                r += 1

            # after
            # l
            # a b c a b a
            #     r

            # обновляем
            result = max(result, r - l + 1)

            # когда двигаем левую границу убираем буквы
            windowChars.remove(s[l])
            l += 1

            # если r < l то обноввляенм r и windowChars
            if r < l < len(s):
                r = l
                # r - включительно идет, поэтому добавляем в windowChars
                windowChars = {s[r]}

        return result


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Находит длину самой длинной подстроки без повторяющихся символов.
        Использует технику скользящего окна и множество (set).
        """
        # Множество для хранения уникальных символов текущего окна
        char_set = set()

        left = 0  # Левая граница окна
        max_len = 0  # Максимальная найденная длина

        # right - правая граница окна, двигаем её по всей строке
        for right in range(len(s)):
            current_char = s[right]

            # Если символ уже есть в множестве, значит мы нашли дубликат.
            # Сужаем окно слева, пока не удалим этот дубликат из множества.
            while current_char in char_set:
                char_set.remove(s[left])
                left += 1

            # Добавляем новый уникальный символ в множество
            char_set.add(current_char)

            # Вычисляем длину текущего окна и обновляем максимум
            # Длина окна = right - left + 1
            max_len = max(max_len, right - left + 1)

        return max_len


def main():
    """Тест-кейсы для задачи Longest Substring Without Repeating Characters."""
    solution = Solution()

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ЗАДАЧИ LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS")
    print("=" * 60)

    # Тест 1: Стандартный случай из примера LeetCode
    s = "abcabcbb"
    result = solution.lengthOfLongestSubstring(s)
    expected = 3
    print(f"\nТест 1: s = '{s}'")
    print(f"Результат: {result} (подстрока 'abc')")
    assert result == expected, f"Тест 1 провален!"
    print("✓ Пройден")

    # Тест 2: Все символы одинаковые
    s = "bbbbb"
    result = solution.lengthOfLongestSubstring(s)
    expected = 1
    print(f"\nТест 2: s = '{s}'")
    print(f"Результат: {result} (подстрока 'b')")
    assert result == expected, f"Тест 2 провален!"
    print("✓ Пройден")

    # Тест 3: Подстрока в середине (важно не перепутать с подпоследовательностью)
    s = "pwwkew"
    result = solution.lengthOfLongestSubstring(s)
    expected = 3
    print(f"\nТест 3: s = '{s}'")
    print(f"Результат: {result} (подстрока 'wke')")
    assert result == expected, f"Тест 3 провален!"
    print("✓ Пройден")

    # Тест 4: Пустая строка (Edge case)
    s = ""
    result = solution.lengthOfLongestSubstring(s)
    expected = 0
    print(f"\nТест 4: s = '{s}' (пустая строка)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 4 провален!"
    print("✓ Пройден")

    # Тест 5: Все символы уникальные
    s = "abcdef"
    result = solution.lengthOfLongestSubstring(s)
    expected = 6
    print(f"\nТест 5: s = '{s}' (все уникальные)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 5 провален!"
    print("✓ Пройден")

    # Тест 6: Пробелы и спецсимволы
    s = "a b c a b c"
    result = solution.lengthOfLongestSubstring(s)
    expected = 4  # "a b " или " b c"
    print(f"\nТест 6: s = '{s}' (с пробелами)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 6 провален!"
    print("✓ Пройден")

    # Тест 7: Дубликат в самом конце
    s = "abcdeaf"
    result = solution.lengthOfLongestSubstring(s)
    expected = 6  # "bcdeaf"
    print(f"\nТест 7: s = '{s}' (дубликат в конце)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 7 провален!"
    print("✓ Пройден")

    print("\n" + "=" * 60)
    print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО! ✓")
    print("=" * 60)


if __name__ == "__main__":
    main()
