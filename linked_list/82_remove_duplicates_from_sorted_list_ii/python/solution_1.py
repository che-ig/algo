# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        Удаляет все узлы, имеющие дубликаты, оставляя только уникальные.
        """
        # Создаем Dummy Node, так как head может быть удален
        dummy = ListNode(0)
        dummy.next = head

        # prev — последний узел, который точно уникален и останется в списке
        prev = dummy

        # curr — текущий узел, который мы проверяем на дубликаты
        curr = head

        while curr:
            # "Разведчик" curr пробегает по всем дубликатам подряд
            while curr.next and curr.val == curr.next.val:
                curr = curr.next

            # Проверяем, сдвинулся ли curr
            if prev.next == curr:
                # Если prev.next всё ещё указывает на curr,
                # значит дубликатов не было. curr уникален!
                prev = prev.next
            else:
                # Если prev.next != curr, значит curr сдвинулся по дубликатам.
                # Вырезаем всю группу дубликатов, перенаправляя ссылку prev
                prev.next = curr.next

            # Двигаем curr на следующий узел для проверки
            curr = curr.next

        return dummy.next
