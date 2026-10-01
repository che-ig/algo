from collections import deque

"""
Почему это работает за O(n)?
На первый взгляд кажется, что вложенный while делает алгоритм медленнее. Но ключевое наблюдение:

    Каждый индекс добавляется в deque ровно один раз (в строке dq.append(right))
    Каждый индекс удаляется из deque ровно один раз (либо через pop() справа, либо через popleft() слева)

Значит, общее количество операций над deque — не более 2n, что даёт O(n) в сумме.
Это называется амортизированная сложность: хотя одна итерация может сделать много работы (например, очистить всю очередь), в среднем на итерацию приходится O(1) операций.
Сложность алгоритма

    Время: O(n) — каждый элемент добавляется и удаляется из deque не более одного раза.
    Память: O(k) — deque хранит не более kkk индексов (размер окна).


"""


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """
        Находит максимум в каждом скользящем окне размера k.
        Использует монотонную убывающую очередь (deque).
        """
        # Edge case: если окно размером 1, каждый элемент — свой максимум
        if k == 1:
            return nums[:]

        # deque хранит ИНДЕКСЫ элементов в убывающем порядке их значений.
        # nums[deque[0]] — это максимум текущего окна.
        dq = deque()

        result = []

        for right in range(len(nums)):
            # Правило 1: Удаляем из конца очереди все элементы,
            # которые меньше или равны текущему.
            # Они больше никогда не станут максимумом, пока nums[right] в окне.
            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()

            # Добавляем индекс текущего элемента в конец очереди
            dq.append(right)

            # Правило 2: Удаляем из начала очереди элементы,
            # которые вышли за пределы окна.
            # Окно — это [right - k + 1, right], поэтому элемент с индексом
            # dq[0] вышел, если dq[0] <= right - k
            if dq[0] <= right - k:
                dq.popleft()

            # Начинаем записывать результаты, когда окно полностью сформировалось
            # (right >= k - 1 означает, что мы обработали как минимум k элементов)
            if right >= k - 1:
                result.append(nums[dq[0]])

        return result


def main():
    """Тест-кейсы для задачи Sliding Window Maximum."""
    solution = Solution()

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ЗАДАЧИ SLIDING WINDOW MAXIMUM")
    print("=" * 60)

    # Тест 1: Стандартный случай из примера LeetCode
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result = solution.maxSlidingWindow(nums, k)
    expected = [3, 3, 5, 5, 6, 7]
    print(f"\nТест 1: nums = {nums}, k = {k}")
    print(f"Результат: {result}")
    assert result == expected, (
        f"Тест 1 провален! Ожидалось {expected}, получено {result}"
    )
    print("✓ Пройден")

    # Тест 2: Окно размером 1
    nums = [1]
    k = 1
    result = solution.maxSlidingWindow(nums, k)
    expected = [1]
    print(f"\nТест 2: nums = {nums}, k = {k} (окно = 1)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 2 провален!"
    print("✓ Пройден")

    # Тест 3: Окно равно длине массива
    nums = [1, 2, 3, 4, 5]
    k = 5
    result = solution.maxSlidingWindow(nums, k)
    expected = [5]
    print(f"\nТест 3: nums = {nums}, k = {k} (окно = длина массива)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 3 провален!"
    print("✓ Пройден")

    # Тест 4: Убывающая последовательность
    nums = [5, 4, 3, 2, 1]
    k = 3
    result = solution.maxSlidingWindow(nums, k)
    expected = [5, 4, 3]
    print(f"\nТест 4: nums = {nums}, k = {k} (убывающая)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 4 провален!"
    print("✓ Пройден")

    # Тест 5: Возрастающая последовательность
    nums = [1, 2, 3, 4, 5]
    k = 3
    result = solution.maxSlidingWindow(nums, k)
    expected = [3, 4, 5]
    print(f"\nТест 5: nums = {nums}, k = {k} (возрастающая)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 5 провален!"
    print("✓ Пройден")

    # Тест 6: Все элементы одинаковые
    nums = [7, 7, 7, 7, 7]
    k = 2
    result = solution.maxSlidingWindow(nums, k)
    expected = [7, 7, 7, 7]
    print(f"\nТест 6: nums = {nums}, k = {k} (все одинаковые)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 6 провален!"
    print("✓ Пройден")

    # Тест 7: Отрицательные числа
    nums = [-1, -3, -2, -5, -4]
    k = 2
    result = solution.maxSlidingWindow(nums, k)
    expected = [-1, -2, -2, -4]
    print(f"\nТест 7: nums = {nums}, k = {k} (отрицательные)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 7 провален!"
    print("✓ Пройден")

    # Тест 8: Большой массив (проверка производительности)
    import random

    random.seed(42)
    nums = [random.randint(-10000, 10000) for _ in range(10000)]
    k = 100
    result = solution.maxSlidingWindow(nums, k)
    # Проверяем корректность на нескольких случайных окнах
    for i in range(0, len(nums) - k + 1, 1000):
        expected_max = max(nums[i : i + k])
        assert result[i] == expected_max, f"Ошибка на позиции {i}!"
    print(f"\nТест 8: случайный массив из 10000 элементов, k = {k}")
    print(f"Результат: {len(result)} максимумов")
    print("✓ Пройден")

    print("\n" + "=" * 60)
    print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО! ✓")
    print("=" * 60)


if __name__ == "__main__":
    main()
