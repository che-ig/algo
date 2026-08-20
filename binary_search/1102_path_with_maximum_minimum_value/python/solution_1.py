from collections import deque


class Solution:
    def maximumMinimumPath(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def can_reach(min_val: int) -> bool:
            """
            Проверяет, можно ли добраться от (0,0) до (m-1,n-1),
            проходя только через клетки со значением >= min_val.

            Args:
                min_val: минимально допустимое значение клетки на пути

            Returns:
                True если путь существует, иначе False
            """
            # Если стартовая или конечная клетка меньше min_val, путь невозможен
            if grid[0][0] < min_val or grid[m - 1][n - 1] < min_val:
                return False

            # BFS для поиска пути
            visited = [[False] * n for _ in range(m)]
            visited[0][0] = True
            queue = deque([(0, 0)])

            # 4 направления движения: вверх, вниз, влево, вправо
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            while queue:
                x, y = queue.popleft()

                # Если дошли до цели — путь найден
                if x == m - 1 and y == n - 1:
                    return True

                # Проверяем всех соседей
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    # Проверяем границы, посещённость и условие min_val
                    if (
                        0 <= nx < m
                        and 0 <= ny < n
                        and not visited[nx][ny]
                        and grid[nx][ny] >= min_val
                    ):
                        visited[nx][ny] = True
                        queue.append((nx, ny))

            # Путь не найден
            return False

        # Диапазон бинарного поиска:
        # lo = минимальное значение в матрице
        # hi = минимальное из значений стартовой и конечной клетки
        # (путь обязательно проходит через них, поэтому минимум не может быть больше)
        lo = min(min(row) for row in grid)
        hi = min(grid[0][0], grid[m - 1][n - 1])

        ans = lo  # По умолчанию — худший возможный ответ

        # Бинарный поиск максимального значения min_val, при котором путь существует
        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if can_reach(mid):
                # Путь с минимумом >= mid существует
                # Запоминаем ответ и пробуем увеличить минимум
                ans = mid
                lo = mid + 1
            else:
                # Путь невозможен, нужно уменьшить требование к минимуму
                hi = mid - 1

        return ans
