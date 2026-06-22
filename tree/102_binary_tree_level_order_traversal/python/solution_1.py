# Definition for a binary tree node.
from __future__ import annotations


class TreeNode:
    def __init__(
        self, val=0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # time: O(n)
    # mem: O(n)
    def preOrder(
        self, node: TreeNode | None, level: int, levels: list[list[int]]
    ) -> list[list[int]]:
        if node is None:
            return levels
        if level == len(levels):
            levels.append([])
        # делаем preOrder обход и добавляем вершину на текущий уровень в конец списка
        levels[level].append(node.val)
        levels = self.preOrder(node.left, level + 1, levels)
        levels = self.preOrder(node.right, level + 1, levels)
        return levels

    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        return self.preOrder(root, 0, [])
