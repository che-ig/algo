class Solution:
    # проверяем не выходят ли индексы за границу массива, True - если не выходим
    def good_idx(self, i: int, j: int, board: list[list[str]]) -> bool:
        return 0 <= i < len(board) and 0 <= j < len(board[0])

    # проверяем что крайняя правая клетка
    def is_finish_cell(self, cell, grid: list[list[int]]) -> bool:
        return cell[0] == (len(grid) - 1) and cell[1] == (len(grid[0]) - 1)

    # time: O(n * m), n * m - размер матрицы
    # mem: O(n * m)
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        # True - уже были, False - еще не посещали
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        # определяем возможные шаги из клетки - можно сгенерировать 2 циклами, но я расписал
        steps = [
            [0, 1],  # вправо
            [0, -1],  # влево
            [-1, 0],  # вверх
            [1, 0],  # вниз
            [1, 1],  # вниз, вправо
            [-1, -1],  # вверх, влево
            [-1, 1],  # вверх, вправо
            [1, -1],  # вниз, влево
        ]
        # если клетка начала это "стена", то никуда идти не можем
        if grid[0][0] == 1:
            return -1

        # в очереди храним пару (расстояние до текущей клетки) и координаты клетки
        q = deque([(1, (0, 0))])
        visited[0][0] = True

        # запускаем bfs
        while len(q) > 0:
            path_len, (x, y) = q.popleft()
            # проверяю что дошли до пункта назначения
            if self.is_finish_cell((x, y), grid):
                return path_len
            for step in steps:
                next_x, next_y = x + step[0], y + step[1]
                if not self.good_idx(next_x, next_y, grid):
                    # выходим за границы матрицы
                    continue
                if visited[next_x][next_y] or grid[next_x][next_y] == 1:
                    # уже посещали или уперлись в "стену"
                    continue
                # можно проверять здесь что дошли до пункта назначения
                # чтобы в очередь не накладывать лишних элементов,
                # но больше крайних случаев тогда и кода больше
                visited[next_x][next_y] = True
                # добавляем в очередь элемент и увеличиваем число ходов на 1
                q.append((path_len + 1, (next_x, next_y)))
        return -1
