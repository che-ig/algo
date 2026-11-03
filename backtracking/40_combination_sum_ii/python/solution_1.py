class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        Находит все уникальные комбинации, дающих target.
        Каждый элемент можно использовать только один раз.
        В массиве могут быть дубликаты.

        Стратегия:
        - Сортируем массив, чтобы дубликаты были рядом
        - На каждом уровне рекурсии пропускаем дубликаты
        - Передаём i+1 (не i!), потому что каждый элемент используется один раз

        Args:
            candidates: Массив целых чисел (может содержать дубликаты)
            target: Целевая сумма

        Returns:
            Список всех уникальных комбинаций, дающих target
        """
        # КРИТИЧНО: сортируем, чтобы дубликаты были рядом
        candidates.sort()

        result: list[list[int]] = []
        current: list[int] = []
        n = len(candidates)

        def backtrack(start: int, remaining: int) -> None:
            """
            Строит комбинации, начиная с индекса start.

            Args:
                start: Индекс, с которого можно брать кандидатов
                remaining: Оставшаяся сумма, которую нужно набрать
            """
            # Базовый случай: набрали нужную сумму
            if remaining == 0:
                result.append(current.copy())
                return

            # Перебираем кандидатов начиная с start
            for i in range(start, n):
                candidate = candidates[i]

                # ПРОПУСК ДУБЛИКАТОВ:
                # Если это не первый элемент на текущем уровне
                # И он совпадает с предыдущим — пропускаем
                # Это предотвращает генерацию одинаковых комбинаций
                if i > start and candidate == candidates[i - 1]:
                    continue

                # Раннее отсечение: если кандидат больше remaining,
                # все последующие тоже не подойдут (массив отсортирован)
                if candidate > remaining:
                    break  # break, а не continue, потому что массив отсортирован

                # 1. ДЕЛАЕМ ВЫБОР: берём текущий кандидат
                current.append(candidate)

                # 2. ИССЛЕДУЕМ: рекурсивно ищем дальше
                # Передаём i+1 (не i!), потому что каждый элемент
                # можно использовать только один раз
                backtrack(i + 1, remaining - candidate)

                # 3. ОТКАТЫВАЕМ ВЫБОР: убираем кандидата
                current.pop()

        backtrack(0, target)
        return result


def normalize(combinations: list[list[int]]) -> list[tuple[int, ...]]:
    """Приводит ответ к каноническому виду для сравнения."""
    return sorted(tuple(sorted(c)) for c in combinations)


def run_tests() -> None:
    test_cases: list[tuple[list[int], int, list[list[int]], str]] = [
        (
            [10, 1, 2, 7, 6, 1, 5],
            8,
            [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]],
            "Пример 1: дубликаты в массиве",
        ),
        ([2, 5, 2, 1, 2], 5, [[1, 2, 2], [5]], "Пример 2: много дубликатов"),
        ([1], 1, [[1]], "Один элемент = target"),
        ([1], 2, [], "Один элемент < target"),
        ([1, 2, 3], 0, [], "Target = 0 (невозможно по ограничениям)"),
        ([1, 1, 1, 1], 2, [[1, 1]], "Все одинаковые, target = 2"),
        (
            [1, 2, 3, 4, 5],
            10,
            [[1, 2, 3, 4], [1, 4, 5], [2, 3, 5]],
            "Несколько комбинаций",
        ),
        ([5, 5, 5, 5], 10, [[5, 5]], "Дубликаты, target = 10"),
    ]

    print("=" * 70)
    print("ТЕСТИРОВАНИЕ COMBINATION SUM II")
    print("=" * 70)

    # Backtracking
    print("\n📌 Backtracking:")
    solution_bt = Solution()
    passed = 0
    for candidates, target, expected, description in test_cases:
        result = solution_bt.combinationSum2(candidates, target)
        if normalize(result) == normalize(expected):
            print(f"✅ {description}: {len(result)} комбинаций")
            passed += 1
        else:
            print(f"❌ {description}: candidates={candidates}, target={target}")
            print(f"   Ожидалось: {expected}")
            print(f"   Получено:  {result}")
    print(f"\nРезультат: {passed}/{len(test_cases)} тестов пройдено")

    # Перебор частот
    print("\n📌 Перебор частот:")
    passed = 0
    for candidates, target, expected, description in test_cases:
        result = solution_bt.combinationSum2(candidates, target)
        if normalize(result) == normalize(expected):
            print(f"✅ {description}: {len(result)} комбинаций")
            passed += 1
        else:
            print(f"❌ {description}: candidates={candidates}, target={target}")
            print(f"   Ожидалось: {expected}")
            print(f"   Получено:  {result}")
    print(f"\nРезультат: {passed}/{len(test_cases)} тестов пройдено")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()
