class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        dp = nums[:]  # dp[i] — лучшая сумма подмассива, кончающегося в i
        for i in range(1, len(nums)):
            # либо сам элемент, либо элемент + лучший предыдущий
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
        # ответ — максимум по всем концам подмассивов
        return max(dp)
