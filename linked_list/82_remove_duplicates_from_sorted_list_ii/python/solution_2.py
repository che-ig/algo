class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head:
            # Если следующий узел существует и имеет то же значение — нашли дубликаты
            if head.next and head.val == head.next.val:
                # Пропускаем все узлы с этим значением
                while head.next and head.val == head.next.val:
                    head = head.next
                # Вырезаем всю группу дубликатов
                prev.next = head.next
            else:
                # Узел уникален, двигаем prev
                prev = prev.next

            # Двигаем head вперед
            head = head.next

        return dummy.next
