from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Идея: Сначала находим родителей всех узлов (через BFS/DFS),
# потом поднимаемся от p вверх, помечая предков, затем поднимаемся от
# q — первый помеченный предок и есть LCA.
class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode | None, p: TreeNode, q: TreeNode
    ) -> TreeNode | None:
        """
        Итеративное решение через словарь родителей.

        Идея:
        1. BFS: для каждого узла запоминаем его родителя
        2. Поднимаемся от p вверх, помечая всех предков в set
        3. Поднимаемся от q вверх — первый помеченный предок = LCA

        Args:
            root: Корень бинарного дерева
            p: Первый узел
            q: Второй узел

        Returns:
            Наименьший общий предок узлов p и q
        """
        # Словарь: узел → его родитель
        parent: dict[TreeNode, TreeNode | None] = {root: None}

        # Очередь для BFS
        queue: deque[TreeNode] = deque([root])

        # BFS: заполняем словарь родителей
        # Останавливаемся, когда нашли обоих p и q
        while queue:
            node = queue.popleft()

            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            if node.right:
                parent[node.right] = node
                queue.append(node.right)

        # Собираем всех предков p (включая сам p)
        ancestors_of_p: set[TreeNode] = set()
        current: TreeNode | None = p
        while current is not None:
            ancestors_of_p.add(current)
            current = parent[current]

        # Поднимаемся от q вверх — первый предок из ancestors_of_p = LCA
        current = q
        while current is not None:
            if current in ancestors_of_p:
                return current
            current = parent[current]

        # По условию p и q всегда существуют в дереве, поэтому до сюда не дойдём
        return None
