class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        Сравнивает строки за O(N) времени и O(1) памяти.
        Идём с конца строк, пропуская символы, удалённые backspace.
        """
        i, j = len(s) - 1, len(t) - 1
        skip_s, skip_t = 0, 0  # Счётчики пропусков для каждой строки

        while i >= 0 or j >= 0:
            # Находим следующий "реальный" символ в s
            while i >= 0:
                if s[i] == "#":
                    skip_s += 1
                    i -= 1
                elif skip_s > 0:
                    skip_s -= 1
                    i -= 1
                else:
                    break  # Нашли реальный символ

            # Находим следующий "реальный" символ в t
            while j >= 0:
                if t[j] == "#":
                    skip_t += 1
                    j -= 1
                elif skip_t > 0:
                    skip_t -= 1
                    j -= 1
                else:
                    break  # Нашли реальный символ

            # Сравниваем найденные символы
            # Если один указатель вышел за границу, а другой нет — строки разные
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                # Одна строка закончилась, другая — нет
                return False

            # Двигаем оба указателя дальше
            i -= 1
            j -= 1

        return True


def run_tests():
    solution = Solution()

    test_cases = [
        # Стандартные примеры
        ("ab#c", "ad#c", True, "Обе становятся 'ac'"),
        ("ab##", "c#d#", True, "Обе становятся ''"),
        ("a#c", "b", False, "s='c', t='b'"),
        # Граничные случаи
        ("", "", True, "Обе пустые"),
        ("#", "#", True, "Обе backspace на пустой строке"),
        ("a#", "a#", True, "Backspace удаляет единственный символ"),
        ("a#", "", True, "Первая становится '', вторая уже ''"),
        ("", "a#", True, "Вторая становится '', первая уже ''"),
        ("abc", "abc", True, "Одинаковые строки без backspace"),
        ("abc", "abcd", False, "Разная длина"),
        ("#a#c", "#a#c", True, "Backspace в начале строки"),
        ("a##c", "#a#c", True, "Разное расположение backspace, результат 'c'"),
        ("nzp#o#g", "nzp#og", True, "Сложный случай с несколькими backspace"),
    ]

    print("=" * 70)
    print("ТЕСТИРОВАНИЕ BACKSPACE STRING COMPARE")
    print("=" * 70)

    passed = 0
    for s, t, expected, description in test_cases:
        result = solution.backspaceCompare(s, t)
        if result == expected:
            print(f"✅ {description}: s='{s}', t='{t}' -> {result}")
            passed += 1
        else:
            print(f"❌ {description}: s='{s}', t='{t}'")
            print(f"   Ожидалось: {expected}")
            print(f"   Получено:  {result}")

    print("=" * 70)
    print(f"Результат: {passed}/{len(test_cases)} тестов пройдено")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()
