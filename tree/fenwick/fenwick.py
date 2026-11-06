import random


class FenwickTree:
    def __init__(self, size: int):
        # Массив на 1 больше, чтобы использовать 1-индексацию
        self.tree = [0] * (size + 1)
        self.size = size

    def add(self, i: int, delta: int) -> None:
        """
        Добавляет delta к элементу на позиции i (0-индексация).
        Время: O(log N)
        """
        i += 1  # Переходим к 1-индексации
        while i <= self.size:
            self.tree[i] += delta
            i += i & (-i)  # Магия: переходим к следующему ответственному узлу

    def query_prefix(self, i: int) -> int:
        """
        Возвращает сумму на префиксе [0, i] (0-индексация).
        Время: O(log N)
        """
        i += 1  # Переходим к 1-индексации
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & (-i)  # Магия: переходим к предыдущему ответственному узлу
        return res

    def query_range(self, l: int, r: int) -> int:
        """Сумма на отрезке [l, r] за O(log N)."""
        if l == 0:
            return self.query_prefix(r)
        return self.query_prefix(r) - self.query_prefix(l - 1)


# ==============================================================================
# Наивное решение для стресс-тестирования (Ground Truth)
# ==============================================================================


class NaiveArray:
    def __init__(self, arr: list[int]) -> None:
        self.arr = arr.copy()

    def add(self, i: int, delta: int) -> None:
        self.arr[i] += delta

    def query_range(self, l: int, r: int) -> int:
        return sum(self.arr[l : r + 1])


# ==============================================================================
# Тестовый раннер
# ==============================================================================


def run_tests() -> None:
    print("=" * 70)
    print("ТЕСТИРОВАНИЕ ДЕРЕВА ФЕНВИКА (BIT)")
    print("=" * 70)

    passed = 0
    total = 0

    # ---------------------------------------------------------
    # 1. Базовые тесты (ручная проверка)
    # ---------------------------------------------------------
    print("\n📌 1. Базовые операции:")
    base_arr = [1, 2, 3, 4, 5]
    bit = FenwickTree(base_arr)

    tests_basic = [
        (bit.query_range(0, 4), 15, "Сумма всего массива [0, 4]"),
        (bit.query_range(1, 3), 9, "Сумма подмассива [1, 3] (2+3+4)"),
        (bit.query_range(0, 0), 1, "Сумма одного элемента [0, 0]"),
        (bit.query_range(4, 4), 5, "Сумма последнего элемента [4, 4]"),
    ]

    for result, expected, desc in tests_basic:
        total += 1
        if result == expected:
            print(f"   ✅ {desc}: {result}")
            passed += 1
        else:
            print(f"   ❌ {desc}: ожидалось {expected}, получено {result}")

    # ---------------------------------------------------------
    # 2. Тесты на точечное обновление (Point Update)
    # ---------------------------------------------------------
    print("\n📌 2. Точечные обновления:")
    bit.add(2, 10)  # arr[2] было 3, стало 13. Массив: [1, 2, 13, 4, 5]

    tests_update = [
        (bit.query_range(0, 4), 25, "Сумма всего после обновления [0, 4]"),
        (bit.query_range(1, 3), 19, "Сумма [1, 3] после обновления (2+13+4)"),
        (bit.query_range(2, 2), 13, "Значение обновленного элемента [2, 2]"),
    ]

    for result, expected, desc in tests_update:
        total += 1
        if result == expected:
            print(f"   ✅ {desc}: {result}")
            passed += 1
        else:
            print(f"   ❌ {desc}: ожидалось {expected}, получено {result}")

    # ---------------------------------------------------------
    # 3. Краевые случаи (Edge Cases)
    # ---------------------------------------------------------
    print("\n📌 3. Краевые случаи:")

    # Массив из одного элемента
    bit1 = FenwickTree([42])
    total += 1
    if bit1.query_range(0, 0) == 42:
        print(f"   ✅ Массив из 1 элемента: {bit1.query_range(0, 0)}")
        passed += 1
    else:
        print(f"   ❌ Массив из 1 элемента")

    # Отрицательные числа
    bit_neg = FenwickTree([-5, 10, -3, 8])
    total += 1
    if bit_neg.query_range(0, 3) == 10:
        print(f"   ✅ Отрицательные числа (сумма): {bit_neg.query_range(0, 3)}")
        passed += 1
    else:
        print(f"   ❌ Отрицательные числа")

    # Обновление на отрицательное значение
    bit_neg.add(1, -10)  # arr[1] было 10, стало 0
    total += 1
    if bit_neg.query_range(1, 1) == 0:
        print(f"   ✅ Вычитание через add: {bit_neg.query_range(1, 1)}")
        passed += 1
    else:
        print(f"   ❌ Вычитание через add")

    # ---------------------------------------------------------
    # 4. СТРЕСС-ТЕСТ (Сравнение с наивным решением)
    # ---------------------------------------------------------
    print("\n📌 4. Стресс-тест (10 000 случайных операций):")
    random.seed(42)  # Для воспроизводимости

    N = 1000
    Q = 10000

    # Генерируем случайный начальный массив
    initial_arr = [random.randint(-100, 100) for _ in range(N)]

    bit_stress = FenwickTree(initial_arr)
    naive_stress = NaiveArray(initial_arr)

    stress_ok = True
    for _ in range(Q):
        # Случайно выбираем операцию: 0 - update, 1 - query
        op = random.randint(0, 1)

        if op == 0:
            # Точечное обновление
            idx = random.randint(0, N - 1)
            delta = random.randint(-50, 50)
            bit_stress.add(idx, delta)
            naive_stress.add(idx, delta)
        else:
            # Запрос суммы на отрезке
            l = random.randint(0, N - 1)
            r = random.randint(l, N - 1)

            res_bit = bit_stress.query_range(l, r)
            res_naive = naive_stress.query_range(l, r)

            if res_bit != res_naive:
                stress_ok = False
                print(f"   ❌ Рассинхронизация! l={l}, r={r}")
                print(f"      BIT: {res_bit}, Naive: {res_naive}")
                break

    total += 1
    if stress_ok:
        print(f"   ✅ Стресс-тест пройден успешно! ({Q} операций)")
        passed += 1
    else:
        print(f"   ❌ Стресс-тест провален.")

    # ---------------------------------------------------------
    # Итог
    # ---------------------------------------------------------
    print("\n" + "=" * 70)
    print(f"🏁 ИТОГ: Пройдено {passed} из {total} тестов.")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()
