class FenwickTree:
    """
    Дерево Фенвика с честной нулевой индексацией и оптимизированным построением за O(N).

    Использует операции:
      - i | (i + 1)  для движения вверх (update)
      - i & (i + 1)  для движения вниз  (query)

    Построение из массива выполняется за O(N) вместо O(N log N).
    """

    def __init__(self, size_or_arr: int | list[int]) -> None:
        """
        Args:
            size_or_arr: Размер дерева (int) или исходный массив (list[int]).
                         При передаче массива построение выполняется за O(N).
        """
        if isinstance(size_or_arr, int):
            self.n = size_or_arr
            self.tree = [0] * self.n
        else:
            self.n = len(size_or_arr)
            # Копируем исходный массив напрямую (0-индексация)
            self.tree = list(size_or_arr)
            # O(N) построение: проталкиваем значения к родителям
            self._build()

    def _build(self) -> None:
        """
        Строит дерево Фенвика за O(N).

        Для каждого узла i добавляем его текущее значение к родителю
        parent = i | (i + 1). Поскольку мы идём слева направо,
        к моменту обработки узла i все его "внутренние" дети уже
        учтены в tree[i], и мы корректно передаём агрегированную
        сумму наверх.
        """
        for i in range(self.n):
            parent = i | (i + 1)
            if parent < self.n:
                self.tree[parent] += self.tree[i]

    def add(self, i: int, delta: int) -> None:
        """
        Прибавляет delta к элементу arr[i] и обновляет все затронутые узлы.

        Движение вверх: i = i | (i + 1)
        """
        if i < 0 or i >= self.n:
            raise IndexError(f"Индекс {i} вне диапазона [0, {self.n - 1}]")

        while i < self.n:
            self.tree[i] += delta
            i |= i + 1

    def query_prefix(self, i: int) -> int:
        """
        Возвращает сумму префикса arr[0] + arr[1] + ... + arr[i].

        Движение вниз: i = (i & (i + 1)) - 1
        """
        if i < 0 or i >= self.n:
            raise IndexError(f"Индекс {i} вне диапазона [0, {self.n - 1}]")

        result = 0
        while i >= 0:
            result += self.tree[i]
            i = (i & (i + 1)) - 1
        return result

    def query_range(self, left: int, right: int) -> int:
        """
        Возвращает сумму элементов на отрезке [left, right].
        """
        if left < 0 or right >= self.n or left > right:
            raise IndexError(
                f"Некорректный диапазон [{left}, {right}] для массива размера {self.n}"
            )

        if left == 0:
            return self.query_prefix(right)
        return self.query_prefix(right) - self.query_prefix(left - 1)

    def get(self, index: int) -> int:
        """Возвращает значение элемента arr[index]."""
        return self.query_range(index, index)

    def __repr__(self) -> str:
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
