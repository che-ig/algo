# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # time: O(n)
    # mem: O(1)
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        # на каждом шаге curr двигаем по листу на 1 ноду вперед,
        # а prev - поддерживает массив в котором будет ответ, т е

        # если есть изначально массив
        # 1 -> 2 -> 3 -> 4 -> 5 -> None

        # то через несколько шагов он будет таким
        # None <- 1 <- 2      3 -> 4 -> 5 -> None
        #            prev    curr

        # таким образом в prev мы получим конечный ответ
        prev = None
        curr = head
        while curr:
            tmp = curr
            curr = curr.next
            tmp.next = prev
            prev = tmp
        return prev
