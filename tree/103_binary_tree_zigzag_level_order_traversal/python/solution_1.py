from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        """
        Выполняет зигзагообразный обход бинарного дерева.
        Чередует направление обхода на каждом уровне:
        - Уровень 0: слева направо
        - Уровень 1: справа налево
        - Уровень 2: слева направо
        - И так далее...

        Использует BFS с deque для эффективного добавления
        в начало/конец списка уровня.

        Args:
            root: Корень бинарного дерева

        Returns:
            Список списков значений узлов в зигзагообразном порядке
        """
        if not root:
            return []

        result: list[list[int]] = []
        queue: deque[TreeNode] = deque([root])

        # Флаг направления: True = слева направо, False = справа налево
        left_to_right = True

        while queue:
            level_size = len(queue)

            # Используем deque для эффективного добавления в начало/конец
            # append() — O(1) в конец, appendleft() — O(1) в начало
            current_level: deque[int] = deque()

            # Обрабатываем все узлы текущего уровня
            for _ in range(level_size):
                node = queue.popleft()

                # Добавляем значение в правильном направлении
                if left_to_right:
                    # Слева направо: добавляем в конец
                    current_level.append(node.val)
                else:
                    # Справа налево: добавляем в начало
                    current_level.appendleft(node.val)

                # Добавляем детей в очередь для следующего уровня
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Преобразуем deque в список и добавляем в результат
            result.append(list(current_level))

            # Переключаем направление для следующего уровня
            left_to_right = not left_to_right

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
            [[3], [20, 9], [15, 7]],
            "Пример 1: стандартное дерево",
        ),
        ([1], [[1]], "Пример 2: один узел"),
        ([], [], "Пример 3: пустое дерево"),
        (
            [1, 2, 3, 4, 5, 6, 7],
            [[1], [3, 2], [4, 5, 6, 7]],
            "Полное дерево из 7 узлов",
        ),
        (
            [1, 2, 3, 4, None, None, 5],
            [[1], [3, 2], [4, 5]],
            "Несбалансированное дерево",
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
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
            [[1], [3, 2], [4, 5, 6, 7], [15, 14, 13, 12, 11, 10, 9, 8]],
            "Полное дерево глубиной 4",
        ),
    ]

    print("=" * 70)
    print("ТЕСТИРОВАНИЕ BINARY TREE ZIGZAG LEVEL ORDER TRAVERSAL")
    print("=" * 70)

    passed = 0
    for nodes, expected, description in test_cases:
        root = build_tree(nodes)
        result = solution.zigzagLevelOrder(root)

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
