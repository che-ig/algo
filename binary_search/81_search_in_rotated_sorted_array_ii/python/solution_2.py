class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        n = len(nums)

        # ===== ЭТАП 1: Находим индекс минимума с помощью good =====
        def good_min(idx: int) -> bool:
            """
            Проверяет, находится ли элемент на позиции idx в ПРАВОЙ
            (второй отсортированной) части массива.

            В циклически сдвинутом массиве элементы правой части
            всегда <= последнего элемента nums[n-1].
            Элементы левой части (до точки поворота) >= nums[n-1].

            Возвращает True, если nums[idx] <= nums[n-1]
            (то есть мы в правой части или на границе).
            """
            return nums[idx] <= nums[n - 1]

        # Бинарный поиск ПЕРВОГО индекса, где good_min = True
        # Это и есть индекс минимального элемента (точка поворота)
        lo, hi = 0, n - 1
        min_idx = n - 1  # По умолчанию — последний элемент

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            # Обработка дубликатов: если не можем определить,
            # в какой части находимся, сужаем с обоих концов
            if nums[lo] == nums[mid] == nums[hi]:
                # Проверяем, не является ли текущий край искомым
                if nums[lo] == target:
                    return True
                lo += 1
                hi -= 1
            elif good_min(mid):
                # Мы в правой части — минимум здесь или левее
                min_idx = mid
                hi = mid - 1
            else:
                # Мы в левой части — минимум правее
                lo = mid + 1

        # ===== ЭТАП 2: Бинарный поиск target в нужной половине =====
        # Теперь массив фактически разбит на две отсортированные части:
        # [min_idx ... n-1] и [0 ... min_idx-1]

        # Определяем, в какой части искать
        if target >= nums[min_idx] and target <= nums[n - 1]:
            lo, hi = min_idx, n - 1  # Правая часть
        else:
            lo, hi = 0, min_idx - 1  # Левая часть

        # Обычный бинарный поиск по отсортированной части
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return False
