from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Находит минимальную подстроку в s, которая содержит все символы из t.
        Использует скользящее окно переменного размера.
        """
        # Edge case: если t длиннее s, решение невозможно
        if len(t) > len(s):
            return ""

        # Считаем частоты символов в t
        # t_freq = {'A': 1, 'B': 1, 'C': 1} для t = "ABC"
        t_freq = Counter(t)

        # required — количество уникальных символов в t, которые нужно найти
        # Для t = "ABC" required = 3
        # Для t = "AABC" required = 3 (только 'A' и 'B' и 'C', но 'A' нужно 2 раза)
        required = len(t_freq)

        # formed — количество уникальных символов, которые уже найдены в нужном количестве
        formed = 0

        # window_freq — частоты символов в текущем окне
        window_freq = {}

        # left и right — границы скользящего окна
        left = 0
        right = 0

        # ans хранит (длину_окна, левую_границу, правую_границу)
        # Инициализируем бесконечностью, чтобы любое найденное окно было меньше
        ans = (float("inf"), 0, 0)

        # Расширяем окно вправо
        while right < len(s):
            # Добавляем символ s[right] в окно
            char = s[right]
            window_freq[char] = window_freq.get(char, 0) + 1

            # Проверяем, достигли ли мы нужного количества этого символа
            # Если да — увеличиваем formed
            if char in t_freq and window_freq[char] == t_freq[char]:
                formed += 1

            # Пока окно валидно (содержит все символы из t), пытаемся его сжать
            while left <= right and formed == required:
                char = s[left]

                # Обновляем минимальное окно
                current_window_length = right - left + 1
                if current_window_length < ans[0]:
                    ans = (current_window_length, left, right)

                # Удаляем символ s[left] из окна
                window_freq[char] -= 1

                # Если после удаления частота стала меньше требуемой,
                # окно больше не валидно — уменьшаем formed
                if char in t_freq and window_freq[char] < t_freq[char]:
                    formed -= 1

                # Сдвигаем левую границу вправо
                left += 1

            # Сдвигаем правую границу вправо
            right += 1

        # Если нашли валидное окно — возвращаем подстроку, иначе пустую строку
        if ans[0] != float("inf"):
            return s[ans[1] : ans[2] + 1]
        else:
            return ""


def main():
    """Тест-кейсы для задачи Minimum Window Substring."""
    solution = Solution()

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ЗАДАЧИ MINIMUM WINDOW SUBSTRING")
    print("=" * 60)

    # Тест 1: Стандартный случай из примера LeetCode
    s = "ADOBECODEBANC"
    t = "ABC"
    result = solution.minWindow(s, t)
    expected = "BANC"
    print(f"\nТест 1: s = '{s}', t = '{t}'")
    print(f"Результат: '{result}'")
    assert result == expected, (
        f"Тест 1 провален! Ожидалось '{expected}', получено '{result}'"
    )
    print("✓ Пройден")

    # Тест 2: Минимальный случай
    s = "a"
    t = "a"
    result = solution.minWindow(s, t)
    expected = "a"
    print(f"\nТест 2: s = '{s}', t = '{t}'")
    print(f"Результат: '{result}'")
    assert result == expected, f"Тест 2 провален!"
    print("✓ Пройден")

    # Тест 3: Недостаточно символов в s
    s = "a"
    t = "aa"
    result = solution.minWindow(s, t)
    expected = ""
    print(f"\nТест 3: s = '{s}', t = '{t}' (недостаточно символов)")
    print(f"Результат: '{result}'")
    assert result == expected, f"Тест 3 провален!"
    print("✓ Пройден")

    # Тест 4: Дубликаты в t
    s = "aabbcc"
    t = "abc"
    result = solution.minWindow(s, t)
    expected = "abc"
    print(f"\nТест 4: s = '{s}', t = '{t}' (дубликаты в s)")
    print(f"Результат: '{result}'")
    assert result == expected, f"Тест 4 провален!"
    print("✓ Пройден")

    # Тест 5: Требуется несколько одинаковых символов
    s = "aabbcc"
    t = "aab"
    result = solution.minWindow(s, t)
    expected = "aab"
    print(f"\nТест 5: s = '{s}', t = '{t}' (требуется 'aab')")
    print(f"Результат: '{result}'")
    assert result == expected, f"Тест 5 провален!"
    print("✓ Пройден")

    # Тест 6: Все символы одинаковые
    s = "aaaa"
    t = "aa"
    result = solution.minWindow(s, t)
    expected = "aa"
    print(f"\nТест 6: s = '{s}', t = '{t}' (все одинаковые)")
    print(f"Результат: '{result}'")
    assert result == expected, f"Тест 6 провален!"
    print("✓ Пройден")

    # Тест 7: Большое окно в середине
    s = "xyz" + "ABCDEF" + "www"
    t = "ACE"
    result = solution.minWindow(s, t)
    expected = "ABCDEF"
    print(f"\nТест 7: s = '{s}', t = '{t}' (большое окно)")
    print(f"Результат: '{result}'")
    assert result == expected, f"Тест 7 провален!"
    print("✓ Пройден")

    # Тест 8: Регистр имеет значение
    s = "aA"
    t = "A"
    result = solution.minWindow(s, t)
    expected = "A"
    print(f"\nТест 8: s = '{s}', t = '{t}' (регистр важен)")
    print(f"Результат: '{result}'")
    assert result == expected, f"Тест 8 провален!"
    print("✓ Пройден")

    print("\n" + "=" * 60)
    print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО! ✓")
    print("=" * 60)


if __name__ == "__main__":
    main()
