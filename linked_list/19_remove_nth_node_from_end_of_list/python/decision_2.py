# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ListNode dummy = new ListNode(0);
#     dummy.next = head;
#     ListNode first = dummy;
#     ListNode second = dummy;
#     // Advances first pointer so that the gap between first and second is n nodes apart
#     for (int i = 1; i <= n + 1; i++) {
#         first = first.next;
#     }
#     // Move first to the end, maintaining the gap
#     while (first != null) {
#         first = first.next;
#         second = second.next;
#     }
#     second.next = second.next.next;
#     return dummy.next;


class Solution:
    # time:      O(n), где n - длина списка
    # mem(доп):  O(1)
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummyNode = ListNode(val=0, next=head)

        fast = dummyNode
        for i in range(n + 1):
            fast = fast.next

        slow = dummyNode
        while fast is not None:
            slow = slow.next
            fast = fast.next

        # удаляем вершину
        slow.next = slow.next.next

        return dummyNode.next
