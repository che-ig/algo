"""
Для неориентированных графов есть понятие компонент связности (Connected Components) — это множества вершин, где из любой вершины можно добраться до любой другой (по любым рёбрам, так как они двусторонние).
"""


def connected_components_undirected(graph):
    """
    Поиск компонент связности в неориентированном графе.
    Простой DFS — намного проще Тарьяна.
    """
    visited = set()
    components = []

    def dfs(node, component):
        visited.add(node)
        component.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, component)

    for node in graph:
        if node not in visited:
            component = []
            dfs(node, component)
            components.append(component)

    return components


# Пример
graph = {"A": ["B", "C"], "B": ["A"], "C": ["A"], "D": ["E"], "E": ["D"], "F": []}

print(connected_components_undirected(graph))
# Вывод: [['A', 'B', 'C'], ['D', 'E'], ['F']]
