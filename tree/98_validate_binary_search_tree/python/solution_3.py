# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        """
        Итеративная проверка BST через inorder traversal.
        В валидном BST inorder traversal дает строго возрастающую последовательность.
        """
        stack: list[TreeNode] = []
        curr: TreeNode | None = root
        prev: float = -float("inf")

        while stack or curr:
            # Спускаемся максимально влево
            while curr:
                stack.append(curr)
                curr = curr.left

            # Обрабатываем узел
            curr = stack.pop()

            # Проверяем возрастание
            if curr.val <= prev:
                return False

            prev = curr.val

            # Идем в правое поддерево
            curr = curr.right

        return True


def build_tree(nodes: list[int | None]) -> TreeNode | None:
    """Построение дерева из списка (level-order)."""
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue: list[TreeNode] = [root]
    i = 1

    while queue and i < len(nodes):
        node = queue.pop(0)

        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1

        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1

    return root


def run_tests() -> None:
    solution = Solution()

    test_cases: list[tuple[list[int | None], bool, str]] = [
        ([2, 1, 3], True, "Пример 1: валидный BST"),
        ([5, 1, 4, None, None, 3, 6], False, "Пример 2: правый ребенок 4 < 5"),
        ([], True, "Пустое дерево (edge case)"),
        ([1], True, "Один узел"),
        ([5, 4, 6, None, None, 3, 7], False, "3 в правом поддереве < 5"),
        ([2, 2, 2], False, "Все узлы одинаковые (не строго)"),
        ([1, 1], False, "Левый ребенок равен родителю"),
        ([10, 5, 15, None, None, 6, 20], False, "6 в правом поддереве < 10"),
        ([3, 1, 5, 0, 2, 4, 6], True, "Полный валидный BST"),
        ([5, 3, 7, 1, 4, 6, 8], True, "Еще один валидный BST"),
    ]

    print("=" * 70)
    print("ТЕСТИРОВАНИЕ VALIDATE BINARY SEARCH TREE")
    print("=" * 70)

    passed = 0
    for nodes, expected, description in test_cases:
        root = build_tree(nodes)
        result = solution.isValidBST(root)

        if result == expected:
            print(f"✅ {description}: {result}")
            passed += 1
        else:
            print(f"❌ {description}")
            print(f"   Ожидалось: {expected}")
            print(f"   Получено:  {result}")

    print("=" * 70)
    print(f"Результат: {passed}/{len(test_cases)} тестов пройдено")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()
