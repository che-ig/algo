class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        """
        Вычисляет префиксную сумму массива.
        runningSum[i] = nums[0] + nums[1] + ... + nums[i]

        Args:
            nums: Исходный массив целых чисел

        Returns:
            Новый массив, где каждый элемент — сумма всех предыдущих
            элементов исходного массива включая текущий
        """
        n = len(nums)
        result: list[int] = [0] * n

        # Первый элемент префиксной суммы равен первому элементу исходного
        result[0] = nums[0]

        # Для каждого следующего элемента: текущая префиксная сумма =
        # предыдущая префиксная сумма + текущий элемент
        for i in range(1, n):
            result[i] = result[i - 1] + nums[i]

        return result


def run_tests() -> None:
    solution = Solution()

    test_cases: list[tuple[list[int], list[int], str]] = [
        ([1, 2, 3, 4], [1, 3, 6, 10], "Пример 1: стандартный случай"),
        ([1, 1, 1, 1, 1], [1, 2, 3, 4, 5], "Пример 2: одинаковые элементы"),
        ([3, 1, 2, 10, 1], [3, 4, 6, 16, 17], "Пример 3: случайный порядок"),
        ([5], [5], "Один элемент"),
        ([0, 0, 0], [0, 0, 0], "Все нули"),
        ([-1, -2, -3], [-1, -3, -6], "Отрицательные числа"),
        ([-1, 2, -3, 4], [-1, 1, -2, 2], "Смешанные положительные и отрицательные"),
        ([1000000, 1000000], [1000000, 2000000], "Большие числа (граничное значение)"),
        ([-1000000, 1000000], [-1000000, 0], "Компенсация больших чисел"),
    ]

    print("=" * 70)
    print("ТЕСТИРОВАНИЕ RUNNING SUM OF 1D ARRAY")
    print("=" * 70)

    passed = 0
    for nums, expected, description in test_cases:
        # Создаём копию, чтобы in-place модификация не ломала тесты
        nums_copy = nums.copy()
        result = solution.runningSum(nums_copy)

        if result == expected:
            print(f"✅ {description}: {nums} -> {result}")
            passed += 1
        else:
            print(f"❌ {description}: {nums}")
            print(f"   Ожидалось: {expected}")
            print(f"   Получено:  {result}")

    print("=" * 70)
    print(f"Результат: {passed}/{len(test_cases)} тестов пройдено")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()
