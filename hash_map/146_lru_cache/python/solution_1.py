"""
Идея решения
Чтобы обеспечить сложность O(1) для обеих операций (get и put), нам нужно объединить две структуры данных:

    Хеш-таблица (словарь dict): обеспечивает поиск элемента по ключу за O(1).
    Двусвязный список (Doubly Linked List): позволяет за O(1) удалять узел из любого места и добавлять его в начало (или конец), чтобы отслеживать порядок использования.

Как это работает вместе:

    Словарь хранит пары key -> Node (где Node — это узел двусвязного списка).
    Двусвязный список хранит элементы в порядке их использования:
        Голова (Head): самый недавно использованный элемент (Most Recently Used, MRU).
        Хвост (Tail): самый давно использованный элемент (Least Recently Used, LRU), который будет удален при переполнении.
    Фиктивные узлы (Dummy nodes): мы добавляем фиктивные узлы в начало и конец списка, чтобы избежать проверок на None при добавлении/удалении (это делает код чище и быстрее).
"""


class Node:
    """Узел двусвязного списка."""

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Хеш-таблица: key -> Node

        # Фиктивные узлы для упрощения операций с двусвязным списком
        self.head = Node(0, 0)  # Самый недавно использованный (MRU)
        self.tail = Node(0, 0)  # Самый давно использованный (LRU)

        # Изначально список состоит только из фиктивных узлов, связанных друг с другом
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_node(self, node: Node) -> None:
        """Удаляет узел из двусвязного списка (O(1))."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node: Node) -> None:
        """Добавляет узел сразу после head, делая его MRU (O(1))."""
        node.prev = self.head
        node.next = self.head.next

        # Обновляем ссылки соседних узлов
        self.head.next.prev = node
        self.head.next = node

    def _move_to_head(self, node: Node) -> None:
        """Перемещает существующий узел в голову списка (O(1))."""
        self._remove_node(node)
        self._add_to_head(node)

    def _pop_tail(self) -> Node:
        """Удаляет и возвращает узел прямо перед tail (настоящий LRU) (O(1))."""
        lru_node = self.tail.prev
        self._remove_node(lru_node)
        return lru_node

    def get(self, key: int) -> int:
        """Возвращает значение по ключу или -1, если ключа нет."""
        if key not in self.cache:
            return -1

        # Ключ найден: перемещаем узел в голову (он стал MRU)
        node = self.cache[key]
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """Добавляет или обновляет пару ключ-значение."""
        if key in self.cache:
            # Если ключ уже есть, обновляем значение и перемещаем в голову
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            # Если ключа нет, создаем новый узел
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)

            # Проверяем, не превысили ли мы вместимость
            if len(self.cache) > self.capacity:
                # Удаляем LRU элемент из списка и из хеш-таблицы
                lru_node = self._pop_tail()
                del self.cache[lru_node.key]


# ===== Проверка на примере из условия =====
if __name__ == "__main__":
    lRUCache = LRUCache(2)

    lRUCache.put(1, 1)  # cache is {1=1}
    lRUCache.put(2, 2)  # cache is {1=1, 2=2}
    print(lRUCache.get(1))  # return 1
    lRUCache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    print(lRUCache.get(2))  # returns -1 (not found)
    lRUCache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    print(lRUCache.get(1))  # return -1 (not found)
    print(lRUCache.get(3))  # return 3
    print(lRUCache.get(4))  # return 4
