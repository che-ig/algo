"""
Алгоритм Хипа (Heap's Algorithm) — итеративная версия
Алгоритм Хипа — это классический алгоритм для генерации перестановок, который минимизирует количество перестановок (swap'ов).
"""


class SolutionHeap:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        Возвращает все возможные перестановки массива.
        Использует итеративную версию алгоритма Хипа.
        """
        if not nums:
            return []

        result = []
        n = len(nums)

        # Массив для отслеживания количества swap'ов для каждого уровня
        c = [0] * n

        # Добавляем начальную перестановку
        result.append(nums[:])

        i = 0
        while i < n:
            if c[i] < i:
                # Если i чётное, меняем первый и последний элементы
                # Если i нечётное, меняем i-й и последний элементы
                if i % 2 == 0:
                    nums[0], nums[i] = nums[i], nums[0]
                else:
                    nums[c[i]], nums[i] = nums[i], nums[c[i]]

                # Добавляем новую перестановку
                result.append(nums[:])

                # Увеличиваем счётчик для текущего уровня
                c[i] += 1
                i = 0  # Возвращаемся к началу
            else:
                # Сбрасываем счётчик и переходим к следующему уровню
                c[i] = 0
                i += 1

        return result


def main_heap():
    """Тест-кейсы для алгоритма Хипа."""
    solution = SolutionHeap()

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ АЛГОРИТМА ХИПА (ИТЕРАТИВНЫЙ)")
    print("=" * 60)

    # Тест 1: Стандартный случай
    nums = [1, 2, 3]
    result = solution.permute(nums)
    print(f"\nТест 1: nums = {nums}")
    print(f"Количество перестановок: {len(result)}")
    assert len(result) == 6, f"Тест 1 провален!"
    print("✓ Пройден")

    # Тест 2: Максимальная длина
    nums = [1, 2, 3, 4, 5, 6]
    result = solution.permute(nums)
    print(f"\nТест 2: nums = {nums} (максимальная длина)")
    print(f"Количество перестановок: {len(result)}")
    assert len(result) == 720, f"Тест 2 провален!"
    print("✓ Пройден")

    print("\n" + "=" * 60)
    print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО! ✓")
    print("=" * 60)


if __name__ == "__main__":
    main_heap()
