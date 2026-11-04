class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Идея: Находим путь от корня до p и путь от корня до q. Последний общий узел в этих путях — LCA.
class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode | None, p: TreeNode, q: TreeNode
    ) -> TreeNode | None:
        """
        Решение через поиск путей от корня до p и q.

        Идея:
        1. Находим путь от корня до p
        2. Находим путь от корня до q
        3. Последний общий узел в обоих путях — LCA
        """

        def find_path(root: TreeNode | None, target: TreeNode) -> list[TreeNode]:
            """Находит путь от корня до target."""
            if root is None:
                return []
            if root == target:
                return [root]

            left_path = find_path(root.left, target)
            if left_path:
                return [root] + left_path

            right_path = find_path(root.right, target)
            if right_path:
                return [root] + right_path

            return []

        # Находим пути от корня до p и q
        path_p = find_path(root, p)
        path_q = find_path(root, q)

        # Ищем последний общий узел
        lca = None
        for node_p, node_q in zip(path_p, path_q):
            if node_p == node_q:
                lca = node_p
            else:
                break

        return lca
