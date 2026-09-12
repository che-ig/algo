class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        # Сортируем массив по возрастанию
        nums.sort()

        # Суммируем элементы на чётных позициях (0, 2, 4...)
        # Именно они являются минимумами в своих парах
        return sum(nums[::2])
