class SegmentTreeMin:
    """
    Итеративное дерево отрезков для нахождения минимума.

    Массив tree имеет размер 2*n.
    Листья: tree[n], tree[n+1], ..., tree[2n-1]
    Внутренние узлы: tree[1], tree[2], ..., tree[n-1]

    Данная реализация поддерживает:
    - Построение за O(N)
    - Обновление элемента за O(log N)
    - Запрос минимума на отрезке за O(log N)
    """

    def __init__(self, arr: list[int]) -> None:
        """
        Построение дерева отрезков за O(N).

        Args:
            arr: Исходный массив (0-индексация)
        """
        self.n = len(arr)
        # Используем float('inf') как нейтральный элемент для операции минимума
        self.tree: list[int | float] = [float("inf")] * (2 * self.n)

        # Копируем листья
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]

        # Строим внутренние узлы снизу вверх
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = min(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, pos: int, value: int) -> None:
        """
        Устанавливает значение arr[pos] = value.
        Время: O(log N)

        Args:
            pos: Индекс элемента (0-индексация)
            value: Новое значение
        """
        # Переходим к соответствующему листу
        pos += self.n

        # Обновляем лист
        self.tree[pos] = value

        # Поднимаемся вверх, обновляя предков
        while pos > 1:
            pos //= 2
            self.tree[pos] = min(self.tree[2 * pos], self.tree[2 * pos + 1])

    def query(self, left: int, right: int) -> int | float:
        """
        Возвращает минимум на отрезке [left, right].
        Время: O(log N)

        Args:
            left: Левая граница (0-индексация, включительно)
            right: Правая граница (0-индексация, включительно)

        Returns:
            Минимальный элемент среди arr[left], ..., arr[right].
            Если диапазон некорректен (left > right), возвращает float('inf').
        """
        # Переходим к листьям
        left += self.n
        right += self.n

        # Нейтральный элемент для операции минимума
        result = float("inf")

        # Двигаемся вверх, пока указатели не пересекутся
        while left <= right:
            # Если left — правый ребёнок, учитываем его значение и двигаемся вправо
            if left % 2 == 1:
                result = min(result, self.tree[left])
                left += 1

            # Если right — левый ребёнок, учитываем его значение и двигаемся влево
            if right % 2 == 0:
                result = min(result, self.tree[right])
                right -= 1

            # Переходим к родителям
            left //= 2
            right //= 2

        return result


if __name__ == "__main__":
    arr = [5, 2, 8, 1, 9, 3]
    st = SegmentTreeMin(arr)

    print(st.query(1, 4))  # Минимум в [2, 8, 1, 9] -> 1
    print(st.query(0, 5))  # Минимум во всём массиве -> 1

    st.update(3, 10)  # Меняем элемент 1 (на индексе 3) на 10
    print(st.query(1, 4))  # Минимум в [2, 8, 10, 9] -> 2
