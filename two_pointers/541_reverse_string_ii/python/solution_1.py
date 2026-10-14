class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        """
        Разворачивает первые k символов для каждых 2k символов.
        """
        # Конвертируем строку в список, так как строки в Python неизменяемы
        chars = list(s)
        n = len(chars)

        # Проходим по строке с шагом 2k.
        # i — это начало текущего блока 2k.
        for i in range(0, n, 2 * k):
            # Разворачиваем первые k символов в текущем блоке.
            # Магия Python: срез chars[i:i+k] автоматически обрежется,
            # если i+k выходит за пределы списка. Это значит, что правило
            # "если осталось меньше k символов, развернуть все"
            # выполняется АВТОМАТИЧЕСКИ без дополнительных проверок!
            chars[i : i + k] = chars[i : i + k][::-1]

        # Собираем список обратно в строку
        return "".join(chars)


def run_tests():
    solution = Solution()

    test_cases = [
        # Стандартные случаи
        ("abcdefg", 2, "bacdfeg", "Стандартный пример 1"),
        ("abcd", 2, "bacd", "Стандартный пример 2"),
        # Граничные случаи (Edge Cases)
        ("a", 2, "a", "Длина строки меньше k"),
        ("abc", 3, "cba", "Длина строки равна k"),
        ("abcdef", 3, "cbadef", "Длина строки равна 2k"),
        ("abcdefg", 3, "cbadefg", "Длина строки между k и 2k"),
        ("abcdefgh", 3, "cbadefhg", "Больше 2k, но не кратно"),
    ]

    print("=" * 70)
    print("ТЕСТИРОВАНИЕ REVERSE STRING II")
    print("=" * 70)

    passed = 0
    for s, k, expected, description in test_cases:
        result = solution.reverseStr(s, k)
        if result == expected:
            print(f"✅ {description}: s='{s}', k={k} -> '{result}'")
            passed += 1
        else:
            print(f"❌ {description}: s='{s}', k={k}")
            print(f"   Ожидалось: '{expected}'")
            print(f"   Получено:  '{result}'")

    print("=" * 70)
    print(f"Результат: {passed}/{len(test_cases)} тестов пройдено")


run_tests()
