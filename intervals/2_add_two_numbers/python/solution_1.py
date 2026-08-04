# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # time: O(n)
    # mem:  O(n)
    # Note: если разрешено менять входящие списки, то можно из них сделать
    # ответ и доп память будет O(1)
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        dummy = ListNode()
        # carry - остаток который будем переносить
        carry = 0
        # текущая нода, которая собирает ответ
        curr = dummy

        while l1 is not None or l2 is not None or carry != 0:
            # получаем текущее значение, если список закончился
            # то возвращаем 0
            l1Val = l1.val if l1 is not None else 0
            l2Val = l2.val if l2 is not None else 0

            sum = l1Val + l2Val + carry
            # sum % 10 - текущее число которое добавим к ответу
            newNode = ListNode(sum % 10)
            # sum // 10 - остаток который переносим
            carry = sum // 10

            curr.next = newNode
            curr = curr.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        return dummy.next
