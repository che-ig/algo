def tarjan_scc(graph):
    """
    Алгоритм Тарьяна для поиска компонент сильной связности (SCC).

    Args:
        graph: dict, список смежности ориентированного графа.
               Пример: {'A': ['B'], 'B': ['C', 'A'], 'C': []}

    Returns:
        list of lists: каждая компонента — список вершин.
    """

    index_counter = [
        0
    ]  # Счётчик index (используем список для изменяемости в замыкании)
    stack = []  # Стек вершин в текущем пути DFS
    lowlink = {}  # lowlink[v] = минимальный index, достижимый из v
    index = {}  # index[v] = порядок посещения v
    on_stack = set()  # Множество вершин, находящихся в стеке
    sccs = []  # Результат: список SCC

    def strongconnect(v):
        # Шаг 1: Присваиваем index и lowlink
        index[v] = index_counter[0]
        lowlink[v] = index_counter[0]
        index_counter[0] += 1
        stack.append(v)
        on_stack.add(v)

        # Шаг 2: Обходим соседей
        for w in graph.get(v, []):
            if w not in index:
                # Сосед ещё не посещён — рекурсивный вызов
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif w in on_stack:
                # Сосед в стеке (серый) — это back-edge, обновляем lowlink
                lowlink[v] = min(lowlink[v], index[w])

        # Шаг 3: Если v — корень SCC, выгребаем SCC из стека
        if lowlink[v] == index[v]:
            scc = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                scc.append(w)
                if w == v:
                    break
            sccs.append(scc)

    # Шаг 4: Запускаем DFS от каждой непосещённой вершины
    for v in graph:
        if v not in index:
            strongconnect(v)

    return sccs


if __name__ == "__main__":
    # Граф с двумя SCC
    # SCC 1: {A, B, C, D, E, F}
    # SCC 2: {G}
    graph = {
        "A": ["B"],
        "B": ["C"],
        "C": ["D"],
        "D": ["E"],
        "E": ["F", "G"],
        "F": ["A"],  # ← Цикл A→B→C→D→E→F→A
        "G": [],
    }

    sccs = tarjan_scc(graph)

    print("Компоненты сильной связности:")
    for i, scc in enumerate(sccs, 1):
        print(f"  SCC {i}: {scc}")
