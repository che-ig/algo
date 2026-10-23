from __future__ import annotations


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        """
        Итеративный DFS. В стеке храним пары (узел, накопленная_сумма).
        """
        if root is None:
            return False

        # Стек пар: (узел, сумма от корня до этого узла включительно)
        stack: list[tuple[TreeNode, int]] = [(root, root.val)]

        while stack:
            node, current_sum = stack.pop()

            # Если это лист — проверяем, совпадает ли сумма с targetSum
            if node.left is None and node.right is None:
                if current_sum == targetSum:
                    return True
                continue  # лист — дальше идти некуда

            # Добавляем детей с обновлённой суммой
            if node.right is not None:
                stack.append((node.right, current_sum + node.right.val))
            if node.left is not None:
                stack.append((node.left, current_sum + node.left.val))

        # Ни один путь не дал нужной суммы
        return False
