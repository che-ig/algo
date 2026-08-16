class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # row[j] — число путей до клетки (i, j) ТЕКУЩЕЙ строки;
        # старт: в (0,0) можно стоять ровно 1 способом
        row = [0] * n
        row[0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    # препятствие: через клетку пути не идут
                    row[j] = 0
                elif j > 0:
                    # СВЕРХУ: старое row[j] (ещё не перезаписано в этой строке);
                    # СЛЕВА:  row[j-1] (уже обновлено в этой строке)
                    row[j] += row[j - 1]
                # j == 0 и не препятствие: row[0] не меняем —
                # в первый столбец можно прийти только сверху

        return row[n - 1]
