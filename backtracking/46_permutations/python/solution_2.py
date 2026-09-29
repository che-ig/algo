"""
Метод вставки (Insertion Method)
Идея: начинаем с одной перестановки [nums[0]], затем для каждого следующего элемента вставляем его во все возможные позиции каждой существующей перестановки.
"""


class SolutionIterative:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        Возвращает все возможные перестановки массива.
        Использует итеративный метод вставки.
        """
        if not nums:
            return []

        # Начинаем с одной перестановки первого элемента
        result = [[nums[0]]]

        # Для каждого следующего элемента
        for i in range(1, len(nums)):
            new_result = []
            # Для каждой существующей перестановки
            for perm in result:
                # Вставляем nums[i] во все возможные позиции
                for j in range(len(perm) + 1):
                    # Создаём новую перестановку с вставленным элементом
                    new_perm = perm[:j] + [nums[i]] + perm[j:]
                    new_result.append(new_perm)
            result = new_result

        return result


def main_iterative():
    """Тест-кейсы для итеративного решения."""
    solution = SolutionIterative()

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ИТЕРАТИВНОГО РЕШЕНИЯ (МЕТОД ВСТАВКИ)")
    print("=" * 60)

    # Тест 1: Стандартный случай
    nums = [1, 2, 3]
    result = solution.permute(nums)
    print(f"\nТест 1: nums = {nums}")
    print(f"Количество перестановок: {len(result)}")
    assert len(result) == 6, f"Тест 1 провален!"
    print("✓ Пройден")

    # Тест 2: Два элемента
    nums = [0, 1]
    result = solution.permute(nums)
    print(f"\nТест 2: nums = {nums}")
    print(f"Количество перестановок: {len(result)}")
    assert len(result) == 2, f"Тест 2 провален!"
    print("✓ Пройден")

    # Тест 3: Один элемент
    nums = [1]
    result = solution.permute(nums)
    print(f"\nТест 3: nums = {nums}")
    print(f"Количество перестановок: {len(result)}")
    assert len(result) == 1, f"Тест 3 провален!"
    print("✓ Пройден")

    # Тест 4: Максимальная длина
    nums = [1, 2, 3, 4, 5, 6]
    result = solution.permute(nums)
    print(f"\nТест 4: nums = {nums} (максимальная длина)")
    print(f"Количество перестановок: {len(result)}")
    assert len(result) == 720, f"Тест 4 провален!"
    print("✓ Пройден")

    print("\n" + "=" * 60)
    print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО! ✓")
    print("=" * 60)


if __name__ == "__main__":
    main_iterative()
