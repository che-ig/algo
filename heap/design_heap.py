class MinHeap:
    def __init__(self):
        self.arr = []

    def push(self, x):
        self.arr.append(x)
        self._shift_up(len(self.arr) - 1)

    def poptop(self):
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        self.arr.pop()  # удаляем последний элемент
        self._shift_down(0)

    def top(self):
        return self.arr[0]

    def empty(self):
        return len(self.arr) == 0

    def _shift_down(self, i: int):
        left_child_idx = i * 2 + 1
        right_child_idx = i * 2 + 2

        if left_child_idx >= len(self.arr):
            # нет ни левого ни правого ребенка - это лист
            # т к куча заполняется последовательно то если нет левого ребенка то и правого быть не может
            return
        # если тут значит как минимум есть левый ребенок
        # next_idx - индекс с которым будем пробывать swap текущего элемента
        # т е это индекс ребенка который имеет минимальное значение (или максимальное для кучи на максимум)
        next_idx, next_min_val = left_child_idx, self.arr[left_child_idx]

        # обновляем next_idx если правый ребенок есть и значение в нем меньше чем в левом
        # P.S. (для кучи на максимум нужно менять условие)
        if right_child_idx < len(self.arr) and self.arr[right_child_idx] < next_min_val:
            next_idx, next_min_val = right_child_idx, self.arr[right_child_idx]

        current_val = self.arr[i]
        # если значение в одном из детей меньше чем в текущей вершине, значит меняем местами и просеиваем дальше
        if next_min_val < current_val:
            self.arr[i], self.arr[next_idx] = self.arr[next_idx], self.arr[i]
            self._shift_down(next_idx)

    def _shift_up(self, i: int):
        if i == 0:
            return
        parent_idx = (i - 1) // 2
        # если родитель больше, то просеиваем т к куча на минимум
        if (
            self.arr[parent_idx] > self.arr[i]
        ):  # для кучи на макимум менять уловие нужно
            # меняем местами значения и продолжаем просеивание
            self.arr[parent_idx], self.arr[i] = self.arr[i], self.arr[parent_idx]
            self._shift_up(parent_idx)
