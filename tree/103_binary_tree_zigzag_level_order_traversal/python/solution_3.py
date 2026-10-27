from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        """
        Зигзагообразный обход через DFS с использованием deque.
        Добавляем в начало/конец в зависимости от глубины.

        Args:
            root: Корень бинарного дерева

        Returns:
            Список списков значений узлов в зигзагообразном порядке
        """
        result: list[deque[int]] = []

        def dfs(node: TreeNode | None, depth: int) -> None:
            """
            Рекурсивный DFS с отслеживанием глубины.

            Args:
                node: Текущий узел
                depth: Текущая глубина (уровень)
            """
            if not node:
                return

            # Если это первый узел на данном уровне — создаём deque
            if depth == len(result):
                result.append(deque())

            # Чередование направления через чётность глубины
            if depth % 2 == 0:
                # Чётный уровень: слева направо
                result[depth].append(node.val)  # O(1) в конец
            else:
                # Нечётный уровень: справа налево
                result[depth].appendleft(node.val)  # O(1) в начало

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)

        # Преобразуем deque в списки для возврата
        return [list(level) for level in result]
