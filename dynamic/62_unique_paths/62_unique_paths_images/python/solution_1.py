class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # вся таблица сразу 1: первая строка и столбец — базовые
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                # сверху + слева
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]
