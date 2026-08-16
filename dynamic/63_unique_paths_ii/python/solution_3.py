class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0  # клетка закрыта
                elif i == 0 and j == 0:
                    dp[i][j] = 1  # старт
                else:
                    if i > 0:
                        dp[i][j] += dp[i - 1][j]  # сверху
                    if j > 0:
                        dp[i][j] += dp[i][j - 1]  # слева

        return dp[m - 1][n - 1]
