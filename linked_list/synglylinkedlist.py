class SNode:
    """Узел односвязного списка."""

    def __init__(self, value):
        self.value = value
        self.next = None  # Ссылка на следующий узел


class SinglyLinkedList:
    """
    Классический односвязный список.

    Структура: Head -> A -> B -> C -> None

    Операции:
    - append: добавить в конец за O(n)
    - prepend: добавить в начало за O(1)
    - delete: удалить узел по значению за O(n)
    - search: найти узел по значению за O(n)
    - print: напечатать список
    """

    def __init__(self):
        self.head = None  # Голова списка (первый элемент)
        self.size = 0  # Количество элементов

    def prepend(self, value):
        """Добавляет элемент в начало списка. O(1)."""
        new_node = SNode(value)
        new_node.next = self.head  # Новый узел указывает на старую голову
        self.head = new_node  # Голова теперь — новый узел
        self.size += 1

    def append(self, value):
        """Добавляет элемент в конец списка. O(n)."""
        new_node = SNode(value)

        # Если список пуст, новый узел становится головой
        if self.head is None:
            self.head = new_node
            self.size += 1
            return

        # Иначе идём до последнего узла
        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node
        self.size += 1

    def delete(self, value):
        """
        Удаляет первый узел с указанным значением. O(n).
        Возвращает True, если элемент найден и удалён, иначе False.
        """
        # Если список пуст
        if self.head is None:
            return False

        # Если удаляем голову
        if self.head.value == value:
            self.head = self.head.next
            self.size -= 1
            return True

        # Ищем узел для удаления
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                # "Перепрыгиваем" через удаляемый узел
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next

        return False

    def search(self, value):
        """Ищет узел по значению. O(n). Возвращает узел или None."""
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None

    def to_list(self):
        """Преобразует список в Python list (для удобства тестирования)."""
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result

    def __str__(self):
        """Строковое представление списка."""
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.value))
            current = current.next
        return " -> ".join(elements) + " -> None"


# ===== Проверка односвязного списка =====
if __name__ == "__main__":
    print("=== Односвязный список ===")
    sll = SinglyLinkedList()

    sll.append(1)
    sll.append(2)
    sll.append(3)
    print(sll)  # 1 -> 2 -> 3 -> None

    sll.prepend(0)
    print(sll)  # 0 -> 1 -> 2 -> 3 -> None

    sll.delete(2)
    print(sll)  # 0 -> 1 -> 3 -> None

    print(sll.search(1))  # <SNode object>
    print(sll.search(99))  # None
    print(sll.to_list())  # [0, 1, 3]
