import random


class Solution:
    # выбираем pivot рандомно, чтобы улучшить время
    # быстрой сортировки
    # Note: l - включительно, r - не включительно
    def getPivot(self, arr: list[int], l: int, r: int):
        # random.randint выбирает рандомное число между границами
        # границы включены
        pivotIdx = random.randint(l, r - 1)
        pivot = arr[pivotIdx]
        return pivot, pivotIdx

    # time: O(rIdx - lIdx)
    # mem:  O(1)
    # Note: [lIdx, rIdx) - полуинтервал, lIdx включаем, а rIdx - нет
    def partition(self, arr: list[int], lIdx: int, rIdx: int) -> int:
        # находим pivot
        pivot, pivotIdx = self.getPivot(arr, lIdx, rIdx)

        # ставим pivot на самое левое место (pivot не будет
        # учавствовать в перестановке элементов т е его позиция
        # после while не изменится, для этого делаем l = lIdx + 1)

        # r = rIdx - 1 делаем чтобы r указывал на последний элемент
        # (rIdx - может указывать на не существующий элемент)
        arr[lIdx], arr[pivotIdx] = arr[pivotIdx], arr[lIdx]
        l, r = lIdx + 1, rIdx - 1

        # делим массив на 2 партиции (где элементы)
        # 1 part - элементы <= pivot
        # 2 part - элементы >= pivot
        while l <= r:
            if arr[l] < pivot:
                l += 1
            elif arr[r] > pivot:
                r -= 1
            else:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        # ставим pivot на нужное место
        # это будет гарантированно правильнам местом в отсортированном
        # массиве т е индекс где стоит pivot (r) можно будет
        # выкинуть из рекурсии (не запускать для него сного qsort)
        arr[lIdx], arr[r] = arr[r], arr[lIdx]
        return r

    # time avg:      O(n log n)
    # mem (доп) avg: O(log n)
    def qsort(self, nums: list[int], l: int, r: int) -> list[int]:
        if l >= r:
            return nums
        # разделяем массив на 2 части
        pivotIdx = self.partition(nums, l, r)
        # рекурсивно сортируем 1 part (pivotIdx не включаем т к правая
        # граница идет не включительно)
        self.qsort(nums, l, pivotIdx)
        # рекурсивно сортируем 2 part (pivotIdx не включаем)
        self.qsort(nums, pivotIdx + 1, r)
        return nums

    # Quick sort
    # time avg:       O(n log n)
    # time wors:      O(n ** 2)
    # mem (доп) avg:  O(log n)
    # mem (доп) wors: O(N)
    def sortArray(self, nums: list[int]) -> list[int]:
        return self.qsort(nums, 0, len(nums))
