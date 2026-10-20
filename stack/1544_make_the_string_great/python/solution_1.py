class Solution:
    def makeGood(self, s: str) -> str:
        """
        Удаляет соседние символы, которые являются одной и той же буквой
        в разных регистрах, пока строка не станет "хорошей".
        """
        stack = []

        for char in s:
            # Проверяем условие "плохой" пары:
            # 1. Стек не пуст
            # 2. Буквы одинаковые (игнорируя регистр)
            # 3. Но сами символы разные (то есть регистр разный)
            if stack and stack[-1].lower() == char.lower() and stack[-1] != char:
                stack.pop()  # Аннигиляция: убираем верхушку стека
            else:
                stack.append(char)  # Кладём символ в стек

        return "".join(stack)


def run_tests():
    solution = Solution()

    test_cases = [
        # Стандартные примеры из условия
        ("leEeetcode", "leetcode", "Стандартный пример 1"),
        ("abBAcC", "", "Стандартный пример 2 (полная аннигиляция)"),
        ("s", "s", "Стандартный пример 3 (один символ)"),
        # Граничные случаи (Edge Cases)
        ("abc", "abc", "Уже хорошая строка (нет плохих пар)"),
        ("aA", "", "Простая пара (четная длина, полная аннигиляция)"),
        ("Aa", "", "Заглавная буква перед строчной"),
        ("aAa", "a", "Нечетная длина: первая пара удаляется, остается хвост"),
        ("Aaa", "A", "Нечетная длина: вторая пара удаляется, остается голова"),
        ("dDaA", "", "Несколько пар подряд, полная аннигиляция"),
        ("qM", "qM", "Разные буквы и разные регистры (НЕ аннигилируют, разница не 32)"),
        ("aAaA", "", "Чередующиеся пары, полная аннигиляция"),
    ]

    print("=" * 70)
    print("ТЕСТИРОВАНИЕ MAKE THE STRING GREAT")
    print("=" * 70)

    passed = 0
    for s, expected, description in test_cases:
        result = solution.makeGood(s)
        if result == expected:
            print(f"✅ {description}: '{s}' -> '{result}'")
            passed += 1
        else:
            print(f"❌ {description}: '{s}'")
            print(f"   Ожидалось: '{expected}'")
            print(f"   Получено:  '{result}'")

    print("=" * 70)
    print(f"Результат: {passed}/{len(test_cases)} тестов пройдено")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()
