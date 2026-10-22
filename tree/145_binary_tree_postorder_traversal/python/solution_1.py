class Solution:
    def postorderTraversal(self, root):
        """
        Итеративный postorder traversal через модифицированный preorder.

        Идея:
        1. Обходим дерево в порядке Root → Right → Left (как preorder, но сначала правый ребенок)
        2. Разворачиваем результат, получая Left → Right → Root
        """
        if not root:
            return []

        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)

            # Сначала добавляем ЛЕВОГО ребенка (он будет обработан ПОСЛЕ правого)
            if node.left:
                stack.append(node.left)

            # Затем добавляем ПРАВОГО ребенка (он окажется на вершине стека)
            if node.right:
                stack.append(node.right)

        # Разворачиваем результат: Root→Right→Left превращается в Left→Right→Root
        return result[::-1]
