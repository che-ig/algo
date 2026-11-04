# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode | None, p: TreeNode, q: TreeNode
    ) -> TreeNode | None:
        """
        Находит наименьшего общего предка (LCA) узлов p и q.

        Ключевая идея:
        - Если нашли p или q — возвращаем этот узел
        - Если оба поддерева вернули ненулевой результат → текущий узел = LCA
        - Если только одно поддерево вернуло результат → оно и есть LCA

        Args:
            root: Корень бинарного дерева
            p: Первый узел
            q: Второй узел

        Returns:
            Наименьший общий предок узлов p и q
        """
        # Базовый случай: дошли до листа или до p/q
        # Если нашли p или q — возвращаем этот узел
        if root is None or root == p or root == q:
            return root

        # Рекурсивно ищем в левом и правом поддереве
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # Если оба поддерева нашли по узлу — текущий узел и есть LCA
        # (p в одном поддереве, q в другом)
        if left is not None and right is not None:
            return root

        # Если только одно поддерево что-то нашло — оно и есть LCA
        # (оба узла находятся в этом поддереве)
        return left if left is not None else right


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


def find_node(root: TreeNode | None, val: int) -> TreeNode | None:
    """Находит узел по значению."""
    if root is None:
        return None
    if root.val == val:
        return root

    left = find_node(root.left, val)
    if left is not None:
        return left

    return find_node(root.right, val)


def run_tests() -> None:
    solutions = [
        ("Рекурсия", Solution()),
        ("Parent pointers", Solution()),
        ("Пути от корня", Solution()),
    ]

    # Тест-кейсы: (дерево, p_val, q_val, expected_lca_val, описание)
    test_cases: list[tuple[list[int | None], int, int, int, str]] = [
        (
            [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4],
            5,
            1,
            3,
            "Пример 1: p и q в разных поддеревьях",
        ),
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5, "Пример 2: q — потомок p"),
        ([1, 2], 1, 2, 1, "Пример 3: p — корень, q — потомок"),
        (
            [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4],
            7,
            4,
            2,
            "Оба узла в левом поддереве",
        ),
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 6, 4, 5, "LCA — узел 5"),
        ([1, 2, 3], 2, 3, 1, "Минимальное дерево с LCA в корне"),
        ([1, 2], 2, 1, 1, "p — потомок, q — корень"),
    ]

    print("=" * 70)
    print("ТЕСТИРОВАНИЕ LOWEST COMMON ANCESTOR")
    print("=" * 70)

    for name, solution in solutions:
        print(f"\n📌 {name}:")
        passed = 0
        for nodes, p_val, q_val, expected, description in test_cases:
            root = build_tree(nodes)
            p = find_node(root, p_val)
            q = find_node(root, q_val)

            lca = solution.lowestCommonAncestor(root, p, q)
            result = lca.val if lca else None

            if result == expected:
                print(f"✅ {description}: LCA({p_val}, {q_val}) = {result}")
                passed += 1
            else:
                print(f"❌ {description}: LCA({p_val}, {q_val})")
                print(f"   Ожидалось: {expected}")
                print(f"   Получено:  {result}")

        print(f"\nРезультат: {passed}/{len(test_cases)} тестов пройдено")

    print("=" * 70)


if __name__ == "__main__":
    run_tests()
