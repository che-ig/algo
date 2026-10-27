class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """
        Проверяет, является ли n степенью тройки через последовательное деление.

        Args:
            n: Проверяемое целое число

        Returns:
            True, если n является степенью тройки, иначе False
        """
        # Степени тройки всегда положительны
        if n <= 0:
            return False

        # Делим на 3, пока возможно
        while n % 3 == 0:
            n //= 3

        # Если получили 1 — это степень тройки
        return n == 1


def run_tests() -> None:
    solution = Solution()

    test_cases: list[tuple[int, bool, str]] = [
        (27, True, "Пример 1: 3^3 = 27"),
        (0, False, "Пример 2: 0 не степень тройки"),
        (-1, False, "Пример 3: отрицательное число"),
        (1, True, "3^0 = 1 — степень тройки"),
        (3, True, "3^1 = 3"),
        (9, True, "3^2 = 9"),
        (81, True, "3^4 = 81"),
        (243, True, "3^5 = 243"),
        (1162261467, True, "3^19 — максимальная степень в int32"),
        (45, False, "45 = 9 * 5 — не степень тройки"),
        (10, False, "10 не степень тройки"),
        (2, False, "2 не степень тройки"),
        (-3, False, "Отрицательная степень не считается"),
        (-27, False, "Отрицательное число"),
        (2147483647, False, "2^31 - 1 — не степень тройки"),
    ]

    print("=" * 70)
    print("ТЕСТИРОВАНИЕ POWER OF THREE (Магическое число)")
    print("=" * 70)

    passed = 0
    for n, expected, description in test_cases:
        result = solution.isPowerOfThree(n)

        if result == expected:
            print(f"✅ {description}: n={n} -> {result}")
            passed += 1
        else:
            print(f"❌ {description}: n={n}")
            print(f"   Ожидалось: {expected}")
            print(f"   Получено:  {result}")

    print("=" * 70)
    print(f"Результат: {passed}/{len(test_cases)} тестов пройдено")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()
