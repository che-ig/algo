class Solution:
    # проверяем не выходят ли индексы за границу массива, True - если не выходим
    def good_idx(self, i: int, j: int, board: list[list[str]]) -> bool:
        return 0 <= i < len(board) and 0 <= j < len(board[0])

    # делаем обход и помечаем вершины пройденными
    # если flip -> true, то помечаем все пройденные вершины как X
    def dfs(
        self,
        startX: int,
        startY: int,
        visited: list[list[bool]],
        board: list[list[str]],
        flip: bool,
    ):
        if not self.good_idx(startX, startY, board):
            return
        # dfs запускаем только для не посещенных вершин
        if visited[startX][startY] or board[startX][startY] == "X":
            return

        visited[startX][startY] = True
        if flip:
            board[startX][startY] = "X"

        steps = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # перебераем шаги которые могут быть из текущий вершины
        for step in steps:
            # вычисляем координаты куда можем пойти
            newX, newY = startX + step[0], startY + step[1]
            self.dfs(newX, newY, visited, board, flip)

    def solve(self, board: list[list[str]]) -> None:
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        # перебираем крайние столбцы
        for i in range(len(board)):
            self.dfs(i, 0, visited, board, False)
            self.dfs(i, len(board[0]) - 1, visited, board, False)

        # перебираем крайние строки
        for i in range(len(board[0])):
            self.dfs(0, i, visited, board, False)
            self.dfs(len(board) - 1, i, visited, board, False)

        # обходим все индексы кроме крайних - т к их уже обходили
        for i in range(1, len(board) - 1):
            for j in range(1, len(board[i]) - 1):
                # bfs запускаем только для не посещенных вершин - проверка внутри
                self.dfs(i, j, visited, board, True)


class Solution_1:
    def solve(self, board: list[list[str]]) -> None:
        """
        Изменяет board in-place, заменяя окруженные 'O' на 'X'.
        Использует рекурсивный DFS для пометки безопасных клеток.
        """
        if not board or not board[0]:
            return

        num_rows = len(board)
        num_cols = len(board[0])

        def dfs(row: int, col: int) -> None:
            """
            Рекурсивно помечает все 'O', связанные с граничной клеткой,
            временным символом 'T' (безопасные клетки).
            """
            # Базовый случай: выход за границы или клетка не 'O'
            if (
                row < 0
                or row >= num_rows
                or col < 0
                or col >= num_cols
                or board[row][col] != "O"
            ):
                return

            # Помечаем текущую клетку как безопасную
            board[row][col] = "T"

            # Рекурсивно обходим всех 4 соседей
            dfs(row + 1, col)  # сосед снизу
            dfs(row - 1, col)  # сосед сверху
            dfs(row, col + 1)  # сосед справа
            dfs(row, col - 1)  # сосед слева

        # Шаг 1: Запускаем DFS от всех 'O' на границах доски
        # Верхняя и нижняя строки
        for col in range(num_cols):
            if board[0][col] == "O":
                dfs(0, col)
            if board[num_rows - 1][col] == "O":
                dfs(num_rows - 1, col)

        # Левый и правый столбцы
        for row in range(num_rows):
            if board[row][0] == "O":
                dfs(row, 0)
            if board[row][num_cols - 1] == "O":
                dfs(row, num_cols - 1)

        # Шаг 2: Финальный проход по всей доске
        for row in range(num_rows):
            for col in range(num_cols):
                if board[row][col] == "O":
                    # Окруженная клетка — заменяем на 'X'
                    board[row][col] = "X"
                elif board[row][col] == "T":
                    # Безопасная клетка — возвращаем 'O'
                    board[row][col] = "O"


class Solution_2:
    def solve(self, board: list[list[str]]) -> None:
        """
        Изменяет board in-place, заменяя окруженные 'O' на 'X'.
        Использует итеративный DFS с явным стеком.
        """
        if not board or not board[0]:
            return

        num_rows = len(board)
        num_cols = len(board[0])

        # Направления для обхода соседей: вниз, вверх, вправо, влево
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(start_row: int, start_col: int) -> None:
            """
            Итеративно помечает все 'O', связанные с граничной клеткой,
            временным символом 'T' (безопасные клетки).
            """
            # Инициализируем стек стартовой клеткой
            stack = [(start_row, start_col)]

            # ВАЖНО: помечаем клетку как 'T' СРАЗУ при добавлении в стек,
            # чтобы избежать повторного добавления одной и той же клетки.
            board[start_row][start_col] = "T"

            while stack:
                curr_row, curr_col = stack.pop()

                # Проверяем всех 4 соседей
                for row_offset, col_offset in directions:
                    neighbor_row = curr_row + row_offset
                    neighbor_col = curr_col + col_offset

                    # Если сосед в границах и это 'O'
                    if (
                        0 <= neighbor_row < num_rows
                        and 0 <= neighbor_col < num_cols
                        and board[neighbor_row][neighbor_col] == "O"
                    ):
                        # Помечаем как безопасную и добавляем в стек
                        board[neighbor_row][neighbor_col] = "T"
                        stack.append((neighbor_row, neighbor_col))

        # Шаг 1: Запускаем DFS от всех 'O' на границах доски
        # Верхняя и нижняя строки
        for col in range(num_cols):
            if board[0][col] == "O":
                dfs(0, col)
            if board[num_rows - 1][col] == "O":
                dfs(num_rows - 1, col)

        # Левый и правый столбцы
        for row in range(num_rows):
            if board[row][0] == "O":
                dfs(row, 0)
            if board[row][num_cols - 1] == "O":
                dfs(row, num_cols - 1)

        # Шаг 2: Финальный проход по всей доске
        for row in range(num_rows):
            for col in range(num_cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "T":
                    board[row][col] = "O"
