from __future__ import annotations

from collections import deque


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
        Итеративное инвертирование через BFS.
        Используем очередь для обхода в ширину.
        """
        if root is None:
            return None

        queue: deque[TreeNode] = deque([root])

        while queue:
            node = queue.popleft()

            # Меняем местами потомков
            node.left, node.right = node.right, node.left

            # Добавляем детей в очередь (если они есть)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        return root
