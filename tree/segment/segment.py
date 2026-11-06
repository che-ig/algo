class SegmentTree:
    def __init__(self, arr: list[int]) -> None:
        """
        Инициализирует и строит дерево отрезков.
        Время: O(N)
        """
        self.n = len(arr)
        self.arr = arr
        # Размер дерева: 4 * N - безопасная верхняя граница
        self.tree: list[int] = [0] * (4 * self.n)

        # Строим дерево с корня (индекс 1), который покрывает весь массив [0, n-1]
        self._build(1, 0, self.n - 1)

    def _build(self, v: int, tl: int, tr: int) -> None:
        """
        Рекурсивно строит дерево.
        v: индекс текущего узла в массиве tree
        tl, tr: границы отрезка, за который отвечает узел v
        """
        if tl == tr:
            # Мы в листе: значение узла равно элементу массива
            self.tree[v] = self.arr[tl]
        else:
            tm = (tl + tr) // 2
            # Строим левого и правого ребенка
            self._build(2 * v, tl, tm)
            self._build(2 * v + 1, tm + 1, tr)

            # Значение текущего узла = агрегация значений детей
            self.tree[v] = min(self.tree[2 * v], self.tree[2 * v + 1])

    def update(self, pos: int, new_val: int) -> None:
        """
        Изменяет элемент в исходном массиве на позиции pos на new_val.
        Время: O(log N)
        """
        self._update(1, 0, self.n - 1, pos, new_val)

    def _update(self, v: int, tl: int, tr: int, pos: int, new_val: int) -> None:
        if tl == tr:
            # Нашли лист, обновляем его
            self.tree[v] = new_val
        else:
            tm = (tl + tr) // 2
            # Идем в того ребенка, в чьем отрезке лежит позиция pos
            if pos <= tm:
                self._update(2 * v, tl, tm, pos, new_val)
            else:
                self._update(2 * v + 1, tm + 1, tr, pos, new_val)

            # После обновления ребенка, пересчитываем значение текущего узла
            self.tree[v] = min(self.tree[2 * v], self.tree[2 * v + 1])

    def query(self, l: int, r: int) -> int:
        """
        Возвращает минимум на отрезке [l, r].
        Время: O(log N)
        """
        return self._query(1, 0, self.n - 1, l, r)

    def _query(self, v: int, tl: int, tr: int, l: int, r: int) -> int:
        # Случай 1: Отрезок узла полностью лежит внутри запрашиваемого отрезка
        if l <= tl and tr <= r:
            return self.tree[v]

        # Случай 2: Отрезок узла полностью не пересекается с запрашиваемым
        if r < tl or tr < l:
            return float("inf")  # Нейтральный элемент для операции min

        # Случай 3: Частичное пересечение. Идем в обоих детей.
        tm = (tl + tr) // 2
        left_min = self._query(2 * v, tl, tm, l, r)
        right_min = self._query(2 * v + 1, tm + 1, tr, l, r)

        return min(left_min, right_min)
