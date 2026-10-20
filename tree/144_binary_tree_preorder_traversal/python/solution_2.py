# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def preorderTraversal(self, root):
        """
        Итеративный preorder traversal бинарного дерева.
        Использует явный стек для симуляции рекурсии.
        """
        if not root:
            return []

        # Инициализируем стек с корневым узлом
        stack = [root]
        result = []

        # Пока стек не пуст
        while stack:
            # Извлекаем узел из стека (LIFO)
            node = stack.pop()

            # Добавляем значение узла в результат (обработка Root)
            result.append(node.val)

            # Сначала добавляем ПРАВОГО ребенка (если есть)
            # Он будет обработан ПОСЛЕ левого, так как стек LIFO
            if node.right:
                stack.append(node.right)

            # Затем добавляем ЛЕВОГО ребенка (если есть)
            # Он окажется на вершине стека и будет обработан СЛЕДУЮЩИМ
            if node.left:
                stack.append(node.left)

        return result
