class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        num_rows = len(grid)
        num_cols = len(grid[0])
        max_area = 0

        def dfs(row: int, col: int) -> int:
            """
            Рекурсивно обходит остров и возвращает его площадь.
            Попутно "затапливает" остров (меняет 1 на 0),
            чтобы не посчитать клетки дважды.
            """
            # Базовый случай: выход за границы или вода (0)
            if (
                row < 0
                or row >= num_rows
                or col < 0
                or col >= num_cols
                or grid[row][col] == 0
            ):
                return 0

            # "Затапливаем" текущую клетку (помечаем как посещенную)
            grid[row][col] = 0

            # Площадь = 1 (текущая клетка) + площади всех 4 соседей
            area = 1
            area += dfs(row + 1, col)  # вниз
            area += dfs(row - 1, col)  # вверх
            area += dfs(row, col + 1)  # вправо
            area += dfs(row, col - 1)  # влево

            return area

        # Проходим по всей сетке
        for row in range(num_rows):
            for col in range(num_cols):
                # Если нашли землю, запускаем поиск острова
                if grid[row][col] == 1:
                    current_area = dfs(row, col)
                    max_area = max(max_area, current_area)

        return max_area


class Solution_2:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        """
        Находит максимальную площадь острова в бинарной матрице.
        Использует итеративный DFS с явным стеком и множеством visited.
        """
        if not grid or not grid[0]:
            return 0

        num_rows = len(grid)
        num_cols = len(grid[0])

        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs_iterative(start_row: int, start_col: int) -> int:
            """
            Итеративно обходит остров и возвращает его площадь.
            """
            # Инициализируем стек стартовой клеткой
            stack = [(start_row, start_col)]
            visited.add((start_row, start_col))  # Помечаем сразу при добавлении
            area = 0

            while stack:
                row, col = stack.pop()
                area += 1  # Считаем извлечённую клетку

                # Проверяем всех 4 соседей
                for row_offset, col_offset in directions:
                    neighbor_row = row + row_offset
                    neighbor_col = col + col_offset

                    # Если сосед в границах, это земля и ещё не посещён
                    if (
                        0 <= neighbor_row < num_rows
                        and 0 <= neighbor_col < num_cols
                        and grid[neighbor_row][neighbor_col] == 1
                        and (neighbor_row, neighbor_col) not in visited
                    ):
                        visited.add((neighbor_row, neighbor_col))  # Помечаем сразу
                        stack.append((neighbor_row, neighbor_col))

            return area

        max_area = 0
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    current_area = dfs_iterative(row, col)
                    max_area = max(max_area, current_area)

        return max_area
