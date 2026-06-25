class NumArray:
    # time: O(n)
    # mem: O(n)
    def __init__(self, nums: list[int]):
        # делаем префиксный массив
        # [1, 2, 3] -> [0, 1, 3, 6]
        prefix_sum = [
            0,
        ]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        self.prefix_sum = prefix_sum

    # time: O(1)
    # mem: O(1)
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
