from __future__ import annotations


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        """
        Рекурсивная проверка валидности BST.
        Для каждого узла передаём допустимый диапазон (min_val, max_val).
        """

        def validate(node: TreeNode | None, min_val: float, max_val: float) -> bool:
            if node is None:
                return True

            # Текущий узел должен быть строго в пределах (min_val, max_val)
            if node.val <= min_val or node.val >= max_val:
                return False

            # Для левого поддерева: верхняя граница = текущий узел
            # Для правого поддерева: нижняя граница = текущий узел
            return validate(node.left, min_val, node.val) and validate(
                node.right, node.val, max_val
            )

        return validate(root, float("-inf"), float("inf"))
