import heapq
from typing import List


class Solution:
    # time: O(k + (n - k) log n)
    # mem:  O(k)
    # Note: кучей не оптимально
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # создаем кучу на минимум размером k
        # в куче на минимум будем хранить максимальные элементы
        # сама куча на минимум чтобы потом без лишних удалений
        # найти k-ый наибольший. в случаее кучи на минимум
        # получить этот элемент можно сразу
        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            # кладем в кучу только элементы которые больше самого
            # минимального
            if num <= heap[0]:
                # пропускаем равные элементы т к ничего не изменится
                # т е если мы не зайдем в if то скачала удалим
                # heap[0], а потом добавим num, но heap[0] == num
                continue
            # удаляем их кучи минимальный
            heapq.heappop(heap)
            heapq.heappush(heap, num)

        # достаем минимальный элемент из кучи
        return heap[0]


# Оптимизация: heapq.heapreplace
# Можно объединить push и pop в одну операцию — это быстрее:


class Solution_1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Берём первые k элементов и строим из них кучу за O(k)
        min_heap = nums[:k]
        heapq.heapify(min_heap)

        # Проходим по оставшимся элементам
        for num in nums[k:]:
            # Если текущий элемент больше минимума в куче — заменяем
            if num > min_heap[0]:
                heapq.heapreplace(min_heap, num)

        return min_heap[0]
