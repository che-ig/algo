"""
Иногда интервьюеры говорят: "А если бы массивы были огромными и не помещались в память? Как бы вы решили без хеш-таблиц?". Тогда используется сортировка.
"""


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()

        i, j = 0, 0
        result = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                # Нашли общий элемент
                # Добавляем его, только если он не является дубликатом последнего добавленного
                if not result or result[-1] != nums1[i]:
                    result.append(nums1[i])
                i += 1
                j += 1

        return result
