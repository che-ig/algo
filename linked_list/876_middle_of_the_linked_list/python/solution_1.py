# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # time: O(n)
    # mem (дополнительная): O(1)
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        # изначально ставим slow и fast на голову
        slow = head  # будем двигать на 1 вперед
        fast = head  # будем двигать на 2 вперед
        # продолжаем сдвигать до тех пор пока fast and fast.next
        # советую нарисовать пару примеров и самому посмотреть что это работает
        # если непонятно почему это работает
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
