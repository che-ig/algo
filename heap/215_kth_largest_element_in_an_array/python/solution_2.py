import random

"""
Quick Select (алгоритм Хоара) — O(n)
Идея: модификация быстрой сортировки. Выбираем опорный элемент (pivot), разбиваем массив на три части: меньше pivot, равные pivot, больше pivot. Рекурсивно ищем только в нужной части.
"""


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # k-й наибольший = (n-k)-й наименьший в отсортированном порядке
        target_index = len(nums) - k

        def quick_select(left: int, right: int) -> int:
            # Выбираем случайный опорный элемент для защиты от худшего случая
            pivot_idx = random.randint(left, right)
            pivot = nums[pivot_idx]

            # Перемещаем pivot в конец
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

            # Partition: все элементы < pivot идут влево
            store_idx = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_idx], nums[i] = nums[i], nums[store_idx]
                    store_idx += 1

            # Возвращаем pivot на его итоговое место
            nums[store_idx], nums[right] = nums[right], nums[store_idx]

            # Проверяем, нашли ли мы нужную позицию
            if store_idx == target_index:
                return nums[store_idx]
            elif store_idx < target_index:
                # Искомый элемент справа от pivot
                return quick_select(store_idx + 1, right)
            else:
                # Искомый элемент слева от pivot
                return quick_select(left, store_idx - 1)

        return quick_select(0, len(nums) - 1)
