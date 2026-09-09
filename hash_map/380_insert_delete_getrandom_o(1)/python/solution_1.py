import random

"""
Это классическая задача на системный дизайн структур данных. Главный подвох здесь в том, что ни одна стандартная структура данных не может выполнить все три операции за O(1) в одиночку:

    Массив (List): getRandom работает за O(1) (по индексу), insert за O(1) (в конец), но remove работает за O(N)O(N)O(N) (нужно сдвигать элементы).
    Хеш-таблица (Set/Dict): insert и remove работают за O(1), но getRandom работает за O(N)O(N)O(N), так как нельзя получить случайный элемент по индексу напрямую.

Решение: Комбинация Массива и Хеш-таблицы
Чтобы получить O(1) для всех операций, мы будем использовать обе структуры данных одновременно:

    Список (vals): хранит сами значения. Это дает нам возможность делать getRandom за O(1), выбирая случайный индекс.
    Словарь (val_to_index): хранит отображение значение -> его индекс в списке. Это дает нам возможность делать insert и remove за O(1).

Самая хитрая часть — это удаление. Чтобы удалить элемент из списка за O(1), мы используем трюк Swap and Pop (Поменять местами и удалить с конца), который мы обсуждали в предыдущей задаче. Поскольку порядок элементов для getRandom не важен, мы можем безболезненно менять их местами.
"""


class RandomizedSet:
    def __init__(self):
        # Список для хранения значений (обеспечивает O(1) для getRandom)
        self.vals = []
        # Словарь для хранения маппинга: значение -> его индекс в списке vals
        self.val_to_index = {}

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False

        # Добавляем значение в конец списка
        self.val_to_index[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False

        # 1. Находим индекс удаляемого элемента и последний элемент в списке
        idx_to_remove = self.val_to_index[val]
        last_val = self.vals[-1]

        # 2. Перемещаем последний элемент на место удаляемого (Swap)
        self.vals[idx_to_remove] = last_val

        # 3. Обновляем индекс последнего элемента в словаре
        self.val_to_index[last_val] = idx_to_remove

        # 4. Удаляем старый ключ из словаря и последний элемент из списка (Pop)
        del self.val_to_index[val]
        self.vals.pop()

        return True

    def getRandom(self) -> int:
        # random.choice выбирает случайный элемент из списка за O(1)
        return random.choice(self.vals)
