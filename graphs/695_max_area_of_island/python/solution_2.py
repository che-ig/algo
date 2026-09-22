class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        num_rows = len(grid)
        num_cols = len(grid[0])
        max_area = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs_iterative(start_row: int, start_col: int) -> int:
            """Итеративный подсчет площади острова с помощью стека."""
            stack = [(start_row, start_col)]
            grid[start_row][start_col] = 0  # Помечаем сразу!
            area = 0

            while stack:
                row, col = stack.pop()
                area += 1  # Считаем извлеченную клетку

                for row_offset, col_offset in directions:
                    neighbor_row = row + row_offset
                    neighbor_col = col + col_offset

                    # Если сосед в границах и это земля
                    if (
                        0 <= neighbor_row < num_rows
                        and 0 <= neighbor_col < num_cols
                        and grid[neighbor_row][neighbor_col] == 1
                    ):
                        grid[neighbor_row][neighbor_col] = 0  # Помечаем сразу
                        stack.append((neighbor_row, neighbor_col))

            return area

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1:
                    max_area = max(max_area, dfs_iterative(row, col))

        return max_area
