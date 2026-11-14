"""
Реализация алгоритма Кана для топологической сортировки ориентированного ациклического графа (DAG).

Алгоритм работает за O(V + E), где V — количество вершин, E — количество рёбер.
Использует BFS-подход с подсчётом входящих степеней вершин.
"""

from collections import deque
from collections.abc import Iterable


class CycleDetectedError(ValueError):
    """Исключение, выбрасываемое при обнаружении цикла в графе."""

    def __init__(self, remaining_vertices: set[int]) -> None:
        self.remaining_vertices = remaining_vertices
        super().__init__(
            f"Граф содержит цикл. Вершины, участвующие в цикле или зависящие от него: "
            f"{sorted(remaining_vertices)}"
        )


def topological_sort_kahn[T](
    graph: dict[T, list[T]],
    all_vertices: Iterable[T] | None = None,
) -> list[T]:
    """
    Выполняет топологическую сортировку ориентированного ациклического графа
    с помощью алгоритма Кана (BFS-подход).

    Args:
        graph: Словарь смежности. Ключ — вершина, значение — список вершин,
               в которые ведут рёбра из данной.
        all_vertices: Опциональное множество всех вершин графа. Нужно, если
                      в графе есть изолированные вершины (без исходящих рёбер),
                      которых нет в ключах `graph`. Если не указано, берётся
                      объединение ключей `graph` и всех значений.

    Returns:
        Список вершин в топологическом порядке.

    Raises:
        CycleDetectedError: Если в графе обнаружен цикл.

    Example:
        >>> graph = {0: [1, 2], 1: [3], 2: [3], 3: [4]}
        >>> topological_sort_kahn(graph)
        [0, 1, 2, 3, 4]
    """
    # 1. Собираем множество всех вершин графа
    if all_vertices is None:
        vertices: set[T] = set(graph.keys())
        for neighbors in graph.values():
            vertices.update(neighbors)
    else:
        vertices = set(all_vertices)

    # 2. Инициализируем входящие степени (in-degree) всех вершин нулём
    in_degree: dict[T, int] = {v: 0 for v in vertices}

    # 3. Подсчитываем входящие степени: для каждого ребра u -> v
    #    увеличиваем in_degree[v] на 1
    for u, neighbors in graph.items():
        for v in neighbors:
            in_degree[v] += 1

    # 4. Очередь вершин с нулевой входящей степенью (не зависят ни от кого)
    #    Используем deque для эффективного popleft() за O(1)
    queue: deque[T] = deque(v for v, degree in in_degree.items() if degree == 0)

    # 5. Результирующий список — топологический порядок
    sorted_vertices: list[T] = []

    # 6. Основной цикл BFS: обрабатываем вершины с нулевой входящей степенью
    while queue:
        current = queue.popleft()
        sorted_vertices.append(current)

        # Уменьшаем входящую степень всех соседей текущей вершины
        for neighbor in graph.get(current, []):
            in_degree[neighbor] -= 1
            # Если входящая степень стала нулевой — вершина готова к обработке
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # 7. Проверка на наличие цикла: если обработаны не все вершины,
    #    значит, в графе есть цикл (вершины в цикле никогда не достигнут in_degree = 0)
    if len(sorted_vertices) != len(vertices):
        remaining = vertices - set(sorted_vertices)
        raise CycleDetectedError(remaining)

    return sorted_vertices


# =============================================================================
# Пример использования
# =============================================================================
if __name__ == "__main__":
    # Пример 1: Простой DAG (задачи с зависимостями)
    # Граф: 0 -> 1, 0 -> 2, 1 -> 3, 2 -> 3, 3 -> 4
    dag: dict[int, list[int]] = {
        0: [1, 2],
        1: [3],
        2: [3],
        3: [4],
    }

    print("Пример 1: Ациклический граф")
    print(f"Граф: {dag}")
    result = topological_sort_kahn(dag)
    print(f"Топологический порядок: {result}")
    # Возможный вывод: [0, 1, 2, 3, 4]

    # Пример 2: Граф со строковыми вершинами (курс с пререквизитами)
    courses: dict[str, list[str]] = {
        "Математика": ["Физика"],
        "Физика": ["Механика", "Квантовая физика"],
        "Программирование": ["Алгоритмы"],
        "Алгоритмы": ["Машинное обучение"],
        "Математика": ["Машинное обучение"],
    }

    print("\nПример 2: Строковые вершины")
    print(f"Топологический порядок курсов: {topological_sort_kahn(courses)}")

    # Пример 3: Граф с циклом
    cyclic_graph: dict[int, list[int]] = {
        0: [1],
        1: [2],
        2: [0],  # Цикл: 0 -> 1 -> 2 -> 0
        3: [],
    }

    print("\nПример 3: Граф с циклом")
    try:
        topological_sort_kahn(cyclic_graph)
    except CycleDetectedError as e:
        print(f"Ошибка: {e}")

    # Пример 4: Граф с изолированной вершиной
    graph_with_isolated: dict[int, list[int]] = {
        0: [1],
        1: [2],
    }
    # Вершина 99 не имеет исходящих рёбер и не упоминается в значениях
    print("\nПример 4: Граф с изолированной вершиной")
    print(
        f"Порядок: {topological_sort_kahn(graph_with_isolated, all_vertices={0, 1, 2, 99})}"
    )
