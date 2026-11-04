# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        """
        Оптимальное решение: один проход снизу вверх.

        Идея:
        - Вычисляем высоту поддерева рекурсивно (postorder)
        - Одновременно проверяем условие баланса
        - Если нашли нарушение — возвращаем -1 (сигнал "не сбалансировано")
        - Это позволяет досрочно завершить обход

        Args:
            root: Корень бинарного дерева

        Returns:
            True, если дерево сбалансировано по высоте
        """

        def check_height(node: TreeNode | None) -> int:
            """
            Вычисляет высоту поддерева и проверяет баланс.

            Returns:
                Высота поддерева, если оно сбалансировано.
                -1, если найдено нарушение баланса.
            """
            if not node:
                return 0

            # Рекурсивно проверяем левое поддерево
            left_height = check_height(node.left)
            if left_height == -1:
                return -1  # Раннее завершение: уже нашли нарушение

            # Рекурсивно проверяем правое поддерево
            right_height = check_height(node.right)
            if right_height == -1:
                return -1  # Раннее завершение: уже нашли нарушение

            # Проверяем условие баланса для текущего узла
            if abs(left_height - right_height) > 1:
                return -1  # Сигнал: дерево не сбалансировано

            # Возвращаем высоту текущего поддерева
            return max(left_height, right_height) + 1

        return check_height(root) != -1
