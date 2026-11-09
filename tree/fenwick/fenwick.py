class FenwickTree:
    """
    Дерево Фенвика с честной нулевой индексацией.

    Использует операции:
      - i | (i + 1)  для движения вверх (update)
      - i & (i + 1)  для движения вниз  (query)

    Никаких сдвигов на +1 внутри — индексы 0..n-1 используются напрямую.
    """

    def __init__(self, size_or_arr: int | list[int]) -> None:
        """
        Args:
            size_or_arr: Размер дерева (int) или исходный массив (list[int]).
        """
        if isinstance(size_or_arr, int):
            self.n = size_or_arr
            self.tree = [0] * self.n
        else:
            self.n = len(size_or_arr)
            self.tree = [0] * self.n
            for i, val in enumerate(size_or_arr):
                self.add(i, val)

    def add(self, i: int, delta: int) -> None:
        """
        Прибавляет delta к элементу arr[i] и обновляет все затронутые узлы.

        Движение вверх: i = i | (i + 1)
        """
        if i < 0 or i >= self.n:
            raise IndexError(f"Индекс {i} вне диапазона [0, {self.n - 1}]")

        while i < self.n:
            self.tree[i] += delta
            i = i | (i + 1)  # переход к следующему ответственному узлу

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
            i = (i & (i + 1)) - 1  # переход к предыдущему блоку
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


def run_tests() -> None:
    print("=" * 70)
    print("ТЕСТИРОВАНИЕ FENWICK TREE (честная 0-индексация)")
    print("=" * 70)

    passed = 0
    total = 0

    # 1. Базовые запросы
    print("\n📌 1. Базовые запросы:")
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    bit = FenwickTree(arr)

    tests = [
        (bit.query_range(0, 7), 31, "сумма всего [0,7]"),
        (bit.query_range(2, 5), 19, "сумма [2,5] = 4+1+5+9"),
        (bit.query_range(0, 3), 9, "сумма [0,3] = 3+1+4+1"),
        (bit.query_range(4, 7), 22, "сумма [4,7] = 5+9+2+6"),
        (bit.query_prefix(5), 23, "префикс [0,5]"),
        (bit.query_prefix(0), 3, "префикс [0,0]"),
        (bit.get(3), 1, "отдельный элемент arr[3]"),
        (bit.get(7), 6, "последний элемент arr[7]"),
    ]
    for got, exp, desc in tests:
        total += 1
        if got == exp:
            print(f"   ✅ {desc}: {got}")
            passed += 1
        else:
            print(f"   ❌ {desc}: ожидалось {exp}, получено {got}")

    # 2. Обновления
    print("\n📌 2. Точечные обновления:")
    bit.add(2, 10)  # arr[2]: 4 → 14
    bit.add(5, -9)  # arr[5]: 9 → 0

    tests = [
        (bit.get(2), 14, "обновлённый arr[2]"),
        (bit.get(5), 0, "обновлённый arr[5]"),
        (bit.query_range(0, 7), 32, "новая сумма всего (31+10-9)"),
        (bit.query_range(2, 5), 20, "новая сумма [2,5] = 14+1+5+0"),
    ]
    for got, exp, desc in tests:
        total += 1
        if got == exp:
            print(f"   ✅ {desc}: {got}")
            passed += 1
        else:
            print(f"   ❌ {desc}: ожидалось {exp}, получено {got}")

    # 3. Краевые случаи
    print("\n📌 3. Краевые случаи:")

    b1 = FenwickTree([42])
    total += 1
    if b1.query_range(0, 0) == 42:
        print(f"   ✅ размер 1: {b1.query_range(0, 0)}")
        passed += 1
    else:
        print(f"   ❌ размер 1")

    b_neg = FenwickTree([-5, 10, -3, 8])
    total += 1
    if b_neg.query_range(0, 3) == 10:
        print(f"   ✅ отрицательные числа: {b_neg.query_range(0, 3)}")
        passed += 1
    else:
        print(f"   ❌ отрицательные числа")

    b_zero = FenwickTree(5)
    total += 1
    if b_zero.query_range(0, 4) == 0:
        print(f"   ✅ пустое дерево: {b_zero.query_range(0, 4)}")
        passed += 1
    else:
        print(f"   ❌ пустое дерево")

    # 4. Стресс-тест
    print("\n📌 4. Стресс-тест (10 000 операций):")
    import random

    random.seed(42)

    class Naive:
        def __init__(self, arr):
            self.arr = arr[:]

        def add(self, i, d):
            self.arr[i] += d

        def query(self, l, r):
            return sum(self.arr[l : r + 1])

    N, Q = 500, 10000
    initial = [random.randint(-100, 100) for _ in range(N)]
    bit = FenwickTree(initial)
    naive = Naive(initial)

    stress_ok = True
    for _ in range(Q):
        op = random.randint(0, 1)
        if op == 0:
            idx = random.randint(0, N - 1)
            delta = random.randint(-50, 50)
            bit.add(idx, delta)
            naive.add(idx, delta)
        else:
            l = random.randint(0, N - 1)
            r = random.randint(l, N - 1)
            if bit.query_range(l, r) != naive.query(l, r):
                stress_ok = False
                break

    total += 1
    if stress_ok:
        print(f"   ✅ стресс-тест пройден ({Q} операций)")
        passed += 1
    else:
        print(f"   ❌ стресс-тест провален")

    # 5. Инвариант
    print("\n📌 5. Инвариант get(i) == arr[i]:")
    arr2 = [7, -2, 0, 15, 4, 100, -50]
    bit2 = FenwickTree(arr2)
    inv_ok = all(bit2.get(i) == arr2[i] for i in range(len(arr2)))
    total += 1
    if inv_ok:
        print(f"   ✅ инвариант выполняется для всех индексов")
        passed += 1
    else:
        print(f"   ❌ инвариант нарушен")

    print("\n" + "=" * 70)
    print(f"🏁 ИТОГ: {passed} / {total} тестов пройдено")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()
