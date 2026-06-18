# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # time: O(n)
    # mem: O(1)
    def hasCycle(self, head: ListNode | None) -> bool:
        slow = head  # будем двигать на 1
        fast = head  # будем двигать на 2

        # сдвигаем указатели пока они не встретятся или пока мы не дойдем до конца списка
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
