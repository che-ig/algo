"""
Волновой алгоритм Ли (Lee Algorithm) — поиск кратчайшего пути на 2D-сетке.

Реализация на Python 3.12 с использованием:
- PEP 695: новый синтаксис generic-типов (def func[T](...))
- PEP 695: новый синтаксис TypeAlias (type Point = ...)
- dataclass с параметрами slots и kw_only
- match/case для обработки результатов
- современных type hints (X | Y вместо Union[X, Y])
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from enum import Enum, auto
from typing import Callable, Self

# =============================================================================
# Типы данных (PEP 695 — новый синтаксис type alias)
# =============================================================================

# Координаты точки на сетке (row, col)
type Point = tuple[int, int]

# 2D-сетка произвольного типа ячеек
type Grid[T] = list[list[T]]


# =============================================================================
# Вспомогательные структуры
# =============================================================================


class Direction(Enum):
    """Направления движения на сетке (4-связность)."""

    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

    @property
    def delta(self) -> Point:
        """Смещение координат для данного направления."""
        match self:
            case Direction.UP:
                return (-1, 0)
            case Direction.DOWN:
                return (1, 0)
            case Direction.LEFT:
                return (0, -1)
            case Direction.RIGHT:
                return (0, 1)


# Все направления для 4-связности
FOUR_DIRECTIONS: tuple[Direction, ...] = (
    Direction.UP,
    Direction.DOWN,
    Direction.LEFT,
    Direction.RIGHT,
)

# Все направления для 8-связности (включая диагонали)
EIGHT_DIRECTIONS: tuple[Direction, ...] = (
    Direction.UP,
    Direction.DOWN,
    Direction.LEFT,
    Direction.RIGHT,
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1),  # диагонали как кортежи
)


@dataclass(frozen=True, slots=True)
class SearchResult:
    """Результат работы алгоритма Ли."""

    path: list[Point]
    length: int
    visited_cells: int  # количество посещённых клеток (для отладки)

    @property
    def is_found(self) -> bool:
        """Был ли найден путь."""
        return len(self.path) > 0


@dataclass(frozen=True, slots=True)
class GridBounds:
    """Границы сетки."""

    rows: int
    cols: int

    def contains(self, point: Point) -> bool:
        """Проверка, находится ли точка внутри сетки."""
        row, col = point
        return 0 <= row < self.rows and 0 <= col < self.cols


# =============================================================================
# Основная реализация алгоритма Ли (с PEP 695 generic-синтаксисом)
# =============================================================================


def lee_algorithm[T](
    grid: Grid[T],
    start: Point,
    goal: Point,
    *,
    is_passable: Callable[[T], bool],
    allow_diagonal: bool = False,
) -> SearchResult:
    """
    Волновой алгоритм Ли для поиска кратчайшего пути на 2D-сетке.

    Алгоритм работает за O(R * C), где R — количество строк, C — столбцов.
    Использует BFS для распространения "волны" от стартовой точки.

    Args:
        grid: 2D-сетка (список списков) произвольного типа T.
        start: Начальная точка (row, col).
        goal: Целевая точка (row, col).
        is_passable: Предикат, определяющий, проходима ли ячейка.
                     Например, для int-сетки: lambda cell: cell == 0.
        allow_diagonal: Разрешить движение по диагонали (8-связность).
                        По умолчанию False (4-связность).

    Returns:
        SearchResult с найденным путём, его длиной и статистикой.
        Если путь не найден — path будет пустым списком.

    Raises:
        ValueError: Если start или goal находятся вне сетки или непроходимы.

    Example:
        >>> grid = [[0, 0, 1], [0, 1, 0], [0, 0, 0]]
        >>> result = lee_algorithm(grid, (0, 0), (2, 2), is_passable=lambda x: x == 0)
        >>> result.path
        [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    bounds = GridBounds(rows=rows, cols=cols)

    # === Валидация входных данных ===
    if not bounds.contains(start):
        raise ValueError(f"Стартовая точка {start} находится вне сетки")
    if not bounds.contains(goal):
        raise ValueError(f"Целевая точка {goal} находится вне сетки")
    if not is_passable(grid[start[0]][start[1]]):
        raise ValueError(f"Стартовая точка {start} непроходима")
    if not is_passable(grid[goal[0]][goal[1]]):
        raise ValueError(f"Целевая точка {goal} непроходима")

    # === Специальный случай: старт == цель ===
    if start == goal:
        return SearchResult(path=[start], length=0, visited_cells=1)

    # === Инициализация ===
    # Массив расстояний от старта. -1 означает "не посещено"
    distance: list[list[int]] = [[-1] * cols for _ in range(rows)]
    distance[start[0]][start[1]] = 0

    # Очередь BFS (используем deque для O(1) popleft)
    queue: deque[Point] = deque([start])

    # Массив "предков" для восстановления пути
    # parent[r][c] = точка, из которой мы пришли в (r, c)
    parent: list[list[Point | None]] = [[None] * cols for _ in range(rows)]

    # Направления движения (4 или 8-связность)
    directions: tuple[Direction | tuple[int, int], ...] = (
        EIGHT_DIRECTIONS if allow_diagonal else FOUR_DIRECTIONS
    )

    visited_count = 1  # считаем стартовую клетку

    # === Основной цикл BFS — распространение волны ===
    while queue:
        current = queue.popleft()
        current_dist = distance[current[0]][current[1]]

        # Если достигли цели — можно останавливаться
        if current == goal:
            break

        # Перебираем всех соседей текущей клетки
        for direction in directions:
            # Получаем смещение (у Direction есть .delta, у tuple — напрямую)
            dr, dc = direction.delta if isinstance(direction, Direction) else direction
            neighbor: Point = (current[0] + dr, current[1] + dc)

            # Проверяем границы сетки
            if not bounds.contains(neighbor):
                continue

            nr, nc = neighbor

            # Проверяем, что клетка ещё не посещена и проходима
            if distance[nr][nc] != -1:
                continue
            if not is_passable(grid[nr][nc]):
                continue

            # Для 8-связности: проверяем, что диагональный проход
            # не "режет" угол между двумя препятствиями
            if allow_diagonal and dr != 0 and dc != 0:
                if not is_passable(
                    grid[current[0] + dr][current[1]]
                ) or not is_passable(grid[current[0]][current[1] + dc]):
                    continue

            # "Волна" дошла до этой клетки
            distance[nr][nc] = current_dist + 1
            parent[nr][nc] = current
            queue.append(neighbor)
            visited_count += 1

    # === Проверка: достигли ли мы цели ===
    if distance[goal[0]][goal[1]] == -1:
        # Путь не найден — волна не дошла до цели
        return SearchResult(path=[], length=-1, visited_cells=visited_count)

    # === Восстановление пути (обратный ход от цели к старту) ===
    path: list[Point] = []
    current: Point | None = goal
    while current is not None:
        path.append(current)
        current = parent[current[0]][current[1]]

    # Путь восстановлен в обратном порядке — разворачиваем
    path.reverse()

    return SearchResult(
        path=path,
        length=len(path) - 1,
        visited_cells=visited_count,
    )


# =============================================================================
# Вспомогательные функции для работы с результатом
# =============================================================================


def visualize_grid[T](
    grid: Grid[T],
    path: list[Point],
    *,
    start: Point | None = None,
    goal: Point | None = None,
    wall_symbol: str = "█",
    free_symbol: str = "·",
    path_symbol: str = "★",
    start_symbol: str = "S",
    goal_symbol: str = "G",
) -> str:
    """
    Визуализирует сетку с найденным путём в виде строки.

    Args:
        grid: Исходная 2D-сетка.
        path: Список точек пути.
        start: Стартовая точка (отмечается символом start_symbol).
        goal: Целевая точка (отмечается символом goal_symbol).
        wall_symbol, free_symbol, path_symbol: Символы для отрисовки.

    Returns:
        Строка с визуализацией сетки.
    """
    path_set = set(path)
    lines: list[str] = []

    for r, row in enumerate(grid):
        row_chars: list[str] = []
        for c, cell in enumerate(row):
            point = (r, c)
            if point == start:
                row_chars.append(start_symbol)
            elif point == goal:
                row_chars.append(goal_symbol)
            elif point in path_set:
                row_chars.append(path_symbol)
            # Проверяем, является ли клетка препятствием
            # (используем эвристику: если символ не стандартный — это стена)
            elif cell == 1 or cell == "#" or cell is True:
                row_chars.append(wall_symbol)
            else:
                row_chars.append(free_symbol)
        lines.append(" ".join(row_chars))

    return "\n".join(lines)


# =============================================================================
# Примеры использования
# =============================================================================


def main() -> None:
    """Демонстрация работы алгоритма Ли на различных примерах."""

    print("=" * 60)
    print("ВОЛНОВОЙ АЛГОРИТМ ЛИ — ДЕМОНСТРАЦИЯ")
    print("=" * 60)

    # -------------------------------------------------------------------------
    # Пример 1: Простая сетка с целыми числами
    # -------------------------------------------------------------------------
    print("\n📌 Пример 1: Простая сетка (0 — свободно, 1 — стена)")
    print("-" * 60)

    grid1: Grid[int] = [
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
    ]

    start1: Point = (0, 0)
    goal1: Point = (4, 4)

    result1 = lee_algorithm(
        grid1,
        start1,
        goal1,
        is_passable=lambda cell: cell == 0,
    )

    # Используем match/case для обработки результата (Python 3.10+)
    match result1:
        case SearchResult() if result1.is_found:
            print(f"✅ Путь найден! Длина: {result1.length}")
            print(f"📊 Посещено клеток: {result1.visited_cells}")
            print(f"🛤️  Маршрут: {result1.path}")
            print("\nВизуализация:")
            print(
                visualize_grid(
                    grid1,
                    result1.path,
                    start=start1,
                    goal=goal1,
                )
            )
        case SearchResult() if not result1.is_found:
            print("❌ Путь не найден")
        case _:
            print("⚠️ Неожиданный результат")

    # -------------------------------------------------------------------------
    # Пример 2: Сетка с диагональным движением
    # -------------------------------------------------------------------------
    print("\n\n📌 Пример 2: Движение по диагонали (8-связность)")
    print("-" * 60)

    grid2: Grid[int] = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]

    result2 = lee_algorithm(
        grid2,
        (0, 0),
        (4, 4),
        is_passable=lambda cell: cell == 0,
        allow_diagonal=True,
    )

    if result2.is_found:
        print(f"✅ Путь найден! Длина: {result2.length}")
        print(f"📊 Посещено клеток: {result2.visited_cells}")
        print("\nВизуализация:")
        print(
            visualize_grid(
                grid2,
                result2.path,
                start=(0, 0),
                goal=(4, 4),
            )
        )

    # -------------------------------------------------------------------------
    # Пример 3: Сетка со строковыми ячейками
    # -------------------------------------------------------------------------
    print("\n\n📌 Пример 3: Generic-тип — строковые ячейки")
    print("-" * 60)

    grid3: Grid[str] = [
        ["floor", "floor", "wall", "floor"],
        ["floor", "wall", "floor", "floor"],
        ["floor", "floor", "floor", "wall"],
        ["wall", "floor", "floor", "floor"],
    ]

    result3 = lee_algorithm(
        grid3,
        (0, 0),
        (3, 3),
        is_passable=lambda cell: cell == "floor",
    )

    if result3.is_found:
        print(f"✅ Путь найден! Длина: {result3.length}")
        print(f"🛤️  Маршрут: {result3.path}")
        print("\nВизуализация:")
        print(
            visualize_grid(
                grid3,
                result3.path,
                start=(0, 0),
                goal=(3, 3),
                wall_symbol="▓",
                free_symbol="░",
                path_symbol="◆",
            )
        )

    # -------------------------------------------------------------------------
    # Пример 4: Путь не существует
    # -------------------------------------------------------------------------
    print("\n\n📌 Пример 4: Путь не существует (цель окружена стенами)")
    print("-" * 60)

    grid4: Grid[int] = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 0, 1, 0],  # Клетка (2,2) окружена
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]

    result4 = lee_algorithm(
        grid4,
        (0, 0),
        (2, 2),
        is_passable=lambda cell: cell == 0,
    )

    match result4:
        case SearchResult() if result4.is_found:
            print(f"✅ Путь найден! Длина: {result4.length}")
        case SearchResult() if not result4.is_found:
            print(f"❌ Путь не найден")
            print(f"📊 Посещено клеток до остановки: {result4.visited_cells}")

    # -------------------------------------------------------------------------
    # Пример 5: Старт == Цель
    # -------------------------------------------------------------------------
    print("\n\n📌 Пример 5: Специальный случай — старт совпадает с целью")
    print("-" * 60)

    result5 = lee_algorithm(
        grid1,
        (2, 2),
        (2, 2),
        is_passable=lambda cell: cell == 0,
    )
    print(f"✅ Путь: {result5.path}, длина: {result5.length}")


if __name__ == "__main__":
    main()
