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
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        queue: deque[tuple[TreeNode | None, TreeNode | None]] = deque([(p, q)])

        while queue:
            node_p, node_q = queue.popleft()

            if node_p is None and node_q is None:
                continue
            if node_p is None or node_q is None:
                return False
            if node_p.val != node_q.val:
                return False

            queue.append((node_p.left, node_q.left))
            queue.append((node_p.right, node_q.right))

        return True
