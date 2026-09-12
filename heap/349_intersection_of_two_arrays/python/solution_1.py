class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Преобразуем оба списка в множества и находим их пересечение
        # Оператор & оставляет только общие уникальные элементы
        return list(set(nums1) & set(nums2))


class Solution_2:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Создаем множество из первого массива для поиска за O(1)
        set1 = set(nums1)

        # Используем множество для результата, чтобы гарантировать уникальность
        result_set = set()

        # Проходим по второму массиву
        for num in nums2:
            # Если элемент есть в первом множестве, добавляем его в результат
            if num in set1:
                result_set.add(num)

        # Преобразуем множество обратно в список
        return list(result_set)
