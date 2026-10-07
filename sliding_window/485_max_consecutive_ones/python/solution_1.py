class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        """
        Возвращает максимальное количество подряд идущих единиц в бинарном массиве.
        """
        max_count = 0
        current_count = 0

        for num in nums:
            if num == 1:
                current_count += 1
            else:
                # Серия прервалась — обновляем максимум и сбрасываем счётчик
                max_count = max(max_count, current_count)
                current_count = 0

        # ВАЖНО: финальное обновление на случай, если массив заканчивается на 1
        max_count = max(max_count, current_count)

        return max_count


class Solution_2:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        """
        Возвращает максимальное количество подряд идущих единиц в бинарном массиве.
        """
        max_count = 0
        current_count = 0

        for num in nums:
            if num == 1:
                current_count += 1
            else:
                current_count = 0

            max_count = max(max_count, current_count)

        return max_count


def main():
    """Тест-кейсы для задачи Max Consecutive Ones."""
    solution = Solution()

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ЗАДАЧИ MAX CONSECUTIVE ONES")
    print("=" * 60)

    # Тест 1: Стандартный случай из примера LeetCode
    nums = [1, 1, 0, 1, 1, 1]
    result = solution.findMaxConsecutiveOnes(nums)
    expected = 3
    print(f"\nТест 1: nums = {nums}")
    print(f"Результат: {result}")
    assert result == expected, (
        f"Тест 1 провален! Ожидалось {expected}, получено {result}"
    )
    print("✓ Пройден")

    # Тест 2: Второй пример из LeetCode
    nums = [1, 0, 1, 1, 0, 1]
    result = solution.findMaxConsecutiveOnes(nums)
    expected = 2
    print(f"\nТест 2: nums = {nums}")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 2 провален!"
    print("✓ Пройден")

    # Тест 3: Все единицы
    nums = [1, 1, 1, 1, 1]
    result = solution.findMaxConsecutiveOnes(nums)
    expected = 5
    print(f"\nТест 3: nums = {nums} (все единицы)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 3 провален!"
    print("✓ Пройден")

    # Тест 4: Все нули
    nums = [0, 0, 0, 0]
    result = solution.findMaxConsecutiveOnes(nums)
    expected = 0
    print(f"\nТест 4: nums = {nums} (все нули)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 4 провален!"
    print("✓ Пройден")

    # Тест 5: Один элемент — единица
    nums = [1]
    result = solution.findMaxConsecutiveOnes(nums)
    expected = 1
    print(f"\nТест 5: nums = {nums} (один элемент)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 5 провален!"
    print("✓ Пройден")

    # Тест 6: Один элемент — ноль
    nums = [0]
    result = solution.findMaxConsecutiveOnes(nums)
    expected = 0
    print(f"\nТест 6: nums = {nums} (один ноль)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 6 провален!"
    print("✓ Пройден")

    # Тест 7: Массив заканчивается на длинную серию единиц
    # (проверяем финальное обновление max_count)
    nums = [0, 0, 1, 1, 1, 1, 1]
    result = solution.findMaxConsecutiveOnes(nums)
    expected = 5
    print(f"\nТест 7: nums = {nums} (массив заканчивается на серию)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 7 провален!"
    print("✓ Пройден")

    # Тест 8: Чередование
    nums = [1, 0, 1, 0, 1, 0, 1]
    result = solution.findMaxConsecutiveOnes(nums)
    expected = 1
    print(f"\nТест 8: nums = {nums} (чередование)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 8 провален!"
    print("✓ Пройден")

    # Тест 9: Большой массив (проверка производительности)
    nums = [1] * 100_000
    result = solution.findMaxConsecutiveOnes(nums)
    expected = 100_000
    print(f"\nТест 9: nums = [1] * 100000 (большой массив)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 9 провален!"
    print("✓ Пройден")

    print("\n" + "=" * 60)
    print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО! ✓")
    print("=" * 60)


if __name__ == "__main__":
    main()
