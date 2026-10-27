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
        Рекурсивный подход: передаём текущий путь как строку через вызовы.

        Args:
            root: Корень бинарного дерева

        Returns:
            Список строк вида "1->2->5" для каждого пути от корня до листа
        """
        # Базовый случай: пустое дерево
        if not root:
            return []

        result: list[str] = []

        def dfs(node: TreeNode | None, path: str) -> None:
            """
            Рекурсивный обход дерева с накоплением пути.

            Args:
                node: Текущий узел
                path: Строка пути, накопленная до этого узла
            """
            if not node:
                return

            # Если это лист (нет детей) — добавляем путь в результат
            if not node.left and not node.right:
                result.append(path + str(node.val))
                return

            # Иначе рекурсивно идём к детям, добавляя текущий узел к пути
            dfs(node.left, path + str(node.val) + "->")
            dfs(node.right, path + str(node.val) + "->")

        # Начинаем обход с корня и пустого пути
        dfs(root, "")

        return result


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

    test_cases: list[tuple[list[int | None], list[str], str]] = [
        ([1, 2, 3, None, 5], ["1->2->5", "1->3"], "Пример 1: дерево с двумя листьями"),
        ([1], ["1"], "Пример 2: один узел"),
        ([1, 2], ["1->2"], "Только левый ребенок"),
        ([1, None, 2], ["1->2"], "Только правый ребенок"),
        (
            [1, 2, 3, 4, 5, 6, 7],
            ["1->3->7", "1->3->6", "1->2->5", "1->2->4"],
            "Полное дерево из 7 узлов",
        ),
        (
            [1, 2, 3, None, 5, None, 6],
            ["1->3->6", "1->2->5"],
            "Дерево с пропущенными узлами",
        ),
    ]

    print("=" * 70)
    print("ТЕСТИРОВАНИЕ BINARY TREE PATHS")
    print("=" * 70)

    passed = 0
    for nodes, expected, description in test_cases:
        root = build_tree(nodes)
        result = solution.binaryTreePaths(root)

        # Сортируем для сравнения, так как порядок не важен
        if sorted(result) == sorted(expected):
            print(f"✅ {description}")
            print(f"   Результат: {result}")
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
