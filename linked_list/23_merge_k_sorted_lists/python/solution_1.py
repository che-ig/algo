# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # time:      O(k), где k - число списков
    # mem (доп): O(1)
    def get_min_node_idx(self, lists: List[ListNode | None]):
        # Функция находит индекс в котором текущая нода наименьшая
        min_list_node_val, min_list_node_idx = float("inf"), float("inf")
        for i, list_node in enumerate(lists):
            if list_node is None:
                continue
            if list_node.val < min_list_node_val:
                min_list_node_val = list_node.val
                min_list_node_idx = i
        if min_list_node_val == float("inf"):
            return None
        return min_list_node_idx

    # time:      O(n), где n - общее число вершин
    # mem (доп): O(1)
    # Note: Я переиспользую ноды из входящего списка
    # вы можете написать решение которое будет создавать новые ноды и не менять входящие
    def mergeKLists(self, lists: List[ListNode | None]) -> ListNode | None:
        # решение будет основано на "нескольких указателях"
        # т е мы каждый раз находин наименьший элемент на которые сейчас указывают
        # списки и двигаем указатель для этого списка.
        # продолжаем так делать пока все списки не станут указывать на None

        dummyNode = ListNode()
        curr = dummyNode

        # после того как голову нашли находим очередной минимальную ноду и добавляем к результату
        while True:
            min_node_idx = self.get_min_node_idx(lists)
            if min_node_idx is None:
                curr.next = None
                break
            curr.next = lists[min_node_idx]
            curr = curr.next
            lists[min_node_idx] = lists[min_node_idx].next
        return dummyNode.next
