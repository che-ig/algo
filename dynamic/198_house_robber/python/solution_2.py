class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        dp = [[0, 0] for _ in range(n)]

        # Базовые случаи
        dp[0][0] = 0  # не берем первый дом
        dp[0][1] = nums[0]  # берем первый дом

        for i in range(1, n):
            # не берем i-й дом: максимум из того, брали ли мы (i-1)-й или нет
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])

            # берем i-й дом: к dp[i-1][0] (предыдущий не брали) прибавляем nums[i]
            dp[i][1] = dp[i - 1][0] + nums[i]

        return max(dp[n - 1][0], dp[n - 1][1])
