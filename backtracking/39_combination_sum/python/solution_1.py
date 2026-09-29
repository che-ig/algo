"""
Это классическая задача на бэктрекинг с повторным использованием элементов. Ключевое отличие от предыдущих задач — одно и то же число можно брать неограниченное количество раз.
Ключевая идея
Чтобы избежать дубликатов комбинаций (например, [2,2,3] и [2,3,2]), мы используем параметр start_index. На каждом шаге рекурсии мы можем:

    Взять текущий элемент и остаться на том же индексе (так как можно использовать повторно)
    Пропустить текущий элемент и перейти к следующему

Таким образом, мы всегда двигаемся вправо по массиву и никогда не возвращаемся к предыдущим элементам.
"""


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        Находит все уникальные комбинации чисел из candidates, которые в сумме дают target.
        Одно и то же число можно использовать неограниченное количество раз.
        """
        result = []
        # Сортируем для оптимизации: можно прекратить перебор, когда элемент > target
        candidates.sort()

        def backtrack(
            start_index: int, current_combination: list[int], remaining_target: int
        ) -> None:
            """
            Рекурсивно ищет комбинации.
            start_index - индекс, с которого можно брать элементы (избегаем дубликатов)
            current_combination - текущая собираемая комбинация
            remaining_target - сколько ещё нужно набрать до target
            """
            # Базовый случай: набрали нужную сумму
            if remaining_target == 0:
                result.append(current_combination[:])  # Добавляем копию
                return

            # Пробуем каждый элемент начиная с start_index
            for i in range(start_index, len(candidates)):
                current_num = candidates[i]

                # Оптимизация: если текущий элемент больше оставшегося target,
                # то все последующие элементы тоже будут больше (массив отсортирован)
                if current_num > remaining_target:
                    break

                # 1. Выбираем: добавляем элемент в комбинацию
                current_combination.append(current_num)

                # 2. Исследуем: рекурсивно ищем дальше
                # Важно: передаём i (не i+1), так как можно использовать элемент повторно
                backtrack(i, current_combination, remaining_target - current_num)

                # 3. Отменяем выбор (Backtrack)
                current_combination.pop()

        # Запускаем бэктрекинг с первого элемента (индекс 0)
        backtrack(0, [], target)

        return result


def main():
    """Тест-кейсы для задачи Combination Sum."""
    solution = Solution()

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ЗАДАЧИ COMBINATION SUM")
    print("=" * 60)

    # Тест 1: Стандартный случай из примера LeetCode
    candidates = [2, 3, 6, 7]
    target = 7
    result = solution.combinationSum(candidates, target)
    expected = [[2, 2, 3], [7]]
    print(f"\nТест 1: candidates = {candidates}, target = {target}")
    print(f"Результат: {result}")
    assert sorted([sorted(c) for c in result]) == sorted(
        [sorted(c) for c in expected]
    ), "Тест 1 провален!"
    print("✓ Пройден")

    # Тест 2: Второй пример из LeetCode
    candidates = [2, 3, 5]
    target = 8
    result = solution.combinationSum(candidates, target)
    expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    print(f"\nТест 2: candidates = {candidates}, target = {target}")
    print(f"Результат: {result}")
    assert sorted([sorted(c) for c in result]) == sorted(
        [sorted(c) for c in expected]
    ), "Тест 2 провален!"
    print("✓ Пройден")

    # Тест 3: Нет возможных комбинаций
    candidates = [2]
    target = 1
    result = solution.combinationSum(candidates, target)
    expected = []
    print(f"\nТест 3: candidates = {candidates}, target = {target} (нет решений)")
    print(f"Результат: {result}")
    assert result == expected, "Тест 3 провален!"
    print("✓ Пройден")

    # Тест 4: Один элемент равен target
    candidates = [2, 3, 5]
    target = 5
    result = solution.combinationSum(candidates, target)
    expected = [[5]]
    print(f"\nТест 4: candidates = {candidates}, target = {target}")
    print(f"Результат: {result}")
    assert sorted([sorted(c) for c in result]) == sorted(
        [sorted(c) for c in expected]
    ), "Тест 4 провален!"
    print("✓ Пройден")

    # Тест 5: Максимальное использование одного элемента
    candidates = [2]
    target = 40
    result = solution.combinationSum(candidates, target)
    expected = [[2] * 20]  # 20 двоек = 40
    print(
        f"\nТест 5: candidates = {candidates}, target = {target} (максимальное повторение)"
    )
    print(f"Количество комбинаций: {len(result)}")
    assert result == expected, "Тест 5 провален!"
    print("✓ Пройден")

    # Тест 6: Несколько комбинаций с разными длинами
    candidates = [2, 3, 6, 7]
    target = 14
    result = solution.combinationSum(candidates, target)
    print(f"\nТест 6: candidates = {candidates}, target = {target}")
    print(f"Количество комбинаций: {len(result)}")
    print(f"Комбинации: {result}")
    # Проверяем, что все комбинации в сумме дают target
    for combo in result:
        assert sum(combo) == target, f"Комбинация {combo} не даёт сумму {target}!"
    print("✓ Пройден")

    print("\n" + "=" * 60)
    print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО! ✓")
    print("=" * 60)


if __name__ == "__main__":
    main()
