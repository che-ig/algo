from collections import deque

# Константа для обозначения свободной клетки
FREE_CELL: int = 0
# Константа для обозначения препятствия
OBSTACLE_CELL: int = 1
# Константа для обозначения непосещенной клетки в матрице расстояний
UNVISITED: int = -1

# Возможные направления движения (вверх, вниз, влево, вправо)
# Формат: (изменение строки, изменение столбца)
DIRECTIONS: list[tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def find_path_lee(
    grid: list[list[int]], start: tuple[int, int], end: tuple[int, int]
) -> list[tuple[int, int]]:
    """
    Итеративная реализация алгоритма Ли для поиска кратчайшего пути на сетке.

    :param grid: Двумерный список (матрица), где 0 - свободная клетка, 1 - препятствие.
    :param start: Кортеж (row, col) с координатами начальной точки.
    :param end: Кортеж (row, col) с координатами конечной точки.
    :return: Список кортежей с координатами клеток, составляющих кратчайший путь.
             Пустой список, если путь не найден.
    """

    # Получаем размеры сетки
    rows: int = len(grid)
    if rows == 0:
        return []
    cols: int = len(grid[0])

    start_row, start_col = start
    end_row, end_col = end

    # Проверка на выход за границы или если старт/финиш находятся в препятствии
    if not (0 <= start_row < rows and 0 <= start_col < cols):
        return []
    if not (0 <= end_row < rows and 0 <= end_col < cols):
        return []
    if (
        grid[start_row][start_col] == OBSTACLE_CELL
        or grid[end_row][end_col] == OBSTACLE_CELL
    ):
        return []

    # --- ЭТАП 1: Прямой ход (Распространение волны с помощью BFS) ---

    # Матрица для хранения расстояний от стартовой точки до каждой клетки
    # Инициализируем все значения как UNVISITED (-1)
    dist: list[list[int]] = [[UNVISITED for _ in range(cols)] for _ in range(rows)]

    # Очередь для обхода в ширину (BFS). Хранит координаты (row, col)
    queue: deque[tuple[int, int]] = deque()

    # Помечаем стартовую клетку и добавляем её в очередь
    dist[start_row][start_col] = 0
    queue.append(start)

    # Пока очередь не пуста, продолжаем распространять волну
    while queue:
        current_row, current_col = queue.popleft()
        current_dist: int = dist[current_row][current_col]

        # Если мы уже дошли до финиша, можно досрочно прервать волну,
        # но для классического алгоритма Ли мы заполняем всю достижимую область.
        # Для оптимизации можно добавить: if (current_row, current_col) == end: break

        # Проверяем всех соседей текущей клетки
        for dr, dc in DIRECTIONS:
            neighbor_row: int = current_row + dr
            neighbor_col: int = current_col + dc

            # Проверяем, находится ли сосед в пределах сетки
            if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                # Проверяем, что сосед свободен и еще не был посещен (волна до него не дошла)
                if (
                    grid[neighbor_row][neighbor_col] == FREE_CELL
                    and dist[neighbor_row][neighbor_col] == UNVISITED
                ):
                    # Записываем расстояние и добавляем соседа в очередь
                    dist[neighbor_row][neighbor_col] = current_dist + 1
                    queue.append((neighbor_row, neighbor_col))

    # --- ЭТАП 2: Обратный ход (Восстановление пути) ---

    # Проверяем, достигла ли волна конечной точки
    if dist[end_row][end_col] == UNVISITED:
        return []  # Путь не существует

    # Начинаем восстанавливать путь от конца к началу
    path: list[tuple[int, int]] = []
    current_row, current_col = end_row, end_col

    # Добавляем конечную точку в путь
    path.append((current_row, current_col))

    # Двигаемся назад, пока не вернемся в стартовую точку
    while (current_row, current_col) != start:
        current_dist = dist[current_row][current_col]
        target_dist: int = current_dist - 1

        # Ищем соседа, расстояние до которого на 1 меньше текущего
        found_previous_step: bool = False
        for dr, dc in DIRECTIONS:
            neighbor_row = current_row + dr
            neighbor_col = current_col + dc

            if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                if dist[neighbor_row][neighbor_col] == target_dist:
                    # Нашли предыдущую клетку на пути
                    path.append((neighbor_row, neighbor_col))
                    current_row, current_col = neighbor_row, neighbor_col
                    found_previous_step = True
                    break  # Выходим из цикла по направлениям, идем на следующую итерацию while

        # Защита от зацикливания в случае некорректных данных (не должна сработать при корректном BFS)
        if not found_previous_step:
            return []

    # Так как мы собирали путь от конца к началу, переворачиваем список
    path.reverse()

    return path


# ==========================================
# Пример использования
# ==========================================
if __name__ == "__main__":
    # 0 - свободная клетка, 1 - стена/препятствие
    test_grid: list[list[int]] = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
    ]

    start_point: tuple[int, int] = (0, 0)
    end_point: tuple[int, int] = (4, 4)

    shortest_path: list[tuple[int, int]] = find_path_lee(
        test_grid, start_point, end_point
    )

    print("Найденный путь (координаты):")
    for step in shortest_path:
        print(step)

    # Визуализация пути на сетке (для проверки)
    print(
        "\nВизуализация (S - старт, E - конец, * - путь, # - стена, . - пустая клетка):"
    )
    path_set: set[tuple[int, int]] = set(shortest_path)

    for r in range(len(test_grid)):
        row_str: str = ""
        for c in range(len(test_grid[0])):
            if (r, c) == start_point:
                row_str += "S "
            elif (r, c) == end_point:
                row_str += "E "
            elif test_grid[r][c] == OBSTACLE_CELL:
                row_str += "# "
            elif (r, c) in path_set:
                row_str += "* "
            else:
                row_str += ". "
        print(row_str.strip())
