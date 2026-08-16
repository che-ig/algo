class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # row[j] — мин. сумма пути до клетки (i, j) текущей строки;
        # база: первая строка, суммы накапливаются слева
        row = [0] * n
        row[0] = grid[0][0]
        for j in range(1, n):
            row[j] = row[j - 1] + grid[0][j]

        for i in range(1, m):
            # первый столбец новой строки: прийти можно только сверху
            row[0] += grid[i][0]
            for j in range(1, n):
                # СВЕРХУ: старое row[j] (ещё не перезаписано);
                # СЛЕВА:  новое row[j-1]; берём дешевле + цена клетки
                row[j] = grid[i][j] + min(row[j], row[j - 1])

        return row[n - 1]
