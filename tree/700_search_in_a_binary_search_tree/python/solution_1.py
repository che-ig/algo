from __future__ import annotations


# Сложность: O(H)
# O(H) по времени, O(H)
# O(H) по памяти (глубина рекурсии). Для сбалансированного BST: O(log N)
class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


"""
Главное свойство BST (Binary Search Tree):

    Все значения в левом поддереве меньше значения текущего узла.
    Все значения в правом поддереве больше значения текущего узла.

Это позволяет на каждом шаге отсекать половину дерева:

    Если val == node.val → нашли.
    Если val < node.val → ищем только в левом поддереве.
    Если val > node.val → ищем только в правом поддереве.

Таким образом, время работы — O(H)
O(H), где H
H — высота дерева, а не O(N)
O(N) как при полном обходе.
"""


class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        """
        Рекурсивный поиск в BST.
        Используем свойство: левое поддерево < node < правое поддерево.
        """
        # Базовые случаи: узел не найден или нашли искомый
        if root is None or root.val == val:
            return root

        # Если искомое значение меньше — идём влево
        if val < root.val:
            return self.searchBST(root.left, val)

        # Если больше — идём вправо
        return self.searchBST(root.right, val)


def tree_to_list(root: TreeNode | None) -> list[int | None]:
    """Сериализация дерева в список (level-order)."""
    from collections import deque

    if root is None:
        return []

    result: list[int | None] = []
    queue: deque[TreeNode | None] = deque([root])

    while queue:
        node = queue.popleft()
        if node is None:
            result.append(None)
        else:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

    while result and result[-1] is None:
        result.pop()

    return result


if __name__ == "__main__":
    # BST:
    #       4
    #      / \
    #     2   7
    #    / \
    #   1   3
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))

    # Пример 1: val = 2 → [2,1,3]
    result1 = Solution().searchBST(root, 2)
    print(tree_to_list(result1))  # [2, 1, 3]

    # Пример 2: val = 5 → [] (не найдено)
    result2 = Solution().searchBST(root, 5)
    print(tree_to_list(result2))  # []

    # Дополнительные проверки
    print(tree_to_list(Solution().searchBST(root, 4)))  # [4, 2, 7, 1, 3]
    print(tree_to_list(Solution().searchBST(root, 1)))  # [1]
    print(tree_to_list(Solution().searchBST(root, 7)))  # [7]
