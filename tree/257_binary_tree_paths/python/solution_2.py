# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        """
        Находит все пути от корня до листьев в бинарном дереве.
        Итеративный подход через явный стек.

        Args:
            root: Корень бинарного дерева

        Returns:
            Список строк вида "1->2->5" для каждого пути от корня до листа
        """
        if not root:
            return []

        result: list[str] = []

        # Стек хранит кортежи (узел, накопленный путь до этого узла)
        stack: list[tuple[TreeNode, str]] = [(root, "")]

        while stack:
            # Извлекаем узел и его путь из стека
            node, path = stack.pop()

            # Если это лист — добавляем полный путь в результат
            if not node.left and not node.right:
                result.append(path + str(node.val))
                continue

            # Иначе добавляем детей в стек с обновлённым путём
            # Важно: сначала правый, потом левый (чтобы левый обработался первым)
            if node.right:
                stack.append((node.right, path + str(node.val) + "->"))
            if node.left:
                stack.append((node.left, path + str(node.val) + "->"))

        return result
