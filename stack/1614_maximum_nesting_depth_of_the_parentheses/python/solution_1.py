class Solution:
    def maxDepth(self, s: str) -> int:
        """
        Возвращает максимальную глубину вложенности скобок.
        """
        current_depth = 0
        max_depth = 0

        for char in s:
            if char == "(":
                current_depth += 1
                # Обновляем максимум сразу при открытии скобки
                max_depth = max(max_depth, current_depth)
            elif char == ")":
                current_depth -= 1

        return max_depth


def run_tests():
    solution = Solution()

    test_cases = [
        ("(1+(2*3)+((8)/4))+1", 3, "Стандартный пример 1"),
        ("(1)+((2))+(((3)))", 3, "Стандартный пример 2"),
        ("()(())((()()))", 3, "Стандартный пример 3"),
        ("", 0, "Пустая строка (хотя по условию n >= 1)"),
        ("1", 0, "Нет скобок"),
        ("()", 1, "Одна пара скобок"),
        ("((()))", 3, "Только вложенные скобки"),
        ("()()()", 1, "Только последовательные скобки"),
        ("(a*(b-c)+d)", 1, "Математическое выражение"),
    ]

    print("=" * 70)
    print("ТЕСТИРОВАНИЕ MAXIMUM NESTING DEPTH")
    print("=" * 70)

    passed = 0
    for s, expected, description in test_cases:
        result = solution.maxDepth(s)
        if result == expected:
            print(f"✅ {description}: '{s}' -> {result}")
            passed += 1
        else:
            print(f"❌ {description}: '{s}'")
            print(f"   Ожидалось: {expected}")
            print(f"   Получено:  {result}")

    print("=" * 70)
    print(f"Результат: {passed}/{len(test_cases)} тестов пройдено")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()
