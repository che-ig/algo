from __future__ import annotations

from collections import deque


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


"""
Если дерево очень широкое, BFS может быть выгоднее по памяти — используем deque.
"""


class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if root is None:
            return False

        queue: deque[tuple[TreeNode, int]] = deque([(root, root.val)])

        while queue:
            node, current_sum = queue.popleft()

            if node.left is None and node.right is None and current_sum == targetSum:
                return True

            if node.left is not None:
                queue.append((node.left, current_sum + node.left.val))
            if node.right is not None:
                queue.append((node.right, current_sum + node.right.val))

        return False
