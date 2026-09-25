import heapq

"""
Алгоритм Дейкстры — это алгоритм поиска кратчайшего пути от одной вершины до всех остальных в взвешенном графе с неотрицательными весами рёбер.
Он был предложен нидерландским учёным Эдсгером Дейкстрой в 1956 году (опубликован в 1959).

Ключевая идея
Представьте, что вы в городе и хотите добраться до всех остальных городов с минимальными затратами топлива. У вас есть карта с расстояниями между городами.

Логика алгоритма:
    Начинаем с начальной вершины (расстояние = 0).
    Для всех остальных вершин расстояние = ∞ (бесконечность).
    На каждом шаге выбираем непосещённую вершину с минимальным известным расстоянием.
    "Релаксируем" (обновляем) расстояния до всех её соседей: если путь через текущую вершину короче, чем известный — обновляем.
    Помечаем текущую вершину как посещённую.
    Повторяем, пока все вершины не будут посещены (или пока не достигнем цели).


"""


import heapq


def dijkstra_heap(graph, start):
    """
    Алгоритм Дейкстры с приоритетной очередью (min-heap).

    Сложность: O((V + E) log V)

    Args:
        graph: dict, список смежности с весами
        start: начальная вершина

    Returns:
        dict: кратчайшие расстояния от start
        dict: предыдущие вершины для восстановления пути
    """

    # Инициализация расстояний
    distances = {node: float("infinity") for node in graph}
    distances[start] = 0

    # Для восстановления пути
    previous = {node: None for node in graph}

    # Приоритетная очередь (min-heap)
    # Хранит кортежи (расстояние, вершина)
    # heapq всегда извлекает элемент с минимальным первым значением
    pq = [(0, start)]

    # Множество посещённых вершин
    visited = set()

    while pq:
        # Извлекаем вершину с минимальным расстоянием — O(log V)
        current_dist, current_node = heapq.heappop(pq)

        # Если вершина уже посещена — пропускаем
        # (в куче могут быть устаревшие записи)
        if current_node in visited:
            continue

        visited.add(current_node)

        # Релаксация рёбер
        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                distance = current_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    # Добавляем в кучу — O(log V)
                    heapq.heappush(pq, (distance, neighbor))

    return distances, previous


def reconstruct_path(previous, start, end):
    """Восстанавливает кратчайший путь."""
    path = []
    current = end

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    if path[0] != start:
        return []

    return path


if __name__ == "__main__":
    graph = {"A": {"B": 4, "C": 2}, "B": {"D": 1}, "C": {"B": 1, "D": 5}, "D": {}}

    start = "A"

    distances, previous = dijkstra_heap(graph, start)

    print("Кратчайшие расстояния от A:")
    for node, dist in distances.items():
        print(f"  до {node}: {dist}")

    print("\nВосстановление пути от A до D:")
    path = reconstruct_path(previous, start, "D")
    print(f"  Путь: {' -> '.join(path)}")
    print(f"  Длина: {distances['D']}")
