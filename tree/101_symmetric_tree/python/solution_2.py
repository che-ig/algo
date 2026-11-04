from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        """
        Проверка симметричности дерева через BFS.

        Идея:
        - В очередь кладём пары узлов, которые должны быть зеркальными
        - Начинаем с (root.left, root.right)
        - На каждом шаге сравниваем узлы в паре
        - Добавляем в очередь детей в зеркальном порядке:
          * (left.left, right.right) — внешние пары
          * (left.right, right.left) — внутренние пары

        Args:
            root: Корень бинарного дерева

        Returns:
            True, если дерево симметрично относительно центра
        """
        # Пустое дерево или дерево из одного узла симметрично
        if not root:
            return True

        # Очередь хранит пары узлов, которые должны быть зеркальными
        queue: deque[tuple[TreeNode | None, TreeNode | None]] = deque()
        queue.append((root.left, root.right))

        while queue:
            left, right = queue.popleft()

            # Оба узла пустые — это нормально, продолжаем
            if not left and not right:
                continue

            # Один узел пустой, другой нет — нарушение симметрии
            if not left or not right:
                return False

            # Оба узла существуют, но значения разные — нарушение симметрии
            if left.val != right.val:
                return False

            # Оба узла равны — добавляем их детей в очередь
            # ВАЖНО: в зеркальном порядке!
            queue.append((left.left, right.right))  # внешние пары
            queue.append((left.right, right.left))  # внутренние пары

        return True
