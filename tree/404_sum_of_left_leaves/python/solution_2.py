from __future__ import annotations


class TreeNode:
    """Узел бинарного дерева."""

    def __init__(
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        total = 0
        # Стек хранит пары: (узел, является_ли_он_левым_потомком)
        stack: list[tuple[TreeNode, bool]] = [(root, False)]

        while stack:
            node, is_left = stack.pop()

            # Если это лист И при этом левый потомок — учитываем его
            if node.left is None and node.right is None and is_left:
                total += node.val
                continue  # у листа детей нет, дальше идти некуда

            # Добавляем детей в стек с соответствующей пометкой
            if node.right is not None:
                stack.append((node.right, False))  # правый потомок
            if node.left is not None:
                stack.append((node.left, True))  # левый потомок

        return total
