class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        """
        Возвращает массив, где answer[i] = |leftSum[i] - rightSum[i]|.

        Использует трюк: rightSum[i] = total_sum - leftSum[i] - nums[i].
        Поэтому нужно поддерживать только left_sum при проходе слева направо.
        """
        # Считаем общую сумму всех элементов массива один раз.
        # Это позволит нам вычислять right_sum "на лету" без второго массива.
        total_sum = sum(nums)

        # left_sum — сумма элементов строго слева от текущего индекса i.
        # Инициализируем 0, потому что слева от первого элемента (i=0) ничего нет.
        left_sum = 0

        # Результирующий массив той же длины, что и nums
        answer = []

        # Проходим по массиву слева направо
        for i in range(len(nums)):
            # Вычисляем right_sum по формуле:
            # total_sum = left_sum + nums[i] + right_sum
            # => right_sum = total_sum - left_sum - nums[i]
            right_sum = total_sum - left_sum - nums[i]

            # Добавляем модуль разности в результат
            answer.append(abs(left_sum - right_sum))

            # Обновляем left_sum для СЛЕДУЮЩЕЙ итерации:
            # добавляем текущий элемент, так как для i+1 он будет "слева"
            left_sum += nums[i]

        return answer


def main():
    """Тест-кейсы для задачи Left and Right Sum Differences."""
    solution = Solution()

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ЗАДАЧИ LEFT AND RIGHT SUM DIFFERENCES")
    print("=" * 60)

    # Тест 1: Стандартный случай из примера LeetCode
    nums = [10, 4, 8, 3]
    result = solution.leftRightDifference(nums)
    expected = [15, 1, 11, 22]
    print(f"\nТест 1: nums = {nums}")
    print(f"Результат: {result}")
    print(f"  leftSum  = [0, 10, 14, 22]")
    print(f"  rightSum = [15, 11, 3, 0]")
    assert result == expected, (
        f"Тест 1 провален! Ожидалось {expected}, получено {result}"
    )
    print("✓ Пройден")

    # Тест 2: Один элемент
    nums = [1]
    result = solution.leftRightDifference(nums)
    expected = [0]
    print(f"\nТест 2: nums = {nums} (один элемент)")
    print(f"Результат: {result} (left=0, right=0, |0-0|=0)")
    assert result == expected, f"Тест 2 провален!"
    print("✓ Пройден")

    # Тест 3: Симметричный массив
    nums = [1, 2, 3, 2, 1]
    result = solution.leftRightDifference(nums)
    # leftSum  = [0, 1, 3, 6, 8]
    # rightSum = [8, 6, 3, 1, 0]
    # answer   = [8, 5, 0, 5, 8]
    expected = [8, 5, 0, 5, 8]
    print(f"\nТест 3: nums = {nums} (симметричный)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 3 провален!"
    print("✓ Пройден")

    # Тест 4: Два элемента
    nums = [5, 10]
    result = solution.leftRightDifference(nums)
    # leftSum  = [0, 5]
    # rightSum = [10, 0]
    # answer   = [10, 5]
    expected = [10, 5]
    print(f"\nТест 4: nums = {nums} (два элемента)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 4 провален!"
    print("✓ Пройден")

    # Тест 5: Все элементы одинаковые
    nums = [3, 3, 3, 3]
    result = solution.leftRightDifference(nums)
    # leftSum  = [0, 3, 6, 9]
    # rightSum = [9, 6, 3, 0]
    # answer   = [9, 3, 3, 9]
    expected = [9, 3, 3, 9]
    print(f"\nТест 5: nums = {nums} (все одинаковые)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 5 провален!"
    print("✓ Пройден")

    # Тест 6: Возрастающая последовательность
    nums = [1, 2, 3, 4, 5]
    result = solution.leftRightDifference(nums)
    # leftSum  = [0, 1, 3, 6, 10]
    # rightSum = [14, 12, 9, 5, 0]
    # answer   = [14, 11, 6, 1, 10]
    expected = [14, 11, 6, 1, 10]
    print(f"\nТест 6: nums = {nums} (возрастающая)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 6 провален!"
    print("✓ Пройден")

    # Тест 7: Большой массив (проверка производительности)
    nums = list(range(1, 1001))  # [1, 2, ..., 1000]
    result = solution.leftRightDifference(nums)
    # Проверяем первый и последний элементы
    # Для i=0: left=0, right=sum(2..1000)=500499, |0-500499|=500499
    # Для i=999: left=sum(1..999)=499500, right=0, |499500-0|=499500
    assert result[0] == 500499, f"Тест 7: ошибка на первом элементе!"
    assert result[-1] == 499500, f"Тест 7: ошибка на последнем элементе!"
    print(f"\nТест 7: nums = [1..1000] (большой массив)")
    print(f"Первый элемент: {result[0]}, последний: {result[-1]}")
    print("✓ Пройден")

    print("\n" + "=" * 60)
    print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО! ✓")
    print("=" * 60)


if __name__ == "__main__":
    main()
