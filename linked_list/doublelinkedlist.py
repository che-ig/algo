class DNode:
    """Узел двусвязного списка."""

    def __init__(self, value):
        self.value = value
        self.prev = None  # Ссылка на предыдущий узел
        self.next = None  # Ссылка на следующий узел


class DoublyLinkedList:
    """
    Классический двусвязный список с фиктивными узлами (sentinel nodes).

    Структура: Head <-> A <-> B <-> C <-> Tail

    Фиктивные узлы Head и Tail упрощают код, избавляя от проверок на None.

    Операции:
    - append: добавить в конец за O(1)
    - prepend: добавить в начало за O(1)
    - delete_node: удалить конкретный узел за O(1)
    - delete_value: удалить узел по значению за O(n)
    - forward_traverse: обход от начала к концу
    - backward_traverse: обход от конца к началу
    """

    def __init__(self):
        # Фиктивные узлы-стражи (dummy nodes)
        self.head = DNode(0)  # Фиктивная голова
        self.tail = DNode(0)  # Фиктивный хвост

        # Связываем их между собой
        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def prepend(self, value):
        """Добавляет элемент в начало списка (сразу после head). O(1)."""
        new_node = DNode(value)

        # Вставляем между head и head.next
        new_node.prev = self.head
        new_node.next = self.head.next

        self.head.next.prev = new_node
        self.head.next = new_node

        self.size += 1

    def append(self, value):
        """Добавляет элемент в конец списка (прямо перед tail). O(1)."""
        new_node = DNode(value)

        # Вставляем между tail.prev и tail
        new_node.prev = self.tail.prev
        new_node.next = self.tail

        self.tail.prev.next = new_node
        self.tail.prev = new_node

        self.size += 1

    def _remove_node(self, node):
        """
        Внутренний метод: удаляет конкретный узел из списка. O(1).
        Не проверяет, что узел действительно в списке — ответственность вызывающего.
        """
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def delete_node(self, node):
        """Удаляет конкретный узел (по ссылке). O(1)."""
        self._remove_node(node)

    def delete_value(self, value):
        """
        Удаляет первый узел с указанным значением. O(n).
        Возвращает True, если элемент найден и удалён.
        """
        current = self.head.next
        while current != self.tail:
            if current.value == value:
                self._remove_node(current)
                return True
            current = current.next
        return False

    def search(self, value):
        """Ищет узел по значению. O(n). Возвращает узел или None."""
        current = self.head.next
        while current != self.tail:
            if current.value == value:
                return current
            current = current.next
        return None

    def forward_traverse(self):
        """Обход от начала к концу. Возвращает список значений."""
        result = []
        current = self.head.next
        while current != self.tail:
            result.append(current.value)
            current = current.next
        return result

    def backward_traverse(self):
        """Обход от конца к началу. Возвращает список значений."""
        result = []
        current = self.tail.prev
        while current != self.head:
            result.append(current.value)
            current = current.prev
        return result

    def __str__(self):
        """Строковое представление (прямой обход)."""
        elements = self.forward_traverse()
        return "Head <-> " + " <-> ".join(map(str, elements)) + " <-> Tail"


# ===== Проверка двусвязного списка =====
if __name__ == "__main__":
    print("\n=== Двусвязный список ===")
    dll = DoublyLinkedList()

    dll.append(1)
    dll.append(2)
    dll.append(3)
    print(dll)  # Head <-> 1 <-> 2 <-> 3 <-> Tail

    dll.prepend(0)
    print(dll)  # Head <-> 0 <-> 1 <-> 2 <-> 3 <-> Tail

    print("Прямой обход:", dll.forward_traverse())  # [0, 1, 2, 3]
    print("Обратный обход:", dll.backward_traverse())  # [3, 2, 1, 0]

    # Удаляем конкретный узел по ссылке (O(1)!)
    node_2 = dll.search(2)
    dll.delete_node(node_2)
    print("После удаления 2:", dll)  # Head <-> 0 <-> 1 <-> 3 <-> Tail

    # Удаляем по значению
    dll.delete_value(0)
    print("После удаления 0:", dll)  # Head <-> 1 <-> 3 <-> Tail

    print("Размер:", dll.size)  # 2
