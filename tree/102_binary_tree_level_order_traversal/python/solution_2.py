from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        """
        Выполняет обход бинарного дерева по уровням (level order traversal).
        Использует BFS с очередью для обработки узлов уровень за уровнем.

        Args:
            root: Корень бинарного дерева

        Returns:
            Список списков, где каждый подсписок содержит значения узлов
            на соответствующем уровне дерева
        """
        # Базовый случай: пустое дерево
        if not root:
            return []

        result: list[list[int]] = []

        # Очередь для BFS, начинаем с корневого узла
        queue: deque[TreeNode] = deque([root])

        # Пока в очереди есть узлы
        while queue:
            # Важно: фиксируем размер очереди ДО обработки уровня
            # Это количество узлов на текущем уровне
            level_size = len(queue)
            current_level: list[int] = []

            # Обрабатываем все узлы текущего уровня
            for _ in range(level_size):
                # Извлекаем узел из очереди
                node = queue.popleft()

                # Добавляем значение узла в текущий уровень
                current_level.append(node.val)

                # Добавляем детей в очередь для следующего уровня
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # После обработки всех узлов уровня, добавляем его в результат
            result.append(current_level)

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

    test_cases: list[tuple[list[int | None], list[list[int]], str]] = [
        (
            [3, 9, 20, None, None, 15, 7],
            [[3], [9, 20], [15, 7]],
            "Пример 1: стандартное дерево",
        ),
        ([1], [[1]], "Пример 2: один узел"),
        ([], [], "Пример 3: пустое дерево"),
        (
            [1, 2, 3, 4, 5, 6, 7],
            [[1], [2, 3], [4, 5, 6, 7]],
            "Полное дерево из 7 узлов",
        ),
        (
            [1, 2, None, 3, None, 4],
            [[1], [2], [3], [4]],
            "Вырожденное дерево (только левые дети)",
        ),
        (
            [1, None, 2, None, 3, None, 4],
            [[1], [2], [3], [4]],
            "Вырожденное дерево (только правые дети)",
        ),
        (
            [1, 2, 3, None, 4, 5, 6],
            [[1], [2, 3], [4, 5, 6]],
            "Несбалансированное дерево",
        ),
    ]

    print("=" * 70)
    print("ТЕСТИРОВАНИЕ BINARY TREE LEVEL ORDER TRAVERSAL")
    print("=" * 70)

    passed = 0
    for nodes, expected, description in test_cases:
        root = build_tree(nodes)
        result = solution.levelOrder(root)

        if result == expected:
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
