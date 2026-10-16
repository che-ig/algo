class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        """
        Решение за O(log n) через бинарный поиск.

        Используем два бинарных поиска:
        1. Найти индекс первого числа >= 0 (это количество отрицательных)
        2. Найти индекс первого числа > 0 (вычесть из n — это количество положительных)
        """
        n = len(nums)

        # === Бинарный поиск 1: количество отрицательных ===
        # Ищем индекс первого числа >= 0
        # Все числа левее этого индекса — отрицательные
        neg_count = self._lower_bound(nums, 0)

        # === Бинарный поиск 2: количество положительных ===
        # Ищем индекс первого числа > 0
        # Все числа правее этого индекса (включая его) — положительные
        pos_start = self._upper_bound(nums, 0)
        pos_count = n - pos_start

        return max(neg_count, pos_count)

    def _lower_bound(self, nums: list[int], target: int) -> int:
        """
        Возвращает индекс первого элемента >= target.
        Аналог bisect_left из стандартной библиотеки.
        """
        left = 0
        right = len(nums)

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < target:
                # Искомая позиция правее mid
                left = mid + 1
            else:
                # nums[mid] >= target, ищем левее (включая mid)
                right = mid

        return left

    def _upper_bound(self, nums: list[int], target: int) -> int:
        """
        Возвращает индекс первого элемента > target.
        Аналог bisect_right из стандартной библиотеки.
        """
        left = 0
        right = len(nums)

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] <= target:
                # Искомая позиция правее mid
                left = mid + 1
            else:
                # nums[mid] > target, ищем левее (включая mid)
                right = mid

        return left
