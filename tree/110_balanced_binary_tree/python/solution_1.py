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
        - Используем self.ans для хранения ответа
        - Если нашли нарушение — устанавливаем self.ans = False
        - Функция height() всегда возвращает высоту, независимо от баланса

        Args:
            root: Корень бинарного дерева

        Returns:
            True, если дерево сбалансировано по высоте
        """
        # Инициализируем ответ как True
        # Будем устанавливать в False при обнаружении нарушения
        self.ans: bool = True

        def height(node: TreeNode | None) -> int:
            """
            Вычисляет высоту поддерева.
            Побочный эффект: устанавливает self.ans = False при нарушении баланса.

            Args:
                node: Текущий узел

            Returns:
                Высота поддерева
            """
            if not node:
                return 0

            # Раннее завершение: если уже нашли нарушение, не продолжаем
            if not self.ans:
                return 0

            # Рекурсивно вычисляем высоты детей
            left_height = height(node.left)
            right_height = height(node.right)

            # Проверяем условие баланса для текущего узла
            if abs(left_height - right_height) > 1:
                self.ans = False  # ← Устанавливаем флаг

            # Возвращаем высоту текущего поддерева
            return max(left_height, right_height) + 1

        height(root)
        return self.ans


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
        ([3, 9, 20, None, None, 15, 7], True, "Пример 1: сбалансированное"),
        ([1, 2, 2, 3, 3, None, None, 4, 4], False, "Пример 2: несбалансированное"),
        ([], True, "Пример 3: пустое дерево"),
        ([1], True, "Один узел"),
        ([1, 2], True, "Два узла"),
        ([1, 2, 3, 4, None, None, None, 5], False, "Левое поддерево глубже"),
        ([1, None, 2, None, 3, None, 4], False, "Вырожденное вправо"),
        (
            [1, 2, 2, 3, None, None, 3, 4, None, None, 4],
            False,
            "Классический несбаланс",
        ),
        ([1, 2, 3, 4, 5, 6, 7], True, "Полное дерево из 7 узлов"),
        (
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
            True,
            "Полное дерево из 15 узлов",
        ),
    ]

    print("=" * 70)
    print("ТЕСТИРОВАНИЕ BALANCED BINARY TREE")
    print("=" * 70)

    passed = 0
    for nodes, expected, description in test_cases:
        root = build_tree(nodes)
        result = solution.isBalanced(root)

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
