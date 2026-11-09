class FenwickTree:
    """
    Дерево Фенвика (Binary Indexed Tree) с нулевой индексацией.

    Поддерживает:
    - Точечное обновление: O(log N)
    - Запрос суммы на префиксе: O(log N)
    - Запрос суммы на отрезке: O(log N)

    Внутренне использует 1-индексацию для корректной работы битовых операций.
    """

    def __init__(self, size_or_arr: int | list[int]) -> None:
        """
        Инициализация дерева Фенвика.

        Args:
            size_or_arr: Размер дерева (int) или исходный массив (list[int])
        """
        if isinstance(size_or_arr, int):
            self.n = size_or_arr
            # Внутренний массив на 1 больше (1-индексация)
            self.tree = [0] * (self.n + 1)
        else:
            self.n = len(size_or_arr)
            self.tree = [0] * (self.n + 1)
            # Инициализация за O(N log N)
            for i, val in enumerate(size_or_arr):
                self.add(i, val)

    def add(self, index: int, delta: int) -> None:
        """
        Добавляет delta к элементу на позиции index (0-индексация).

        Args:
            index: Индекс элемента (0 <= index < n)
            delta: Значение для добавления (может быть отрицательным)
        """
        if index < 0 or index >= self.n:
            raise IndexError(f"Индекс {index} вне диапазона [0, {self.n - 1}]")

        # Сдвигаем к 1-индексации
        i = index + 1

        # Двигаемся ВВЕРХ по дереву, обновляя все узлы, которые включают index
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)  # Переход к следующему ответственному узлу

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

        # Сдвигаем к 1-индексации
        i = index + 1
        result = 0

        # Двигаемся ВНИЗ по дереву, собирая сумму
        while i > 0:
            result += self.tree[i]
            i -= i & (-i)  # Переход к предыдущему ответственному узлу

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

        # Сумма [left, right] = сумма [0, right] - сумма [0, left-1]
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


# ==============================================================================
# Примеры использования
# ==============================================================================


def demo():
    print("=" * 70)
    print("ДЕМО: Дерево Фенвика с нулевой индексацией")
    print("=" * 70)

    # Пример 1: Инициализация из массива
    print("\n📌 Пример 1: Инициализация из массива")
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    bit = FenwickTree(arr)
    print(f"Исходный массив: {arr}")
    print(f"Дерево Фенвика: {bit}")

    # Пример 2: Запрос суммы на отрезке
    print("\n📌 Пример 2: Запросы суммы")
    print(f"Сумма [0, 7] (весь массив): {bit.query_range(0, 7)}")  # 31
    print(f"Сумма [2, 5]: {bit.query_range(2, 5)}")  # 4+1+5+9 = 19
    print(f"Сумма [0, 3]: {bit.query_range(0, 3)}")  # 3+1+4+1 = 9

    # Пример 3: Точечное обновление
    print("\n📌 Пример 3: Точечное обновление")
    print(f"До обновления: arr[2] = {bit.get(2)}")
    bit.add(2, 10)  # Прибавляем 10 к arr[2]
    print(f"После add(2, 10): arr[2] = {bit.get(2)}")  # 14
    print(f"Новая сумма [2, 5]: {bit.query_range(2, 5)}")  # 14+1+5+9 = 29

    # Пример 4: Инициализация пустого дерева
    print("\n📌 Пример 4: Инициализация пустого дерева")
    bit2 = FenwickTree(5)
    print(f"Пустое дерево размера 5: {bit2}")
    bit2.add(0, 10)
    bit2.add(1, 20)
    bit2.add(2, 30)
    print(f"После добавлений: {bit2}")
    print(f"Сумма [0, 2]: {bit2.query_range(0, 2)}")  # 60

    # Пример 5: Отрицательные числа
    print("\n📌 Пример 5: Отрицательные числа")
    arr_neg = [-5, 10, -3, 8, -2]
    bit_neg = FenwickTree(arr_neg)
    print(f"Массив с отрицательными числами: {arr_neg}")
    print(f"Сумма [0, 4]: {bit_neg.query_range(0, 4)}")  # 8
    bit_neg.add(1, -10)  # arr[1] становится 0
    print(f"После add(1, -10): сумма [0, 4] = {bit_neg.query_range(0, 4)}")  # -2

    print("\n" + "=" * 70)


if __name__ == "__main__":
    demo()
