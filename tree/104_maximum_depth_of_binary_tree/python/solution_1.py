class Solution:
    def maxDepth(self, root):
        """
        Рекурсивное решение: глубина = 1 + max(глубина левого, глубина правого).
        """
        # Базовый случай: пустое дерево
        if not root:
            return 0

        # Рекурсивно считаем глубину левого и правого поддеревьев
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # Возвращаем 1 (текущий узел) + максимум из двух
        return 1 + max(left_depth, right_depth)
