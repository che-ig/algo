# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# данная задача основывается на задаче 104
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        """
        Альтернативная реализация: высота пустого дерева = 0.
        Тогда путь через узел = left_height + right_height.
        """
        diameter: int = 0

        def height(node: TreeNode | None) -> int:
            nonlocal diameter

            if not node:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            # Путь через текущий узел = сумма высот поддеревьев
            path_through_node = left_height + right_height
            diameter = max(diameter, path_through_node)

            # Высота текущего поддерева = максимум из высот детей + 1
            return max(left_height, right_height) + 1

        height(root)
        return diameter


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

    test_cases: list[tuple[list[int | None], int, str]] = [
        ([1, 2, 3, 4, 5], 3, "Пример 1: путь через корень"),
        ([1, 2], 1, "Пример 2: только два узла"),
        ([1], 0, "Один узел (диаметр = 0)"),
        ([1, 2, 3], 2, "Полное дерево из 3 узлов"),
        ([1, 2, 3, 4, 5, 6, 7], 4, "Полное дерево из 7 узлов"),
        ([1, 2, None, 3, None, 4, None, 5], 4, "Вырожденное влево дерево"),
        ([1, None, 2, None, 3, None, 4], 3, "Вырожденное вправо дерево"),
        ([1, 2, 3, None, None, 4, 5, 6, 7], 5, "Диаметр не через корень"),
    ]

    print("=" * 70)
    print("ТЕСТИРОВАНИЕ DIAMETER OF BINARY TREE")
    print("=" * 70)

    passed = 0
    for nodes, expected, description in test_cases:
        root = build_tree(nodes)
        result = solution.diameterOfBinaryTree(root)

        if result == expected:
            print(f"✅ {description}: диаметр = {result}")
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
