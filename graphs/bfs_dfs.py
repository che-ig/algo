from collections import deque


def bfs(graph, start):
    """
    Обход графа в ширину (BFS).
    """
    # Множество для отслеживания посещенных вершин
    visited = set()

    # Очередь для хранения вершин, которые нужно обойти
    queue = deque([start])

    # Сразу помечаем стартовую вершину как посещенную
    visited.add(start)

    # Список для сохранения порядка обхода (для наглядности)
    traversal_order = []

    while queue:
        # Извлекаем вершину из начала очереди (FIFO)
        current_node = queue.popleft()
        traversal_order.append(current_node)

        # Перебираем всех соседей текущей вершины
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                # Помечаем как посещенную СРАЗУ при добавлении в очередь,
                # чтобы не добавить одну и ту же вершину несколько раз
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order


def dfs_recursive(graph, start):
    """
    Обход графа в глубину (DFS) с использованием рекурсии.
    """
    visited = set()
    traversal_order = []

    # Вложенная рекурсивная функция
    def dfs(node):
        visited.add(node)
        traversal_order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    # Запускаем обход от стартовой вершины
    dfs(start)

    return traversal_order


def dfs_iterative(graph, start):
    """
    Обход графа в глубину (DFS) с использованием явного стека.
    """
    visited = set()
    stack = [start]
    traversal_order = []

    while stack:
        # Извлекаем вершину с вершины стека (LIFO)
        current_node = stack.pop()

        if current_node not in visited:
            visited.add(current_node)
            traversal_order.append(current_node)

            # Получаем соседей.
            # Используем reversed(), чтобы при добавлении в стек
            # первый сосед оказался наверху и был обработан первым.
            for neighbor in reversed(graph[current_node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return traversal_order


if __name__ == "__main__":
    # Представление графа в виде списка смежности
    graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": [], "F": []}

    start_node = "A"

    print("--- BFS (Поиск в ширину) ---")
    print("Порядок обхода:", bfs(graph, start_node))
    # Ожидаем: A, затем соседи A (B, C), затем соседи B и C (D, E, F)
    # Результат: ['A', 'B', 'C', 'D', 'E', 'F']

    print("\n--- DFS Recursive (Рекурсия) ---")
    print("Порядок обхода:", dfs_recursive(graph, start_node))
    # Ожидаем: A, уходим в B, уходим в D, возвращаемся в B, уходим в E...
    # Результат: ['A', 'B', 'D', 'E', 'C', 'F']

    print("\n--- DFS Iterative (Стек) ---")
    print("Порядок обхода:", dfs_iterative(graph, start_node))
    # Благодаря reversed() результат идентичен рекурсии
    # Результат: ['A', 'B', 'D', 'E', 'C', 'F']
