# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        """
        Находит все пути от корня до листьев с суммой, равной targetSum.
        Использует backtracking для экономии памяти.

        Args:
            root: Корень бинарного дерева
            targetSum: Целевая сумма значений в пути

        Returns:
            Список списков значений узлов для каждого подходящего пути
        """
        # Базовый случай: пустое дерево
        if not root:
            return []

        result: list[list[int]] = []
        current_path: list[int] = []

        def dfs(node: TreeNode | None, remaining_sum: int) -> None:
            """
            Рекурсивный обход с backtracking.

            Args:
                node: Текущий узел
                remaining_sum: Оставшаяся сумма, которую нужно набрать
            """
            if not node:
                return

            # Добавляем текущий узел в путь
            current_path.append(node.val)

            # Если это лист — проверяем сумму
            if not node.left and not node.right:
                if remaining_sum == node.val:
                    # Копируем путь, так как current_path будет изменяться дальше
                    result.append(current_path.copy())
            else:
                # Иначе рекурсивно идём к детям с уменьшенной суммой
                dfs(node.left, remaining_sum - node.val)
                dfs(node.right, remaining_sum - node.val)

            # BACKTRACKING: удаляем текущий узел из пути
            # Это позволяет переиспользовать один список для всех путей
            current_path.pop()

        # Начинаем обход с корня и полной целевой суммой
        dfs(root, targetSum)

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

    test_cases: list[tuple[list[int | None], int, list[list[int]], str]] = [
        (
            [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1],
            22,
            [[5, 4, 11, 2], [5, 8, 4, 5]],
            "Пример 1: два подходящих пути",
        ),
        ([1, 2, 3], 5, [], "Пример 2: нет подходящих путей"),
        ([1, 2], 0, [], "Пример 3: отрицательная сумма не достигается"),
        ([], 0, [], "Пустое дерево"),
        ([1], 1, [[1]], "Один узел с подходящей суммой"),
        ([1], 2, [], "Один узел с неподходящей суммой"),
        ([-2, None, -3], -5, [[-2, -3]], "Отрицательные значения"),
        (
            [1, -2, -3, 1, 3, -2, None, -1],
            -1,
            [[1, -2, 1, -1]],
            "Смешанные положительные и отрицательные",
        ),
    ]

    print("=" * 70)
    print("ТЕСТИРОВАНИЕ PATH SUM II")
    print("=" * 70)

    passed = 0
    for nodes, targetSum, expected, description in test_cases:
        root = build_tree(nodes)
        result = solution.pathSum(root, targetSum)

        # Сортируем для сравнения, так как порядок путей не важен
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
