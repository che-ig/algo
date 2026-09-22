from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        num_rows = len(grid)
        num_cols = len(grid[0])
        islands_count = 0

        # Смещения для 4 направлений: вниз, вверх, вправо, влево
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(start_row, start_col):
            queue = deque([(start_row, start_col)])
            grid[start_row][start_col] = "0"  # Помечаем стартовую клетку

            while queue:
                curr_row, curr_col = queue.popleft()

                # Проверяем всех 4 соседей
                for row_offset, col_offset in directions:
                    neighbor_row = curr_row + row_offset
                    neighbor_col = curr_col + col_offset

                    # Если сосед в границах и это земля
                    if (
                        0 <= neighbor_row < num_rows
                        and 0 <= neighbor_col < num_cols
                        and grid[neighbor_row][neighbor_col] == "1"
                    ):
                        grid[neighbor_row][neighbor_col] = "0"  # Помечаем сразу
                        queue.append((neighbor_row, neighbor_col))

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == "1":
                    islands_count += 1
                    bfs(row, col)

        return islands_count
