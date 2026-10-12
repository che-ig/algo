class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        """
        Решает задачу через сортировку.
        Индекс первого вхождения числа в отсортированном массиве
        равен количеству чисел, меньших его.
        """
        # Сортируем копию массива
        sorted_nums = sorted(nums)

        # Для каждого числа запоминаем индекс его ПЕРВОГО вхождения.
        # Все числа левее этого индекса гарантированно меньше.
        first_index = {}
        for i, num in enumerate(sorted_nums):
            if num not in first_index:
                first_index[num] = i

        # Формируем ответ в исходном порядке
        return [first_index[num] for num in nums]
