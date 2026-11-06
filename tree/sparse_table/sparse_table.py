import math


class SparseTable:
    def __init__(self, arr: list[int]) -> None:
        """
        Строит разреженную таблицу для массива arr.
        Время: O(N log N), Память: O(N log N)
        """
        self.n = len(arr)
        if self.n == 0:
            return

        # ПРЕДПОДСЧЕТ ЛОГАРИФМОВ
        # log_table[i] = floor(log2(i)) для всех i от 1 до n
        self.log_table = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            # математическое обоснование
            # floor(log2(i)) = floor(log2(i // 2)) + 1
            self.log_table[i] = self.log_table[i // 2] + 1

        # Максимальная степень двойки
        self.k_max = self.log_table[self.n] + 1

        # Таблица: table[k][i] = минимум на отрезке [i, i + 2^k - 1]
        self.table: list[list[int]] = [[0] * self.n for _ in range(self.k_max)]

        # База: k=0 (отрезки длины 1)
        for i in range(self.n):
            self.table[0][i] = arr[i]

        # Заполнение таблицы для k = 1, 2, ..., k_max
        for k in range(1, self.k_max):
            step = 1 << (k - 1)  # 2^(k-1)
            for i in range(self.n - (1 << k) + 1):
                self.table[k][i] = min(
                    self.table[k - 1][i], self.table[k - 1][i + step]
                )

    def query(self, left: int, right: int) -> int:
        """
        Минимум на отрезке [left, right] за O(1).
        Использует предподсчитанные логарифмы.
        """
        if left > right:
            raise ValueError("left должен быть <= right")

        # БЫСТРО: просто берем из массива вместо math.log2()
        length = right - left + 1
        k = self.log_table[length]

        # Два перекрывающихся отрезка длины 2^k
        return min(self.table[k][left], self.table[k][right - (1 << k) + 1])


def run_tests() -> None:
    test_cases: list[tuple[list[int], list[tuple[int, int, int]], str]] = [
        (
            [3, 1, 4, 1, 5, 9, 2, 6],
            [
                (0, 7, 1),  # весь массив
                (2, 6, 1),  # [4, 1, 5, 9, 2]
                (0, 3, 1),  # [3, 1, 4, 1]
                (4, 7, 2),  # [5, 9, 2, 6]
                (1, 1, 1),  # один элемент
            ],
            "Базовые запросы",
        ),
        (
            [5, 4, 3, 2, 1],
            [
                (0, 4, 1),  # убывающий массив
                (2, 4, 1),
                (0, 2, 3),
            ],
            "Убывающий массив",
        ),
        (
            [1, 2, 3, 4, 5],
            [
                (0, 4, 1),  # возрастающий массив
                (2, 4, 3),
                (0, 2, 1),
            ],
            "Возрастающий массив",
        ),
        (
            [7, 7, 7, 7, 7],
            [
                (0, 4, 7),  # все элементы одинаковые
                (1, 3, 7),
            ],
            "Одинаковые элементы",
        ),
        (
            [42],
            [
                (0, 0, 42),  # один элемент
            ],
            "Массив из одного элемента",
        ),
    ]

    print("=" * 70)
    print("ТЕСТИРОВАНИЕ SPARSE TABLE (RMQ)")
    print("=" * 70)

    passed = 0
    for arr, queries, description in test_cases:
        st = SparseTable(arr)
        print(f"\n📌 {description}: arr = {arr}")

        all_ok = True
        for left, right, expected in queries:
            result = st.query(left, right)
            if result == expected:
                print(f"   ✅ query({left}, {right}) = {result}")
            else:
                print(f"   ❌ query({left}, {right}) = {result} (ожидалось {expected})")
                all_ok = False

        if all_ok:
            passed += 1

    print("\n" + "=" * 70)
    print(f"Результат: {passed}/{len(test_cases)} тестов пройдено")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()
