from collections import deque


class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        """
        Находит длину кратчайшего подмассива с суммой >= k.
        Использует префиксные суммы и монотонно возрастающую очередь.
        """
        n = len(nums)

        # Считаем префиксные суммы.
        # prefix[i] = сумма элементов nums[0..i-1]
        # prefix[0] = 0 (пустой префикс)
        # prefix[i] - prefix[j] = сумма подмассива nums[j..i-1]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # Монотонно возрастающая очередь индексов префиксных сумм.
        # Храним индексы так, что prefix[queue[0]] < prefix[queue[1]] < ...
        # Это позволяет быстро находить кратчайший подмассив.
        queue = deque()

        # Минимальная длина подмассива. Инициализируем бесконечностью.
        min_length = float("inf")

        # Проходим по всем префиксным суммам (от 0 до n)
        for j in range(n + 1):
            # Правило 1: Проверяем, можно ли образовать подмассив с суммой >= k
            # Если prefix[j] - prefix[queue[0]] >= k, то подмассив [queue[0], j-1]
            # имеет нужную сумму. Обновляем ответ и удаляем queue[0],
            # потому что для будущих j подмассив будет длиннее.
            while queue and prefix[j] - prefix[queue[0]] >= k:
                min_length = min(min_length, j - queue[0])
                queue.popleft()

            # Правило 2: Поддерживаем монотонность очереди.
            # Если prefix[j] <= prefix[queue[-1]], то queue[-1] больше не нужен.
            # Почему? Потому что для любого будущего j', если prefix[j'] - prefix[queue[-1]] >= k,
            # то и prefix[j'] - prefix[j] >= k (так как prefix[j] <= prefix[queue[-1]]),
            # и подмассив [j, j'-1] будет короче, чем [queue[-1], j'-1].
            while queue and prefix[j] <= prefix[queue[-1]]:
                queue.pop()

            # Добавляем текущий индекс в очередь
            queue.append(j)

        # Если нашли валидный подмассив — возвращаем длину, иначе -1
        return min_length if min_length != float("inf") else -1


def main():
    """Тест-кейсы для задачи Shortest Subarray with Sum at Least K."""
    solution = Solution()

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ЗАДАЧИ SHORTEST SUBARRAY WITH SUM AT LEAST K")
    print("=" * 60)

    # Тест 1: Минимальный случай
    nums = [1]
    k = 1
    result = solution.shortestSubarray(nums, k)
    expected = 1
    print(f"\nТест 1: nums = {nums}, k = {k}")
    print(f"Результат: {result}")
    assert result == expected, (
        f"Тест 1 провален! Ожидалось {expected}, получено {result}"
    )
    print("✓ Пройден")

    # Тест 2: Недостаточная сумма
    nums = [1, 2]
    k = 4
    result = solution.shortestSubarray(nums, k)
    expected = -1
    print(f"\nТест 2: nums = {nums}, k = {k} (сумма недостаточна)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 2 провален!"
    print("✓ Пройден")

    # Тест 3: Стандартный случай с отрицательным числом
    nums = [2, -1, 2]
    k = 3
    result = solution.shortestSubarray(nums, k)
    expected = 3
    print(f"\nТест 3: nums = {nums}, k = {k} (с отрицательным числом)")
    print(f"Результат: {result} (подмассив [2, -1, 2] = 3)")
    assert result == expected, f"Тест 3 провален!"
    print("✓ Пройден")

    # Тест 4: Короткий подмассив в середине
    nums = [2, -1, 2, 1]
    k = 3
    result = solution.shortestSubarray(nums, k)
    expected = 2
    print(f"\nТест 4: nums = {nums}, k = {k}")
    print(f"Результат: {result} (подмассив [2, 1] = 3)")
    assert result == expected, f"Тест 4 провален!"
    print("✓ Пройден")

    # Тест 5: Все положительные числа
    nums = [1, 2, 3, 4, 5]
    k = 5
    result = solution.shortestSubarray(nums, k)
    expected = 2
    print(f"\nТест 5: nums = {nums}, k = {k} (все положительные)")
    print(f"Результат: {result} (подмассив [2, 3] или [5])")
    assert result == expected, f"Тест 5 провален!"
    print("✓ Пройден")

    # Тест 6: Отрицательные числа в начале
    nums = [-1, -2, 5, 3]
    k = 5
    result = solution.shortestSubarray(nums, k)
    expected = 2
    print(f"\nТест 6: nums = {nums}, k = {k} (отрицательные в начале)")
    print(f"Результат: {result} (подмассив [5, 3] = 8)")
    assert result == expected, f"Тест 6 провален!"
    print("✓ Пройден")

    # Тест 7: Большой массив (проверка производительности)
    import random

    random.seed(42)
    nums = [random.randint(-100000, 100000) for _ in range(10000)]
    k = 1000000
    result = solution.shortestSubarray(nums, k)
    print(f"\nТест 7: случайный массив из 10000 элементов, k = {k}")
    print(f"Результат: {result}")
    # Проверяем корректность, если результат найден
    if result != -1:
        # Находим подмассив и проверяем его сумму
        found = False
        for i in range(len(nums) - result + 1):
            if sum(nums[i : i + result]) >= k:
                found = True
                break
        assert found, f"Тест 7: найденный подмассив не имеет сумму >= {k}!"
    print("✓ Пройден")

    print("\n" + "=" * 60)
    print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО! ✓")
    print("=" * 60)


if __name__ == "__main__":
    main()
