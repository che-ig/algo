# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummyNode = ListNode(val=0, next=head)

        # находим длину списка с учетом dummyNode
        length = 0
        curr = dummyNode
        while curr is not None:
            curr = curr.next
            length += 1

        # доходим до (n-1)-ой вершины с конца
        curr = dummyNode
        for i in range(length - n - 1):
            curr = curr.next

        # удаляем вершину
        curr.next = curr.next.next

        return dummyNode.next
