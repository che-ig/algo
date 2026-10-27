from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        """
        Зигзагообразный обход через BFS с разворотом списка.
        Более простой для понимания, но менее эффективен.
        """
        if not root:
            return []

        result: list[list[int]] = []
        queue: deque[TreeNode] = deque([root])
        left_to_right = True

        while queue:
            level_size = len(queue)
            current_level: list[int] = []

            # Собираем уровень как обычно (слева направо)
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Разворачиваем, если нужно справа налево
            if not left_to_right:
                current_level.reverse()

            result.append(current_level)
            left_to_right = not left_to_right

        return result
