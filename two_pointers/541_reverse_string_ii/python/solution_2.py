class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        """
        Разворачивает первые k символов для каждых 2k символов.
        Без использования срезов — явная реализация через два указателя.
        """
        # Конвертируем строку в список для in-place модификации
        chars = list(s)
        n = len(chars)

        # Проходим по строке с шагом 2k
        for i in range(0, n, 2 * k):
            # Определяем границы разворота.
            # Начало — всегда i.
            # Конец — либо i + k - 1, либо конец массива (n - 1), если осталось меньше k символов.
            left = i
            right = min(i + k - 1, n - 1)

            # Разворачиваем подмассив [left, right] через два указателя
            self._reverse(chars, left, right)

        return "".join(chars)

    def _reverse(self, chars: list[str], left: int, right: int) -> None:
        """
        Разворачивает подмассив chars[left..right] in-place.
        Классический алгоритм с двумя указателями.
        """
        while left < right:
            # Меняем местами символы на позициях left и right
            chars[left], chars[right] = chars[right], chars[left]

            # Двигаем указатели к центру
            left += 1
            right -= 1


def run_tests():
    solution = Solution()

    test_cases = [
        # Стандартные случаи
        ("abcdefg", 2, "bacdfeg", "Стандартный пример 1"),
        ("abcd", 2, "bacd", "Стандартный пример 2"),
        # Граничные случаи
        ("a", 2, "a", "Длина строки меньше k"),
        ("abc", 3, "cba", "Длина строки равна k"),
        ("abcdef", 3, "cbadef", "Длина строки равна 2k"),
        ("abcdefg", 3, "cbadefg", "Длина строки между k и 2k"),
        ("abcdefgh", 3, "cbadefhg", "Больше 2k, но не кратно"),
        # Дополнительные edge cases
        ("", 1, "", "Пустая строка"),  # хотя по условию n >= 1
        ("a", 1, "a", "k = 1, один символ"),
        ("ab", 1, "ba", "k = 1, два символа"),
        ("abcde", 1, "badce", "k = 1, разворот каждой пары"),
    ]

    print("=" * 70)
    print("ТЕСТИРОВАНИЕ REVERSE STRING II (без срезов)")
    print("=" * 70)

    passed = 0
    for s, k, expected, description in test_cases:
        result = solution.reverseStr(s, k)
        if result == expected:
            print(f"✅ {description}: s='{s}', k={k} -> '{result}'")
            passed += 1
        else:
            print(f" {description}: s='{s}', k={k}")
            print(f"   Ожидалось: '{expected}'")
            print(f"   Получено:  '{result}'")

    print("=" * 70)
    print(f"Результат: {passed}/{len(test_cases)} тестов пройдено")


run_tests()
