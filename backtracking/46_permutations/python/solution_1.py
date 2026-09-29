class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        Возвращает все возможные перестановки массива уникальных чисел.
        Использует бэктрекинг с отслеживанием использованных элементов.
        """
        result = []
        current_permutation = []
        used = [False] * len(nums)  # Отслеживаем, какие элементы уже использованы

        def backtrack() -> None:
            """
            Рекурсивно генерирует перестановки.
            """
            # Базовый случай: текущая перестановка содержит все элементы
            if len(current_permutation) == len(nums):
                result.append(current_permutation[:])  # Добавляем копию
                return

            # Пробуем каждый неиспользованный элемент
            for i in range(len(nums)):
                if not used[i]:
                    # 1. Выбираем элемент
                    current_permutation.append(nums[i])
                    used[i] = True

                    # 2. Рекурсивно генерируем остальные позиции
                    backtrack()

                    # 3. Отменяем выбор (backtrack)
                    current_permutation.pop()
                    used[i] = False

        backtrack()
        return result


class SolutionSwap:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        Возвращает все возможные перестановки массива.
        Использует бэктрекинг через swap (перестановку элементов).
        """
        result = []

        def backtrack(start: int) -> None:
            """
            Генерирует перестановки, меняя элементы местами.
            start - индекс позиции, которую нужно заполнить.
            """
            # Базовый случай: все позиции заполнены
            if start == len(nums):
                result.append(nums[:])  # Добавляем копию текущего состояния
                return

            # Пробуем каждый элемент на позиции start
            for i in range(start, len(nums)):
                # 1. Меняем местами элементы на позициях start и i
                nums[start], nums[i] = nums[i], nums[start]

                # 2. Рекурсивно заполняем следующую позицию
                backtrack(start + 1)

                # 3. Отменяем swap (backtrack)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return result


def main_swap():
    """Тест-кейсы для решения через swap."""
    solution = SolutionSwap()

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ РЕШЕНИЯ ЧЕРЕЗ SWAP")
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


def main():
    """Тест-кейсы для задачи Permutations."""
    solution = Solution()

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ РЕШЕНИЯ С БЭКТРЕКИНГОМ")
    print("=" * 60)

    # Тест 1: Стандартный случай из примера LeetCode
    nums = [1, 2, 3]
    result = solution.permute(nums)
    expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    print(f"\nТест 1: nums = {nums}")
    print(f"Количество перестановок: {len(result)}")
    print(f"Ожидаемое количество: {len(expected)}")
    assert len(result) == len(expected), (
        f"Тест 1 провален! Ожидалось {len(expected)}, получено {len(result)}"
    )
    # Проверяем, что все ожидаемые перестановки присутствуют
    assert sorted([sorted(p) for p in result]) == sorted(
        [sorted(p) for p in expected]
    ), "Тест 1 провален!"
    print("✓ Пройден")

    # Тест 2: Два элемента
    nums = [0, 1]
    result = solution.permute(nums)
    expected = [[0, 1], [1, 0]]
    print(f"\nТест 2: nums = {nums}")
    print(f"Количество перестановок: {len(result)}")
    assert len(result) == 2, f"Тест 2 провален!"
    assert sorted([sorted(p) for p in result]) == sorted(
        [sorted(p) for p in expected]
    ), "Тест 2 провален!"
    print("✓ Пройден")

    # Тест 3: Один элемент
    nums = [1]
    result = solution.permute(nums)
    expected = [[1]]
    print(f"\nТест 3: nums = {nums}")
    print(f"Количество перестановок: {len(result)}")
    assert len(result) == 1, f"Тест 3 провален!"
    assert result == expected, "Тест 3 провален!"
    print("✓ Пройден")

    # Тест 4: Отрицательные числа
    nums = [-1, 0, 1]
    result = solution.permute(nums)
    print(f"\nТест 4: nums = {nums} (с отрицательными числами)")
    print(f"Количество перестановок: {len(result)}")
    # Для 3 элементов должно быть 3! = 6 перестановок
    assert len(result) == 6, f"Тест 4 провален! Ожидалось 6, получено {len(result)}"
    print("✓ Пройден")

    # Тест 5: Максимальная длина (6 элементов)
    nums = [1, 2, 3, 4, 5, 6]
    result = solution.permute(nums)
    print(f"\nТест 5: nums = {nums} (максимальная длина)")
    print(f"Количество перестановок: {len(result)}")
    # Для 6 элементов должно быть 6! = 720 перестановок
    assert len(result) == 720, f"Тест 5 провален! Ожидалось 720, получено {len(result)}"
    print("✓ Пройден")

    print("\n" + "=" * 60)
    print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО! ✓")
    print("=" * 60)


if __name__ == "__main__":
    main_swap()
    main()
