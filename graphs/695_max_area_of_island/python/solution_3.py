from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        """
        Находит максимальную площадь острова в бинарной матрице.
        Использует BFS с очередью и множеством visited.
        """
        if not grid or not grid[0]:
            return 0

        num_rows = len(grid)
        num_cols = len(grid[0])

        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(start_row: int, start_col: int) -> int:
            """
            Обходит остров в ширину и возвращает его площадь.
            """
            queue = deque([(start_row, start_col)])
            visited.add((start_row, start_col))  # Помечаем сразу при добавлении
            area = 0

            while queue:
                row, col = queue.popleft()
                area += 1  # Считаем извлечённую клетку

                for row_offset, col_offset in directions:
                    neighbor_row = row + row_offset
                    neighbor_col = col + col_offset

                    if (
                        0 <= neighbor_row < num_rows
                        and 0 <= neighbor_col < num_cols
                        and grid[neighbor_row][neighbor_col] == 1
                        and (neighbor_row, neighbor_col) not in visited
                    ):
                        visited.add((neighbor_row, neighbor_col))
                        queue.append((neighbor_row, neighbor_col))

            return area

        max_area = 0
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    current_area = bfs(row, col)
                    max_area = max(max_area, current_area)

        return max_area
