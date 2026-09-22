class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        num_rows = len(grid)
        num_cols = len(grid[0])
        islands_count = 0

        def dfs(row, col):
            # Базовый случай: выход за границы или вода/уже посещено
            if (
                row < 0
                or row >= num_rows
                or col < 0
                or col >= num_cols
                or grid[row][col] == "0"
            ):
                return

            # Помечаем текущую клетку как посещённую (превращаем в воду)
            grid[row][col] = "0"

            # Рекурсивно обходим всех 4 соседей
            dfs(row + 1, col)  # сосед снизу
            dfs(row - 1, col)  # сосед сверху
            dfs(row, col + 1)  # сосед справа
            dfs(row, col - 1)  # сосед слева

        # Проходим по каждой клетке сетки
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == "1":
                    # Нашли новый остров
                    islands_count += 1
                    # "Закрашиваем" весь остров через DFS
                    dfs(row, col)

        return islands_count
