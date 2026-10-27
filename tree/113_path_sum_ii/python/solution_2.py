class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        """
        Находит все пути от корня до листьев с суммой, равной targetSum.
        Итеративный подход через явный стек.

        Args:
            root: Корень бинарного дерева
            targetSum: Целевая сумма значений в пути

        Returns:
            Список списков значений узлов для каждого подходящего пути
        """
        if not root:
            return []

        result: list[list[int]] = []

        # Стек хранит кортежи: (узел, накопленный путь, оставшаяся сумма)
        stack: list[tuple[TreeNode, list[int], int]] = [(root, [], targetSum)]

        while stack:
            # Извлекаем узел, его путь и оставшуюся сумму
            node, path, remaining_sum = stack.pop()

            # Если это лист — проверяем сумму
            if not node.left and not node.right:
                if remaining_sum == node.val:
                    result.append(path + [node.val])
                continue

            # Иначе добавляем детей в стек с обновлённым путём и суммой
            # Важно: сначала правый, потом левый (чтобы левый обработался первым)
            if node.right:
                stack.append((node.right, path + [node.val], remaining_sum - node.val))
            if node.left:
                stack.append((node.left, path + [node.val], remaining_sum - node.val))

        return result
