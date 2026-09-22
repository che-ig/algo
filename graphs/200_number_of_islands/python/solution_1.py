from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        """
        Подсчитывает количество островов в двоичной сетке.

        Остров — это группа единиц ('1'), соединённых горизонтально
        или вертикально. Вода обозначена нулями ('0').

        Args:
            grid: двумерный массив строк '0' и '1'

        Returns:
            Количество островов в сетке
        """
        # Обработка пустой сетки
        if not grid:
            return 0

        num_rows = len(grid)
        num_cols = len(grid[0])
        islands_count = 0

        # Массив для отслеживания посещённых клеток.
        # Создаём его отдельно, чтобы не мутировать входные данные grid.
        # Это важно в реальных проектах, где входной массив может
        # использоваться дальше по коду.
        visited = [[False] * num_cols for _ in range(num_rows)]

        # 4 направления обхода: вниз, вверх, вправо, влево.
        # Диагонали не учитываем по условию задачи.
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(start_row: int, start_col: int) -> None:
            """
            Обходит весь остров, начинающийся с клетки (start_row, start_col),
            и помечает все его клетки как посещённые.
            """
            # Инициализируем очередь с начальной клеткой
            queue = deque([(start_row, start_col)])

            # ВАЖНО: помечаем клетку как посещённую СРАЗУ при добавлении
            # в очередь, а не при извлечении. Это предотвращает дублирование
            # клеток в очереди и экономит память.
            visited[start_row][start_col] = True

            while queue:
                curr_row, curr_col = queue.popleft()

                # Проверяем всех 4 соседей текущей клетки
                for row_offset, col_offset in directions:
                    neighbor_row = curr_row + row_offset
                    neighbor_col = curr_col + col_offset

                    # Ранний выход #1: сосед вне границ сетки
                    if not (
                        0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols
                    ):
                        continue

                    # Ранний выход #2: сосед — это вода или уже посещён
                    # Использование continue вместо вложенных if делает
                    # код более плоским и читаемым.
                    if (
                        grid[neighbor_row][neighbor_col] == "0"
                        or visited[neighbor_row][neighbor_col]
                    ):
                        continue

                    # Сосед — новая клетка острова. Помечаем и добавляем в очередь.
                    visited[neighbor_row][neighbor_col] = True
                    queue.append((neighbor_row, neighbor_col))

        # Проходим по каждой клетке сетки
        for row in range(num_rows):
            for col in range(num_cols):
                # Новый остров найден, если:
                # 1. Клетка содержит землю ('1')
                # 2. Клетка ещё не была посещена (иначе она часть уже
                #    подсчитанного острова)
                if grid[row][col] == "1" and not visited[row][col]:
                    islands_count += 1
                    # Обходим весь остров, чтобы пометить все его клетки.
                    # Это гарантирует, что мы не посчитаем один и тот же
                    # остров дважды.
                    bfs(row, col)

        return islands_count
