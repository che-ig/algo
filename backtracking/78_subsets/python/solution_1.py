class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        Генерирует все подмножества (power set) через backtracking.

        Args:
            nums: Массив различных целых чисел

        Returns:
            Список всех возможных подмножеств
        """
        result: list[list[int]] = []
        current_subset: list[int] = []

        def backtrack(start: int) -> None:
            """
            Backtracking-функция: строит подмножества, начиная с индекса start.

            Args:
                start: Индекс, с которого начинаем выбирать элементы
            """
            # ВАЖНО: добавляем текущее подмножество в результат НА КАЖДОМ ШАГЕ
            # Это отличается от Permutations, где добавляли только в базовом случае
            result.append(current_subset.copy())

            # Перебираем все кандидаты, начиная с start
            for i in range(start, len(nums)):
                # 1. ДЕЛАЕМ ВЫБОР: добавляем элемент в подмножество
                current_subset.append(nums[i])

                # 2. ИССЛЕДУЕМ: рекурсивно добавляем оставшиеся элементы
                # Передаём i + 1, чтобы не возвращаться к уже рассмотренным
                backtrack(i + 1)

                # 3. ОТКАТЫВАЕМ ВЫБОР: убираем элемент, чтобы попробовать другой
                current_subset.pop()

        backtrack(0)
        return result


def run_tests() -> None:
    solution = Solution()

    test_cases: list[tuple[list[int], int, str]] = [
        ([1, 2, 3], 8, "Пример 1: три элемента → 2^3 = 8 подмножеств"),
        ([0], 2, "Пример 2: один элемент → 2^1 = 2 подмножества"),
        ([1, 2], 4, "Два элемента → 2^2 = 4 подмножества"),
        ([-1, 0, 1], 8, "Отрицательные числа"),
        ([1, 2, 3, 4], 16, "Четыре элемента → 2^4 = 16 подмножеств"),
    ]

    print("=" * 70)
    print("ТЕСТИРОВАНИЕ SUBSETS")
    print("=" * 70)

    passed = 0
    for nums, expected_count, description in test_cases:
        result = solution.subsets(nums)

        # Проверяем количество подмножеств
        if len(result) == expected_count:
            print(f"✅ {description}")
            print(f"   Результат: {result}")
            passed += 1
        else:
            print(f"❌ {description}: {nums}")
            print(f"   Ожидалось: {expected_count} подмножеств")
            print(f"   Получено:  {len(result)} подмножеств")
            print(f"   Результат: {result}")

    print("=" * 70)
    print(f"Результат: {passed}/{len(test_cases)} тестов пройдено")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()
