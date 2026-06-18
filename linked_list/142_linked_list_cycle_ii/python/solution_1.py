# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# почему это работает объяснено в статье
# https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi448Poi-v_AhWXrosKHY9NDNEQFnoECA4QAQ&url=https%3A%2F%2Fabhisekbunty94.medium.com%2Fwhy-does-floyds-cycle-detection-algorithm-work-59f61984dc3e&usg=AOvVaw2GhP_ctyrf_mvWUlJdmPTq&opi=89978449


class Solution:
    # time: O(n)
    # mem (доп): O(1)
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        slow = head  # будем двигать на 1
        fast = head  # будем двигать на 2

        # сдвигаем указатели пока они не встретятся или пока мы не дойдем до конца списка
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        # если дошли до конца списка, то возвращаем None т к тут нет цикла
        if fast is None or fast.next is None:
            return None

        # двигаемся от головы и от fast поинтера на 1 пока они не встретятся
        # место встречи и будет началом цикла
        result = head
        while result != fast:
            result = result.next
            fast = fast.next
        return result
