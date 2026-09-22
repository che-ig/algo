from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        """
        Находит длину кратчайшего пути от (0,0) до (n-1, n-1).
        Использует алгоритм Ли с восстановлением пути через обратный проход.
        """
        n = len(grid)

        # Быстрая проверка стартовой и конечной клеток
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        # 8 направлений обхода
        # (-1, -1), (-1, 0), (-1, 1),
        # (0, -1),           (0, 1),
        # (1, -1),  (1, 0),  (1, 1)

        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        # Массив для хранения "родителя" каждой клетки.
        # parent[row][col] = (parent_row, parent_col) — откуда мы пришли в эту клетку.
        # Инициализируем None — клетка ещё не посещена.
        parent = [[None] * n for _ in range(n)]
        parent[0][0] = (-1, -1)  # Стартовая клетка не имеет родителя (маркер)

        # Очередь хранит только координаты (длину считаем через parent)
        queue = deque([(0, 0)])

        # Шаг 1: BFS (волновой алгоритм Ли)
        found = False
        while queue:
            curr_row, curr_col = queue.popleft()

            # Если достигли цели — останавливаемся
            if curr_row == n - 1 and curr_col == n - 1:
                found = True
                break

            # Проверяем всех 8 соседей
            for row_offset, col_offset in directions:
                neighbor_row = curr_row + row_offset
                neighbor_col = curr_col + col_offset

                if (
                    0 <= neighbor_row < n
                    and 0 <= neighbor_col < n
                    and grid[neighbor_row][neighbor_col] == 0
                    and parent[neighbor_row][neighbor_col] is None
                ):
                    # Запоминаем родителя и добавляем в очередь
                    parent[neighbor_row][neighbor_col] = (curr_row, curr_col)
                    queue.append((neighbor_row, neighbor_col))

        # Если не достигли цели — пути нет
        if not found:
            return -1

        # Шаг 2: Обратный проход — восстанавливаем путь от цели к старту
        path = []
        curr = (n - 1, n - 1)

        while curr != (-1, -1):  # Идём пока не дойдём до маркера старта
            path.append(curr)
            curr = parent[curr[0]][curr[1]]  # Переходим к родителю

        # path сейчас идёт от цели к старту, разворачиваем его
        path.reverse()

        # Длина пути = количество клеток в пути
        return len(path)
