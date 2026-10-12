from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        """
        Возвращает количество хороших пар (i, j) где nums[i] == nums[j] и i < j.

        Если число встречается k раз, то количество пар из этих вхождений
        равно C(k, 2) = k * (k - 1) / 2.
        """
        # Считаем частоты каждого числа
        count = Counter(nums)

        total_pairs = 0

        # Для каждого числа с частотой k добавляем k * (k - 1) / 2 пар
        for k in count.values():
            # Формула сочетаний: C(k, 2) = k! / (2! * (k-2)!) = k * (k-1) / 2
            # Например: если число встречается 3 раза, пар = 3 * 2 / 2 = 3
            # Если 4 раза: 4 * 3 / 2 = 6
            total_pairs += k * (k - 1) // 2

        return total_pairs
