class Solution:
    # time: O(n)
    # mem: O(1)
    def missingNumber(self, nums: list[int]) -> int:
        # overallSum - сумма чисел от 0 до n включительно
        # n - взято из условия
        overallSum = sum([i for i in range(0, len(nums) + 1)])

        # numsSum - сумма всех элементов массива
        numsSum = sum(nums)

        return overallSum - numsSum
