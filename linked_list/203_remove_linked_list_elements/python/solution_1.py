from typing import Optional

# Определение для singly-linked list (обычно уже дано в условии LeetCode).
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        Удаляет все узлы со значением val из связного списка.
        """
        # 1. Создаем фиктивный узел (Dummy Node).
        # Его значение не важно (ставим 0 или -1).
        # Он "притворяется" узлом, который стоит перед head.
        dummy = ListNode(0)
        dummy.next = head

        # curr — указатель, который будет проверять СЛЕДУЮЩИЙ узел.
        # Начинаем с dummy, чтобы иметь возможность удалить сам head.
        curr = dummy

        # 2. Проходим по списку, пока есть следующий узел
        while curr.next:
            # Если следующий узел нужно удалить
            if curr.next.val == val:
                # "Перепрыгиваем" через него: указываем curr.next на узел после удаляемого.
                # Удаляемый узел просто отсоединяется от списка.
                curr.next = curr.next.next
                # ВАЖНО: мы НЕ двигаем curr вперед!
                # Нужно проверить новый curr.next, потому что он тоже может быть равен val.
            else:
                # Если следующий узел удалять не нужно, просто двигаем указатель вперед
                curr = curr.next

        # 3. Возвращаем новый head.
        # Если head был удален, dummy.next будет указывать на следующий за ним узел.
        # Если head не был удален, dummy.next по-прежнему указывает на исходный head.
        return dummy.next
