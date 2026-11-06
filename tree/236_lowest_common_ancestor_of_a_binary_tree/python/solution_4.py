class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode | None, p: TreeNode, q: TreeNode
    ) -> TreeNode | None:
        """
        Backtracking-подобное решение: ищем пути от корня до p и q.
        """

        def find_path(
            node: TreeNode | None, target: TreeNode, path: list[TreeNode]
        ) -> bool:
            """
            Находит путь от node до target через backtracking.
            Returns True, если путь найден.
            """
            if not node:
                return False

            # Добавляем текущий узел в путь
            path.append(node)

            # Если нашли target — путь найден
            if node == target:
                return True

            # Ищем в левом поддереве
            if find_path(node.left, target, path):
                return True

            # Ищем в правом поддереве
            if find_path(node.right, target, path):
                return True

            # Откат: убираем узел из пути (backtrack!)
            path.pop()
            return False

        # Находим пути от корня до p и q
        path_p: list[TreeNode] = []
        path_q: list[TreeNode] = []

        find_path(root, p, path_p)
        find_path(root, q, path_q)

        # Находим последний общий узел в путях
        lca = None
        for node_p, node_q in zip(path_p, path_q):
            if node_p == node_q:
                lca = node_p
            else:
                break

        return lca
