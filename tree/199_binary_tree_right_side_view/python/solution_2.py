from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        result: list[int] = []
        queue: deque[TreeNode] = deque([root])

        while queue:
            level_size = len(queue)
            last_node_val: int = 0  # Сохраняем значение последнего узла

            # Обрабатываем все узлы уровня
            for _ in range(level_size):
                node = queue.popleft()
                last_node_val = node.val  # Перезаписываем на каждом шаге

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # После цикла last_node_val содержит значение ПРАВОГОMOST узла
            result.append(last_node_val)

        return result


class Solution_2:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        """
        Возвращает узлы, видимые с правой стороны дерева.
        Использует BFS: для каждого уровня берём последний узел.

        Args:
            root: Корень бинарного дерева

        Returns:
            Список значений узлов, видимых справа сверху вниз
        """
        if not root:
            return []

        result: list[int] = []
        queue: deque[TreeNode] = deque([root])

        while queue:
            # Фиксируем размер текущего уровня
            level_size = len(queue)

            # Обрабатываем все узлы уровня
            for i in range(level_size):
                node = queue.popleft()

                # Если это последний узел уровня — добавляем в результат
                if i == level_size - 1:
                    result.append(node.val)

                # Добавляем детей в очередь
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
