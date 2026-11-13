import sys
from typing import Callable


class SegmentTree:
    """
    Итеративное Дерево отрезков.
    Поддерживает:
    - Обновление значения в точке (Point Update)
    - Запрос суммы на отрезке (Range Sum Query)
    """

    def __init__(self, data: list[int]):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build(data)

    def build(self, data: list[int]) -> None:
        """Построение дерева отрезков за O(n)."""
        # Заполняем листья
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        # Строим внутренние узлы снизу вверх
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, pos: int, value: int) -> None:
        """
        Обновление значения в позиции pos (0-indexed).
        Время: O(log n)
        """
        pos += self.n
        self.tree[pos] = value
        # Обновляем всех предков
        while pos > 1:
            self.tree[pos >> 1] = self.tree[pos] + self.tree[pos ^ 1]
            pos >>= 1

    def query(self, l: int, r: int) -> int:
        """
        Сумма на отрезке [l, r] (0-indexed, включительно).
        Время: O(log n)
        """
        res = 0
        l += self.n
        r += self.n + 1  # Делаем r исключительно правым

        while l < r:
            # Если l - правый ребёнок, берём его и идём правее
            if l & 1:
                res += self.tree[l]
                l += 1
            # Если r - правый ребёнок, берём его (r-1) и идём левее
            if r & 1:
                r -= 1
                res += self.tree[r]
            l >>= 1
            r >>= 1
        return res


class HLD:
    """
    Heavy-Light Decomposition (итеративная версия).

    Разбивает дерево на тяжёлые пути так, что:
    - Каждый путь в дереве разбивается на O(log n) непрерывных отрезков
    - Каждый тяжёлый путь занимает непрерывный диапазон в массиве

    Это позволяет использовать Дерево отрезков для операций на путях.
    """

    def __init__(
        self,
        n: int,
        edges: list[tuple[int, int]],
        initial_values: list[int],
        root: int = 0,
    ):
        self.n = n
        # Строим список смежности
        self.adj: list[list[int]] = [[] for _ in range(n)]
        for u, v in edges:
            self.adj[u].append(v)
            self.adj[v].append(u)

        self.values = initial_values
        self.root = root

        # Результаты первого DFS
        self.parent = [-1] * n  # Родитель каждой вершины
        self.depth = [0] * n  # Глубина каждой вершины
        self.sz = [1] * n  # Размер поддерева
        self.heavy = [-1] * n  # Индекс тяжёлого ребёнка

        # Результаты второго DFS
        self.pos = [0] * n  # Позиция в линеаризованном массиве
        self.top = [0] * n  # Голова тяжёлой цепи

        # Выполняем итеративные DFS
        self._dfs1_iterative(root)
        self._dfs2_iterative(root)

        # Собираем массив для Дерева отрезков в правильном порядке
        seg_data = [0] * n
        for i in range(n):
            seg_data[self.pos[i]] = self.values[i]

        self.seg = SegmentTree(seg_data)

    def _dfs1_iterative(self, start: int) -> None:
        """
        Первый итеративный DFS.
        Считает размеры поддеревьев и находит тяжёлых детей.

        Используем стек с состоянием (вершина, родитель, индекс_ребёнка).
        Индекс_ребёнка нужен, чтобы после возврата из поддерева продолжить
        обход оставшихся детей.
        """
        # Стек хранит кортежи: (вершина, родитель, индекс_текущего_ребёнка)
        stack = [(start, -1, 0)]

        # Также нужен стек для post-order обработки (когда все дети обработаны)
        post_order_stack = []

        while stack:
            v, p, child_idx = stack.pop()

            # Если это первый визит (child_idx == 0)
            if child_idx == 0:
                self.parent[v] = p
                if p != -1:
                    self.depth[v] = self.depth[p] + 1

                # Помещаем вершину в post-order стек для обработки после детей
                post_order_stack.append(v)

            # Пропускаем уже обработанных детей
            while child_idx < len(self.adj[v]) and self.adj[v][child_idx] == p:
                child_idx += 1

            # Если есть необработанные дети
            if child_idx < len(self.adj[v]):
                to = self.adj[v][child_idx]
                # Возвращаем текущую вершину с увеличенным индексом ребёнка
                stack.append((v, p, child_idx + 1))
                # Идём в ребёнка
                stack.append((to, v, 0))
            else:
                # Все дети обработаны - ничего не делаем, обработаем в post-order

                # Post-order обработка: считаем размеры и ищем тяжёлых детей
                while post_order_stack:
                    v = post_order_stack.pop()
                    max_subtree_size = 0

                    for to in self.adj[v]:
                        if to != self.parent[v]:
                            self.sz[v] += self.sz[to]
                            if self.sz[to] > max_subtree_size:
                                max_subtree_size = self.sz[to]
                                self.heavy[v] = to

    def _dfs2_iterative(self, start: int) -> None:
        """
        Второй итеративный DFS.
        Линеаризует дерево: присваивает позиции и головы цепей.

        ВАЖНО: Тяжёлого ребёнка нужно обрабатывать ПЕРВЫМ,
        чтобы вся тяжёлая цепь получила непрерывные индексы.

        Используем стек, но при добавлении детей в стек
        кладём тяжёлого ребёнка ПОСЛЕДНИМ (чтобы он обработался первым).
        """
        cur_pos = 0
        # Стек хранит кортежи: (вершина, голова_цепи)
        stack = [(start, start)]

        while stack:
            v, up = stack.pop()

            # Присваиваем позицию и голову
            self.pos[v] = cur_pos
            self.top[v] = up
            cur_pos += 1

            # Собираем детей, кроме тяжёлого (его обработаем отдельно)
            light_children = []
            for to in self.adj[v]:
                if to != self.parent[v] and to != self.heavy[v]:
                    light_children.append(to)

            # Добавляем лёгких детей в стек (они начнут новые цепи)
            # В обратном порядке, чтобы первый ребёнок обработался первым
            for to in reversed(light_children):
                stack.append((to, to))

            # Тяжёлого ребёнка добавляем последним (обработается первым)
            # Он продолжает текущую цепь, поэтому голова остаётся up
            if self.heavy[v] != -1:
                stack.append((self.heavy[v], up))

    def update_vertex(self, v: int, new_value: int) -> None:
        """
        Обновить значение в конкретной вершине дерева.
        Время: O(log n)
        """
        self.seg.update(self.pos[v], new_value)

    def query_path(self, u: int, v: int) -> int:
        """
        Запрос суммы на пути между u и v.

        Алгоритм:
        1. Пока u и v в разных цепях, поднимаем ту, чья голова глубже
        2. Берём сумму от головы до текущей вершины
        3. Переходим к родителю головы
        4. Когда оказались в одной цепи, берём сумму между u и v

        Время: O(log² n) - не более O(log n) запросов к Segment Tree
        """
        res = 0

        # Пока u и v находятся в разных тяжёлых цепях
        while self.top[u] != self.top[v]:
            # Та вершина, чья "голова" цепи глубже, будет подниматься
            if self.depth[self.top[u]] < self.depth[self.top[v]]:
                u, v = v, u

            # u теперь глубже. Берём сумму от головы цепи u до самой u
            res += self.seg.query(self.pos[self.top[u]], self.pos[u])
            # Переходим к родителю головы цепи
            u = self.parent[self.top[u]]

        # Теперь u и v в одной цепи
        # Та вершина, которая глубже, будет правой границей в массиве
        if self.depth[u] > self.depth[v]:
            u, v = v, u

        res += self.seg.query(self.pos[u], self.pos[v])
        return res


