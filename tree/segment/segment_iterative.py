class SegmentTreeSum:
    """
    Итеративное дерево отрезков для суммы.

    Массив tree имеет размер 2*n.
    Листья: tree[n], tree[n+1], ..., tree[2n-1]
    Внутренние узлы: tree[1], tree[2], ..., tree[n-1]
    """

    def __init__(self, arr: list[int]) -> None:
        """
        Построение дерева отрезков за O(N).

        Args:
            arr: Исходный массив (0-индексация)
        """
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)

        # Копируем листья
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]

        # Строим внутренние узлы снизу вверх
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

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
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]

    def query(self, left: int, right: int) -> int:
        """
        Возвращает сумму на отрезке [left, right].
        Время: O(log N)

        Args:
            left: Левая граница (0-индексация, включительно)
            right: Правая граница (0-индексация, включительно)

        Returns:
            Сумма элементов arr[left] + ... + arr[right]
        """
        # Переходим к листьям
        left += self.n
        right += self.n

        result = 0

        # Двигаемся вверх, пока не встретимся
        while left <= right:
            # Если left — правый ребёнок, добавляем его и двигаемся вправо
            if left % 2 == 1:
                result += self.tree[left]
                left += 1

            # Если right — левый ребёнок, добавляем его и двигаемся влево
            if right % 2 == 0:
                result += self.tree[right]
                right -= 1

            # Переходим к родителям
            left //= 2
            right //= 2

        return result
