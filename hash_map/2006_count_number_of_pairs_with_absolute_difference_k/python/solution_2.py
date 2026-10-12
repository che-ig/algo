from collections import Counter


class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        """
        Универсальное решение через Counter.
        Работает при любых значениях nums[i].
        """
        # Считаем частоты всех элементов
        count = Counter(nums)

        pairs = 0
        # Для каждого уникального числа x проверяем, есть ли x + k
        for x in count:
            if x + k in count:
                # Умножаем количество вхождений x на количество вхождений x + k
                pairs += count[x] * count[x + k]

        return pairs
