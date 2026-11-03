# Сложность
#     Время: O(n * 2^n) в худшем случае, где n = len(nums). При n ≤ 10 это очень быстро.
#     Дополнительная память: O(n) на стек рекурсии и текущее подмножество.
#     Память под ответ: O(n * 2^n) для хранения всех уникальных подмножеств.


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        """
        Генерация всех уникальных подмножеств через backtracking.

        Стратегия:
        1. Сортируем массив, чтобы дубликаты оказались рядом
        2. На каждом уровне рекурсии пропускаем дубликаты
        3. Добавляем текущее подмножество в результат на каждом шаге

        Args:
            nums: Массив целых чисел (может содержать дубликаты)

        Returns:
            Список всех уникальных подмножеств
        """
        # КРИТИЧНО: сортируем массив, чтобы дубликаты были рядом
        nums.sort()

        result: list[list[int]] = []
        current: list[int] = []
        n = len(nums)

        def backtrack(start: int) -> None:
            """
            Строит подмножества, начиная с индекса start.
            Пропускает дубликаты на каждом уровне рекурсии.

            Args:
                start: Индекс, с которого начинаем выбирать элементы
            """
            # Каждое промежуточное состояние — валидное подмножество
            result.append(current.copy())

            # Перебираем кандидатов
            for i in range(start, n):
                # ПРОПУСК ДУБЛИКАТОВ:
                # Если это не первый элемент на текущем уровне
                # И он совпадает с предыдущим — пропускаем
                # Это предотвращает генерацию одинаковых подмножеств
                if i > start and nums[i] == nums[i - 1]:
                    continue

                # 1. ДЕЛАЕМ ВЫБОР: добавляем элемент
                current.append(nums[i])

                # 2. ИССЛЕДУЕМ: рекурсивно добавляем оставшиеся элементы
                # Передаём i + 1, чтобы не возвращаться к уже рассмотренным
                backtrack(i + 1)

                # 3. ОТКАТЫВАЕМ ВЫБОР: убираем элемент
                current.pop()

        backtrack(0)
        return result


def normalize(subsets: list[list[int]]) -> list[tuple[int, ...]]:
    """Приводит ответ к каноническому виду для сравнения."""
    return sorted(tuple(sorted(s)) for s in subsets)


def run_tests() -> None:
    solution = Solution()

    test_cases: list[tuple[list[int], list[list[int]], str]] = [
        (
            [1, 2, 2],
            [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]],
            "Пример 1: один дубликат",
        ),
        ([0], [[], [0]], "Пример 2: один элемент"),
        ([1, 1], [[], [1], [1, 1]], "Два одинаковых элемента"),
        (
            [1, 2, 3],
            [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]],
            "Нет дубликатов",
        ),
        ([1, 1, 1], [[], [1], [1, 1], [1, 1, 1]], "Все элементы одинаковые"),
        (
            [-1, -1, 0],
            [[], [-1], [-1, -1], [-1, 0], [-1, -1, 0], [0]],
            "Отрицательные числа с дубликатами",
        ),
        (
            [4, 4, 4, 4],
            [[], [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]],
            "Четыре одинаковых элемента",
        ),
    ]

    print("=" * 70)
    print("ТЕСТИРОВАНИЕ SUBSETS II")
    print("=" * 70)

    # Тестируем Backtracking
    print("\n📌 Backtracking:")
    passed = 0
    for nums, expected, description in test_cases:
        result = solution.subsetsWithDup(nums)

        if normalize(result) == normalize(expected):
            print(f"✅ {description}: {nums} -> {len(result)} подмножеств")
            passed += 1
        else:
            print(f"❌ {description}: {nums}")
            print(f"   Ожидалось: {expected}")
            print(f"   Получено:  {result}")

    print(f"\nРезультат: {passed}/{len(test_cases)} тестов пройдено")

    # Тестируем Bitmask
    print("\n📌 Bitmask:")
    passed = 0
    for nums, expected, description in test_cases:
        result = solution.subsetsWithDup(nums)

        if normalize(result) == normalize(expected):
            print(f"✅ {description}: {nums} -> {len(result)} подмножеств")
            passed += 1
        else:
            print(f"❌ {description}: {nums}")
            print(f"   Ожидалось: {expected}")
            print(f"   Получено:  {result}")

    print(f"\nРезультат: {passed}/{len(test_cases)} тестов пройдено")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()
