from __future__ import annotations


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        """
        Итеративное инвертирование через DFS.
        Используем стек для обхода дерева.
        """
        if root is None:
            return None

        stack: list[TreeNode] = [root]

        while stack:
            node = stack.pop()

            # Меняем местами потомков
            node.left, node.right = node.right, node.left

            # Добавляем детей в стек (если они есть)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)

        return root
