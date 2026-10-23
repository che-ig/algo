from __future__ import annotations


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        """
        Рекурсивное инвертирование дерева.
        Для каждого узла меняем местами левого и правого потомка.
        """
        # Базовый случай: пустой узел
        if root is None:
            return None

        # Меняем местами левого и правого потомка
        root.left, root.right = root.right, root.left

        # Рекурсивно инвертируем поддеревья
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


def tree_to_list(root: TreeNode | None) -> list[int | None]:
    """Вспомогательная функция для сериализации дерева в список (level-order)."""
    if root is None:
        return []

    result: list[int | None] = []
    queue: deque[TreeNode | None] = deque([root])

    while queue:
        node = queue.popleft()
        if node is None:
            result.append(None)
        else:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

    # Убираем trailing None
    while result and result[-1] is None:
        result.pop()

    return result


if __name__ == "__main__":
    # Пример 1: root = [4,2,7,1,3,6,9] → [4,7,2,9,6,3,1]
    root1 = TreeNode(
        4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9))
    )
    Solution().invertTree(root1)
    print(tree_to_list(root1))  # [4, 7, 2, 9, 6, 3, 1]

    # Пример 2: root = [2,1,3] → [2,3,1]
    root2 = TreeNode(2, TreeNode(1), TreeNode(3))
    Solution().invertTree(root2)
    print(tree_to_list(root2))  # [2, 3, 1]

    # Пример 3: root = [] → []
    print(tree_to_list(Solution().invertTree(None)))  # []