# Пример использования
if __name__ == "__main__":
    # Дерево:
    #        0 (val=10)
    #      /   \
    #     1     2 (val=20, 30)
    #    / \     \
    #   3   4     5 (val=40, 50, 60)

    # n = 6
    # edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5)]
    # values = [10, 20, 30, 40, 50, 60]
    n = 16
    edges = [
        (0, 1),
        (0, 2),
        (0, 3),  # Корень к детям первого уровня
        (1, 4),  # Вершина 1 к ребёнку
        (2, 5),  # Вершина 2 к ребёнку
        (3, 6),
        (3, 7),
        (3, 8),  # Вершина 3 к трём детям
        (4, 9),  # Вершина 4 к ребёнку
        (5, 10),
        (5, 11),  # Вершина 5 к двум детям
        (6, 12),
        (6, 13),  # Вершина 6 к двум детям
        (8, 14),  # Вершина 8 к ребёнку
        (10, 15),  # Вершина 10 к ребёнку
    ]

    values = [50, 30, 70, 40, 60, 20, 80, 90, 10, 100, 110, 120, 130, 140, 150, 160]
    hld = HLD(n, edges, values, root=0)

    # Запрос 1: Сумма на пути 3 -> 5 (3 -> 1 -> 0 -> 2 -> 5)
    # Ожидаем: 40 + 20 + 10 + 30 + 60 = 160
    print("Path 3 to 5:", hld.query_path(3, 5))

    # Запрос 2: Сумма на пути 4 -> 2 (4 -> 1 -> 0 -> 2)
    # Ожидаем: 50 + 20 + 10 + 30 = 110
    print("Path 4 to 2:", hld.query_path(4, 2))
    print("Path 0 to 5:", hld.query_path(0, 5))
    print("Path 3 to 4:", hld.query_path(3, 4))
    print("Path 4 to 3:", hld.query_path(4, 3))

    # Обновление: Меняем значение в вершине 0 на 100
    hld.update_vertex(0, 100)

    # Запрос 3: Сумма на пути 3 -> 5 после обновления
    # Ожидаем: 40 + 20 + 100 + 30 + 60 = 250
    print("Path 3 to 5 (after update):", hld.query_path(3, 5))
