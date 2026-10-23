from __future__ import annotations


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        """
        Итеративная проверка идентичности двух деревьев через DFS.
        В стеке храним пары соответствующих узлов из p и q.
        """
        stack: list[tuple[TreeNode | None, TreeNode | None]] = [(p, q)]

        while stack:
            node_p, node_q = stack.pop()

            # Оба None — эта пара совпадает, идём дальше
            if node_p is None and node_q is None:
                continue

            # Один None, другой нет — расхождение в структуре
            if node_p is None or node_q is None:
                return False

            # Значения различаются
            if node_p.val != node_q.val:
                return False

            # Оба узла валидны и равны — кладём детей в стек
            # (порядок не важен, так как мы просто проверяем соответствие)
            stack.append((node_p.left, node_q.left))
            stack.append((node_p.right, node_q.right))

        return True
