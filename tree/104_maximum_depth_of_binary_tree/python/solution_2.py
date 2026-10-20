class Solution:
    def maxDepth(self, root):
        """
        Итеративное решение через DFS со стеком.
        Храним в стеке пары (узел, глубина_этого_узла).
        """
        if not root:
            return 0

        # Стек хранит кортежи (узел, глубина)
        stack = [(root, 1)]
        max_depth = 0

        while stack:
            node, depth = stack.pop()

            # Обновляем максимум
            max_depth = max(max_depth, depth)

            # Добавляем детей в стек с увеличенной глубиной
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        return max_depth


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(nodes):
    """Построение дерева из списка (level-order)."""
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = [root]
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


def run_tests():
    solution = Solution()

    test_cases = [
        ([3, 9, 20, None, None, 15, 7], 3, "Стандартный пример 1"),
        ([1, None, 2], 2, "Стандартный пример 2 (вырожденное дерево)"),
        ([], 0, "Пустое дерево"),
        ([1], 1, "Один узел"),
        ([1, 2, 3, 4, 5], 3, "Полное дерево глубиной 3"),
        ([1, 2, None, 3, None, 4, None, 5], 5, "Линейное дерево (только левые дети)"),
        ([1, None, 2, None, 3, None, 4], 4, "Линейное дерево (только правые дети)"),
        ([1, 2, 3, 4, None, None, 5, 6], 4, "Несбалансированное дерево"),
    ]

    print("=" * 70)
    print("ТЕСТИРОВАНИЕ MAXIMUM DEPTH OF BINARY TREE")
    print("=" * 70)

    passed = 0
    for nodes, expected, description in test_cases:
        root = build_tree(nodes)
        result = solution.maxDepth(root)

        if result == expected:
            print(f"✅ {description}: глубина = {result}")
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
