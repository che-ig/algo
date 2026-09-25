"""
Мост — это ребро, удаление которого увеличивает количество компонент связности.
"""


def find_bridges(graph):
    """
    Алгоритм Тарьяна для поиска мостов в неориентированном графе.
    """
    index_counter = [0]
    lowlink = {}
    index = {}
    bridges = []
    parent = {}

    def dfs(v):
        index[v] = lowlink[v] = index_counter[0]
        index_counter[0] += 1

        for w in graph[v]:
            if w not in index:
                parent[w] = v
                dfs(w)
                lowlink[v] = min(lowlink[v], lowlink[w])

                # Если lowlink[w] > index[v], то (v, w) — мост
                if lowlink[w] > index[v]:
                    bridges.append((v, w))
            elif w != parent.get(v):
                lowlink[v] = min(lowlink[v], index[w])

    for v in graph:
        if v not in index:
            dfs(v)

    return bridges


# Пример
graph = {
    "A": ["B", "C"],
    "B": ["A", "C"],
    "C": ["A", "B", "D"],
    "D": ["C"],  # Ребро C-D — мост
}

print(find_bridges(graph))
# Вывод: [('C', 'D')]
