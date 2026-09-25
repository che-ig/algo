def bellman_ford(graph, start):
    """
    Алгоритм Беллмана-Форда.

    Args:
        graph: dict, список смежности с весами (могут быть отрицательными)
        start: начальная вершина

    Returns:
        dict: кратчайшие расстояния от start
        bool: True если нет отрицательных циклов, False если есть
    """

    # Инициализация расстояний
    distances = {node: float("infinity") for node in graph}
    distances[start] = 0

    # Релаксация рёбер V-1 раз
    V = len(graph)
    for _ in range(V - 1):
        for node in graph:
            if distances[node] == float("infinity"):
                continue
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    # Проверка на отрицательные циклы
    # Если на V-й итерации можно ещё улучшить путь — есть отрицательный цикл
    for node in graph:
        if distances[node] == float("infinity"):
            continue
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                return distances, False  # Отрицательный цикл найден

    return distances, True  # Отрицательных циклов нет


def bellman_ford_optimized(graph, start):
    distances = {node: float("infinity") for node in graph}
    distances[start] = 0

    V = len(graph)
    for i in range(V - 1):
        updated = False  # Флаг изменений

        for node in graph:
            if distances[node] == float("infinity"):
                continue
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    updated = True

        # Если на этой итерации не было изменений — выходим
        if not updated:
            break

    # Проверка на отрицательные циклы
    for node in graph:
        if distances[node] == float("infinity"):
            continue
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                return distances, False

    return distances, True
