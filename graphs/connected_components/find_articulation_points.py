"""
Точка сочленения — это вершина, удаление которой увеличивает количество компонент связности.
"""


def find_articulation_points(graph):
    """
    Алгоритм Тарьяна для поиска точек сочленения (Articulation Points)
    в неориентированном графе.

    Точка сочленения — это вершина, удаление которой (вместе с инцидентными
    рёбрами) увеличивает количество компонент связности графа.
    """
    index_counter = [0]
    lowlink = {}
    index = {}
    ap = set()
    parent = {}

    def dfs(v):
        index[v] = lowlink[v] = index_counter[0]
        index_counter[0] += 1
        children = 0

        for w in graph[v]:
            if w not in index:
                parent[w] = v
                children += 1
                dfs(w)
                lowlink[v] = min(lowlink[v], lowlink[w])

                # Случай 1: v — корень DFS-дерева и имеет >= 2 детей
                if parent.get(v) is None and children > 1:
                    ap.add(v)

                # Случай 2: v — не корень, и lowlink[w] >= index[v]
                if parent.get(v) is not None and lowlink[w] >= index[v]:
                    ap.add(v)

            elif w != parent.get(v):
                # Back-edge: обновляем lowlink через index (не lowlink!)
                lowlink[v] = min(lowlink[v], index[w])

    for v in graph:
        if v not in index:
            dfs(v)

    return list(ap)


graph1 = {
    "A": ["B", "D"],
    "B": ["A", "C"],
    "C": ["B", "D", "E"],
    "D": ["A", "C"],
    "E": ["C", "F", "H"],
    "F": ["E", "G"],
    "G": ["F", "H"],
    "H": ["E", "G"],
}

print("Тест 1: Граф с одной точкой сочленения")
print(f"  Точки сочленения: {find_articulation_points(graph1)}")
# Ожидаем: ['C']
