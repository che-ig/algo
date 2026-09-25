def dijkstra_simple(graph, start):
    """
    Алгоритм Дейкстры без приоритетной очереди.
    Использует простой поиск минимума за O(V) на каждой итерации.

    Сложность: O(V²)

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

    # Множество непосещённых вершин
    unvisited = set(graph.keys())

    while unvisited:
        # Находим вершину с минимальным расстоянием среди непосещённых
        # Это O(V) на каждой итерации
        min_dist = float("infinity")
        current_node = None

        for node in unvisited:
            if distances[node] < min_dist:
                min_dist = distances[node]
                current_node = node

        # Если минимальное расстояние = бесконечность,
        # значит оставшиеся вершины недостижимы
        if current_node is None or min_dist == float("infinity"):
            break

        # Удаляем текущую вершину из непосещённых
        unvisited.remove(current_node)

        # Релаксация рёбер
        for neighbor, weight in graph[current_node].items():
            if neighbor in unvisited:  # Только непосещённые
                distance = distances[current_node] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node

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

    distances, previous = dijkstra_simple(graph, start)

    print("Кратчайшие расстояния от A:")
    for node, dist in distances.items():
        print(f"  до {node}: {dist}")

    print("\nВосстановление пути от A до D:")
    path = reconstruct_path(previous, start, "D")
    print(f"  Путь: {' -> '.join(path)}")
    print(f"  Длина: {distances['D']}")
