class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        """
        Слижает два отсортированных связных списка в один отсортированный.
        """
        # 1. Создаем Dummy Node — он будет стоять перед головой результата
        dummy = ListNode(0)

        # tail — указатель на последний узел результирующего списка.
        # Изначально он указывает на dummy.
        tail = dummy

        # 2. Пока оба списка не пусты, сравниваем их головы
        while list1 and list2:
            if list1.val <= list2.val:
                # Узел из list1 меньше или равен — пришиваем его к результату
                tail.next = list1
                list1 = list1.next  # Двигаем голову list1 вперед
            else:
                # Узел из list2 меньше — пришиваем его
                tail.next = list2
                list2 = list2.next  # Двигаем голову list2 вперед

            # В любом случае tail сдвигается на только что добавленный узел
            tail = tail.next

        # 3. Один из списков закончился. Пришиваем остаток второго списка.
        # Здесь не нужно идти по остатку — просто привязываем его целиком,
        # так как он уже отсортирован.
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        # 4. Возвращаем настоящий head результата (следующий за dummy)
        return dummy.next
