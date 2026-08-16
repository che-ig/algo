class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        # ── База: первый столбец ──
        # Сюда можно попасть только спускаясь вниз, поэтому путей — 1,
        # но встретив препятствие, дальше по столбцу пути обрываются (break)
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1

        # ── База: первая строка ──
        # Симметрично: только движемся вправо, до первого препятствия
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1

        # ── Основная часть: сама рекуррентность ──
        # dp[i][j] = сверху + слева; препятствие остаётся нулём
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0  # клетка закрыта
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]
