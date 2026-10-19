class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        """
        Удаляет дубликаты из отсортированного связного списка.
        """
        # Начинаем с головы списка
        curr = head

        # Проходим по списку, пока есть текущий узел и следующий за ним
        while curr and curr.next:
            # Если значения текущего и следующего узлов совпадают
            if curr.val == curr.next.val:
                # "Перепрыгиваем" через дубликат
                curr.next = curr.next.next
                # ВАЖНО: Мы НЕ двигаем curr вперед!
                # Нужно проверить новый curr.next, вдруг там тоже дубликат.
            else:
                # Если значения разные, значит последовательность дубликатов закончилась.
                # Двигаем указатель вперед.
                curr = curr.next

        return head
