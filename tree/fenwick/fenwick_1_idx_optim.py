class FenwickTree:
    """
    Дерево Фенвика (Binary Indexed Tree) с нулевой индексацией.

    Поддерживает:
    - Построение из массива за O(N)
    - Точечное обновление: O(log N)
    - Запрос суммы на префиксе: O(log N)
    - Запрос суммы на отрезке: O(log N)

    Внутренне использует 1-индексацию для корректной работы битовых операций.
    """

    def __init__(self, size_or_arr: int | list[int]) -> None:
        """
        Инициализация дерева Фенвика.

        Args:
            size_or_arr: Размер дерева (int) или исходный массив (list[int]).
                         При передаче массива построение выполняется за O(N).
        """
        if isinstance(size_or_arr, int):
            self.n = size_or_arr
            self.tree = [0] * (self.n + 1)
        else:
            self.n = len(size_or_arr)
            # Копируем исходный массив в tree со сдвигом на +1 (1-индексация)
            self.tree = [0] + list(size_or_arr)
            # O(N) построение: проталкиваем значение каждого узла к его родителю
            self._build()

    def _build(self) -> None:
        """
        Строит дерево Фенвика за O(N).

        Для каждого узла i добавляем его текущее значение к родителю
        parent = i + lowbit(i). Поскольку мы идём слева направо,
        к моменту обработки узла i все его "внутренние" дети уже
        учтены в tree[i], и мы корректно передаём агрегированную
        сумму наверх.
        """
        for i in range(1, self.n + 1):
            parent = i + (i & (-i))
            if parent <= self.n:
                self.tree[parent] += self.tree[i]

    def add(self, index: int, delta: int) -> None:
        """
        Добавляет delta к элементу на позиции index (0-индексация).

        Args:
            index: Индекс элемента (0 <= index < n)
            delta: Значение для добавления (может быть отрицательным)
        """
        if index < 0 or index >= self.n:
            raise IndexError(f"Индекс {index} вне диапазона [0, {self.n - 1}]")

        i = index + 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)

    def query_prefix(self, index: int) -> int:
        """
        Возвращает сумму элементов на префиксе [0, index] (0-индексация).

        Args:
            index: Правая граница префикса (0 <= index < n)

        Returns:
            Сумма элементов arr[0] + arr[1] + ... + arr[index]
        """
        if index < 0 or index >= self.n:
            raise IndexError(f"Индекс {index} вне диапазона [0, {self.n - 1}]")

        i = index + 1
        result = 0
        while i > 0:
            result += self.tree[i]
            i -= i & (-i)
        return result

    def query_range(self, left: int, right: int) -> int:
        """
        Возвращает сумму элементов на отрезке [left, right] (0-индексация).

        Args:
            left: Левая граница отрезка (0 <= left <= right < n)
            right: Правая граница отрезка (0 <= left <= right < n)

        Returns:
            Сумма элементов arr[left] + arr[left+1] + ... + arr[right]
        """
        if left < 0 or right >= self.n or left > right:
            raise IndexError(
                f"Некорректный диапазон [{left}, {right}] для массива размера {self.n}"
            )

        if left == 0:
            return self.query_prefix(right)

        return self.query_prefix(right) - self.query_prefix(left - 1)

    def get(self, index: int) -> int:
        """
        Возвращает значение элемента на позиции index (0-индексация).

        Args:
            index: Индекс элемента (0 <= index < n)

        Returns:
            Значение arr[index]
        """
        return self.query_range(index, index)

    def __repr__(self) -> str:
        """Строковое представление дерева."""
        elements = [self.get(i) for i in range(self.n)]
        return f"FenwickTree({elements})"


def test_optimized_build() -> None:
    """Проверяем, что O(N) построение даёт тот же результат, что и O(N log N)."""

    # Тест 1: сравнение с наивным построением
    arr = [3, 1, 4, 1, 5, 9, 2, 6]

    # O(N) версия
    bit_fast = FenwickTree(arr)

    # O(N log N) версия (эталон)
    bit_slow = FenwickTree(len(arr))
    for i, v in enumerate(arr):
        bit_slow.add(i, v)

    # Проверяем все возможные запросы
    for l in range(len(arr)):
        for r in range(l, len(arr)):
            assert bit_fast.query_range(l, r) == bit_slow.query_range(l, r), (
                f"Несовпадение на [{l}, {r}]: {bit_fast.query_range(l, r)} != {bit_slow.query_range(l, r)}"
            )

    print("✅ Тест 1: O(N) построение совпадает с O(N log N)")

    # Тест 2: после построения обновления работают корректно
    bit_fast.add(2, 10)  # arr[2]: 4 → 14
    assert bit_fast.get(2) == 14
    assert bit_fast.query_range(0, 7) == 41  # 31 + 10
    print("✅ Тест 2: обновления после O(N) построения работают")

    # Тест 3: пустой массив и массив из одного элемента
    assert FenwickTree([]).n == 0
    b1 = FenwickTree([42])
    assert b1.query_range(0, 0) == 42
    print("✅ Тест 3: краевые случаи")

    # Тест 4: производительность на большом массиве
    import time

    big_arr = list(range(100_000))

    start = time.perf_counter()
    FenwickTree(big_arr)
    elapsed = time.perf_counter() - start
    print(f"✅ Тест 4: построение 100 000 элементов за {elapsed * 1000:.2f} мс")


if __name__ == "__main__":
    test_optimized_build()
