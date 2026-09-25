def tarjan_scc(graph):
    """
    Итеративный алгоритм Тарьяна для поиска компонент сильной связности.

    :param graph: dict {вершина: список смежных вершин}
                  или список списков (граф, заданный списком смежности)
    :return: список компонент сильной связности (каждая — список вершин)
    """
    n = len(graph)

    # discovery[v] = индекс времени, когда вершина v была впервые посещена
    #                (-1 означает, что вершина ещё не посещена)
    discovery = [-1] * n
    # lowlink[v] = минимальный discovery-индекс, достижимый из v
    #              (через потомков и обратные рёбра)
    lowlink = [-1] * n
    # on_stack[v] = находится ли v сейчас в стеке tarjan_stack
    on_stack = [False] * n

    # Стек вершин, находящихся в текущей "рассматриваемой" части графа.
    # Когда мы находим SCC — снимаем её вершины с этого стека.
    tarjan_stack = []

    # Стек для эмуляции рекурсии.
    # Каждый элемент — это [вершина, индекс следующего соседа для обработки].
    call_stack = []

    # Счётчик времени (глобальный для всего алгоритма)
    time = 0
    # Список найденных SCC
    sccs = []

    for start in range(n):
        # Пропускаем уже посещённые вершины
        if discovery[start] != -1:
            continue

        # Кладём стартовую вершину в стек вызовов.
        # Второй элемент (индекс соседа) изначально 0.
        call_stack.append([start, 0])

        # При "входе" в вершину выполняем инициализацию
        discovery[start] = lowlink[start] = time
        time += 1
        tarjan_stack.append(start)
        on_stack[start] = True

        # Основной цикл обхода
        while call_stack:
            v, i = call_stack[-1]
            neighbors = graph[v]

            if i < len(neighbors):
                # Есть ещё необработанные соседи — берём следующего
                w = neighbors[i]
                # Увеличиваем счётчик соседей у вершины v
                call_stack[-1][1] += 1

                if discovery[w] == -1:
                    # Сосед w ещё не посещён — "рекурсивно" заходим в него
                    discovery[w] = lowlink[w] = time
                    time += 1
                    tarjan_stack.append(w)
                    on_stack[w] = True
                    call_stack.append([w, 0])
                elif on_stack[w]:
                    # w в стеке — это обратное ребро, обновляем lowlink
                    if discovery[w] < lowlink[v]:
                        lowlink[v] = discovery[w]
                # Если w посещён, но не в стеке — это ребро в уже
                # обработанную SCC, его можно игнорировать.
            else:
                # Все соседи обработаны — "выходим" из вершины v
                call_stack.pop()

                if lowlink[v] == discovery[v]:
                    # v — корень SCC. Снимаем все вершины до v включительно.
                    scc = []
                    while True:
                        w = tarjan_stack.pop()
                        on_stack[w] = False
                        scc.append(w)
                        if w == v:
                            break
                    sccs.append(scc)

                # После возврата из v обновляем lowlink родителя
                if call_stack:
                    parent = call_stack[-1][0]
                    if lowlink[v] < lowlink[parent]:
                        lowlink[parent] = lowlink[v]

    return sccs


# ---------- Пример использования ----------
if __name__ == "__main__":
    # Граф:
    #   0 → 1 → 2 → 0   (цикл: {0,1,2} — одна SCC)
    #   2 → 3 → 4 → 3   (цикл: {3,4} — другая SCC)
    graph = {
        0: [1],
        1: [2],
        2: [0, 3],
        3: [4],
        4: [3],
    }

    # Если граф задан словарём — преобразуем в список смежности
    n = max(graph) + 1
    adj = [graph.get(i, []) for i in range(n)]

    result = tarjan_scc(adj)
    print("Компоненты сильной связности:")
    for comp in result:
        print(sorted(comp))
