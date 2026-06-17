# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getVal(self, node: ListNode):
        if node is None:
            return float("inf")
        return node.val

    # time: O(n)
    # mem: O(1)
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        curr = stab = ListNode()
        while list1 is not None or list2 is not None:
            if self.getVal(list1) < self.getVal(list2):
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        return stab.next
