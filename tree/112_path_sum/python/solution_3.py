from __future__ import annotations

"""
Вместо того чтобы накапливать сумму, мы вычитаем значение текущего узла из targetSum.
Тогда у листа нужно просто проверить, что остаток равен 0.
Это избавляет от хранения пары — в стеке лежат только узлы.
"""


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if root is None:
            return False

        stack: list[tuple[TreeNode, int]] = [(root, targetSum - root.val)]

        while stack:
            node, remaining = stack.pop()

            # Лист и остаток обнулился — путь найден
            if node.left is None and node.right is None and remaining == 0:
                return True

            if node.right is not None:
                stack.append((node.right, remaining - node.right.val))
            if node.left is not None:
                stack.append((node.left, remaining - node.left.val))

        return False
