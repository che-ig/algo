import heapq


class Solution:
    def maximumMinimumPath(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # max_score[x][y] — максимальный минимум на пути от (0,0) до (x,y)
        # Инициализируем -1 (ещё не посещали)
        max_score = [[-1] * n for _ in range(m)]
        max_score[0][0] = grid[0][0]

        # Max-heap (в Python min-heap, поэтому храним отрицательные значения)
        # Элементы: (-текущий_минимум, x, y)
        heap = [(-grid[0][0], 0, 0)]

        # 4 направления движения
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while heap:
            # Извлекаем клетку с наибольшим текущим минимумом
            neg_score, x, y = heapq.heappop(heap)
            current_min = -neg_score

            # Если дошли до цели — возвращаем ответ
            # (гарантируется, что это оптимальный путь, т.к. heap даёт максимум)
            if x == m - 1 and y == n - 1:
                return current_min

            # Если мы уже нашли путь до (x,y) с большим минимумом — пропускаем
            if current_min < max_score[x][y]:
                continue

            # Проверяем всех соседей
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    # Новый минимум на пути через (nx, ny) — это минимум
                    # между текущим минимумом и значением клетки (nx, ny)
                    new_min = min(current_min, grid[nx][ny])

                    # Если нашли путь с большим минимумом, чем был раньше — обновляем
                    if new_min > max_score[nx][ny]:
                        max_score[nx][ny] = new_min
                        heapq.heappush(heap, (-new_min, nx, ny))

        return max_score[m - 1][n - 1]
