from collections import deque


class Solution:
    def maxDepth(self, root):
        """
        Итеративное решение через BFS: считаем количество уровней.
        """
        if not root:
            return 0

        queue = deque([root])  # Очередь с корневым узлом
        depth = 0

        while queue:
            # Обрабатываем весь текущий уровень целиком
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()

                # Добавляем детей в очередь для следующего уровня
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # После обработки уровня увеличиваем счетчик глубины
            depth += 1

        return depth
