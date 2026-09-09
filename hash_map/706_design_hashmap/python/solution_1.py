class MyHashMap:
    def __init__(self):
        # Выбираем простое число для размера массива, чтобы минимизировать коллизии
        # (простые числа лучше распределяют остатки при делении)
        self.capacity = 1009
        # Создаем массив пустых списков (корзин)
        self.buckets = [[] for _ in range(self.capacity)]

    def _hash(self, key: int) -> int:
        # Простая хеш-функция: остаток от деления на размер массива
        return key % self.capacity

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        bucket = self.buckets[idx]

        # Проверяем, есть ли уже такой ключ в корзине
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Обновляем значение
                return

        # Если ключа нет, добавляем новую пару в конец списка
        bucket.append((key, value))

    def get(self, key: int) -> int:
        idx = self._hash(key)
        bucket = self.buckets[idx]

        # Ищем ключ в корзине
        for k, v in bucket:
            if k == key:
                return v

        return -1  # Ключ не найден

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        bucket = self.buckets[idx]

        # Ищем ключ и удаляем его из корзины
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return

    def remove_optimize(self, key: int) -> None:
        idx = self._hash(key)
        bucket = self.buckets[idx]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                # --- ОПТИМИЗАЦИЯ O(1) ---
                # Меняем удаляемый элемент местами с последним
                bucket[i] = bucket[-1]
                # Удаляем последний элемент (это O(1) в Python)
                bucket.pop()
                return
