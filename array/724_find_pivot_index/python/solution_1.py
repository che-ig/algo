class Solution:
    # time: O(n)
    # mem(доп): O(1)
    def pivotIndex(self, nums: list[int]) -> int:
        # сумма всех элементов массива nums
        numsSum = sum(nums)

        # текущая сумма всех элементов слева
        leftSum = 0
        for i, num in enumerate(nums):
            # rightSum - сумма элементов справа
            # 0 1 2 3 4 5
            #     i
            # если i = 2, то leftSum = 0 + 1
            # rightSum = 3 + 4 + 5
            rightSum = numsSum - leftSum - num
            if leftSum == rightSum:
                return i
            leftSum += num
        return -1
