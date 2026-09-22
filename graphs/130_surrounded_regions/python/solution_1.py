from collections import deque


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Изменяет board in-place, заменяя окруженные 'O' на 'X'.
        """
        if not board or not board[0]:
            return

        num_rows = len(board)
        num_cols = len(board[0])

        # Направления для обхода соседей: вниз, вверх, вправо, влево
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(start_row: int, start_col: int) -> None:
            """
            Помечает все 'O', связанные с граничной клеткой,
            временным символом 'T' (безопасные клетки).
            """
            queue = deque([(start_row, start_col)])
            board[start_row][start_col] = "T"  # Помечаем сразу при добавлении

            while queue:
                curr_row, curr_col = queue.popleft()

                for row_offset, col_offset in directions:
                    neighbor_row = curr_row + row_offset
                    neighbor_col = curr_col + col_offset

                    # Проверяем границы и является ли сосед 'O'
                    if (
                        0 <= neighbor_row < num_rows
                        and 0 <= neighbor_col < num_cols
                        and board[neighbor_row][neighbor_col] == "O"
                    ):
                        board[neighbor_row][neighbor_col] = (
                            "T"  # Помечаем как безопасный
                        )
                        queue.append((neighbor_row, neighbor_col))

        # Шаг 1: Запускаем BFS от всех 'O' на границах доски
        # Проходим по верхней и нижней строкам
        for col in range(num_cols):
            if board[0][col] == "O":
                bfs(0, col)
            if board[num_rows - 1][col] == "O":
                bfs(num_rows - 1, col)

        # Проходим по левому и правому столбцам
        for row in range(num_rows):
            if board[row][0] == "O":
                bfs(row, 0)
            if board[row][num_cols - 1] == "O":
                bfs(row, num_cols - 1)

        # Шаг 2: Финальный проход по всей доске для замены символов
        for row in range(num_rows):
            for col in range(num_cols):
                if board[row][col] == "O":
                    # Этот 'O' не был помечен как 'T', значит он окружен
                    board[row][col] = "X"
                elif board[row][col] == "T":
                    # Возвращаем безопасные клетки обратно в 'O'
                    board[row][col] = "O"
