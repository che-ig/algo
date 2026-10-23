from __future__ import annotations


class TreeNode:
    """Узел бинарного дерева."""

    def __init__(
        self,
        val: int = 0,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        """Рекурсивный вариант: смотрим на левого потомка каждого узла."""
        if root is None:
            return 0

        total = 0
        left = root.left

        if left is not None:
            # Лист — это узел без обоих детей. Проверяем именно левого потомка.
            if left.left is None and left.right is None:
                total += left.val
            else:
                # Не лист: внутри его поддерева тоже могут быть левые листья.
                total += self.sumOfLeftLeaves(left)

        # В правое поддерево спускаемся ОБЯЗАТЕЛЬНО:
        # у правых узлов тоже есть левые дети, которые могут быть листьями.
        total += self.sumOfLeftLeaves(root.right)

        return total


def sum_of_left_leaves_iterative(root: TreeNode | None) -> int:
    """Итеративный вариант: тот же критерий, но вместо рекурсии — явный стек."""
    total = 0
    # Стек узлов для обхода preorder. Пустое дерево сразу даёт 0.
    stack: list[TreeNode] = [root] if root is not None else []

    while stack:
        node = stack.pop()

        if node.left is not None:
            left = node.left
            if left.left is None and left.right is None:
                # Нашли левый лист — учитываем его значение.
                total += left.val
                # В сам лист идти не нужно: детей у него нет.
            else:
                # Внутренний узел — исследуем его позже.
                stack.append(left)

        # Правый потомок всегда отправляем в стек:
        # его левые листья должны быть найдены, когда мы обработаем его как родителя.
        if node.right is not None:
            stack.append(node.right)

    return total


# ==========================================
# Проверки
# ==========================================
if __name__ == "__main__":
    solution = Solution()

    # Пример 1:
    #     3
    #    / \
    #   9  20
    #      / \
    #     15  7
    tree1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert solution.sumOfLeftLeaves(tree1) == 24
    assert sum_of_left_leaves_iterative(tree1) == 24

    # Пример 2: один корень — он не является чьим-то левым ребёнком.
    assert solution.sumOfLeftLeaves(TreeNode(1)) == 0
    assert sum_of_left_leaves_iterative(TreeNode(1)) == 0

    # Пустое дерево (вне ограничений, но корректно обрабатывается).
    assert sum_of_left_leaves_iterative(None) == 0

    # Левый потомок НЕ лист, но у него есть левый лист.
    tree2 = TreeNode(1, TreeNode(2, TreeNode(4)), None)
    assert solution.sumOfLeftLeaves(tree2) == 4
    assert sum_of_left_leaves_iterative(tree2) == 4

    # Отрицательные значения: складываем как есть, не отбрасываем.
    tree3 = TreeNode(0, TreeNode(-3), TreeNode(5))
    assert solution.sumOfLeftLeaves(tree3) == -3
    assert sum_of_left_leaves_iterative(tree3) == -3

    print("Все проверки пройдены")
