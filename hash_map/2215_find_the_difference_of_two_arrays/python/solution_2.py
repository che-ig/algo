class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        """
        Альтернативное решение через явную проверку элементов.
        """
        # Создаём множества для быстрого поиска
        set1 = set(nums1)
        set2 = set(nums2)

        # Находим элементы nums1, которых нет в nums2
        diff1 = []
        for num in set1:
            if num not in set2:
                diff1.append(num)

        # Находим элементы nums2, которых нет в nums1
        diff2 = []
        for num in set2:
            if num not in set1:
                diff2.append(num)

        return [diff1, diff2]
