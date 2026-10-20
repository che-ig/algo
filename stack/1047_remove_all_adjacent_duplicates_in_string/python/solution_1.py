class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        Удаляет все соседние дубликаты из строки.
        Использует стек для отслеживания "активных" символов.
        """
        stack = []

        for char in s:
            # Если стек не пуст и верхний элемент совпадает с текущим символом
            if stack and stack[-1] == char:
                stack.pop()  # "Аннигиляция": удаляем пару дубликатов
            else:
                stack.append(char)  # Кладём символ в стек

        # Собираем стек обратно в строку
        return "".join(stack)


def run_tests():
    solution = Solution()

    test_cases = [
        ("abbaca", "ca", "Стандартный пример 1 (каскадное удаление)"),
        ("azxxzy", "ay", "Стандартный пример 2"),
        ("a", "a", "Один символ"),
        ("aa", "", "Пара дубликатов"),
        ("aaa", "a", "Три одинаковых (удаляется пара, остаётся один)"),
        ("aaaa", "", "Четыре одинаковых"),
        ("ab", "ab", "Нет дубликатов"),
        ("abba", "", "Палиндром-дубликат"),
        ("abcddcba", "", "Вложенные дубликаты"),
        ("abcde", "abcde", "Все уникальные"),
    ]

    print("=" * 70)
    print("ТЕСТИРОВАНИЕ REMOVE ADJACENT DUPLICATES")
    print("=" * 70)

    passed = 0
    for s, expected, description in test_cases:
        result = solution.removeDuplicates(s)
        if result == expected:
            print(f"✅ {description}: '{s}' -> '{result}'")
            passed += 1
        else:
            print(f"❌ {description}: '{s}'")
            print(f"   Ожидалось: '{expected}'")
            print(f"   Получено:  '{result}'")

    print("=" * 70)
    print(f"Результат: {passed}/{len(test_cases)} тестов пройдено")


run_tests()
