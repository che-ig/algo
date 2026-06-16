# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # in:  1 -> 2 -> 3 -> None
    # out: 3 -> 2 -> 1 -> None
    # time: O(n)
    # mem: O(1)
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head
        while curr:
            tmp = curr
            curr = curr.next
            tmp.next = prev
            prev = tmp
        return prev

    # in:     1  ->  2  ->  3
    # out:        pre_mid

    # in:     1  ->  2  ->  3  ->  4
    # out:        pre_mid

    # in:     1  ->  2  ->  3  ->  4  ->  5
    # out:               pre_mid

    # time: O(n)
    # mem: O(1)
    def preMiddleNode(self, head: ListNode | None) -> ListNode | None:
        slow = head
        fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # time: O(n)
    # mem: O(1)
    def reorderList(self, head: ListNode | None) -> None:
        tmp = self.preMiddleNode(head)
        # in:   1 -> 2 -> 3 -> 4 -> 5
        #                tmp
        p2 = self.reverseList(tmp.next)
        # curr: 1 -> 2 -> 3 -> 4 <- 5
        #                     /     p2
        #               None <

        # будет зацикливание если не сделать None
        tmp.next = None
        # p1: 1 -> 2 -> 3 -> None
        # p2: 5 -> 4 -> None

        # merge lists
        # p2 - тот с кем дальше соединяем p1
        new_head = p1 = head
        while p2:
            p1_next = p1.next
            p1.next = p2
            p1 = p2
            p2 = p1_next
        return new_head


if __name__ == "__main__":
    values = [2, 4, 7, 9, 11]
    next_node = None
    for i in values:
        node_i = ListNode(val=i, next=next_node)
        next_node = node_i

    temp_head = node_i
    while temp_head:
        print(temp_head.val)
        temp_head = temp_head.next
