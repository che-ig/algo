from collections import deque


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
        Находит LCA с помощью Эйлерова обхода и поиска минимума на отрезке.
        """
        # euler: последовательность узлов эйлерова обхода
        euler: list[TreeNode] = []

        # depth: глубина каждого узла в эйлеровом обходе
        depth: list[int] = []

        # first: индекс первого появления узла в euler
        first: dict[TreeNode, int] = {}

        def dfs(node: TreeNode | None, d: int) -> None:
            """
            Строит эйлеров обход дерева.
            """
            if not node:
                return

            # 1. Записываем узел при первом посещении
            first[node] = len(euler)
            euler.append(node)
            depth.append(d)

            # 2. Обходим левого ребёнка
            if node.left:
                dfs(node.left, d + 1)
                # Возвращаемся в текущий узел
                euler.append(node)
                depth.append(d)

            # 3. Обходим правого ребёнка
            if node.right:
                dfs(node.right, d + 1)
                # Возвращаемся в текущий узел
                euler.append(node)
                depth.append(d)

        # Запускаем обход от корня с глубиной 0
        dfs(root, 0)

        # Получаем индексы первого появления p и q
        i, j = first[p], first[q]

        # Убеждаемся, что i <= j
        if i > j:
            i, j = j, i

        # Ищем индекс минимальной глубины на отрезке [i, j]
        # (Линейный поиск. Для множества запросов здесь используют Sparse Table за O(1))
        min_idx = i
        for k in range(i + 1, j + 1):
            if depth[k] < depth[min_idx]:
                min_idx = k

        # Узел с минимальной глубиной на этом отрезке и есть LCA
        return euler[min_idx]


# ==============================================================================
# Вспомогательные функции для построения дерева и поиска узлов
# ==============================================================================


def build_tree(nodes: list[int | None]) -> TreeNode | None:
    """Построение дерева из списка в формате level-order (как на LeetCode)."""
    if not nodes or nodes[0] is None:
        return None

    root = TreeNode(nodes[0])
    queue: deque[TreeNode] = deque([root])
    i = 1

    while queue and i < len(nodes):
        node = queue.popleft()

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
    """Находит узел в дереве по его значению (для тестов)."""
    if not root:
        return None
    if root.val == val:
        return root

    left = find_node(root.left, val)
    if left:
        return left
    return find_node(root.right, val)


# ==============================================================================
# Тест-кейсы
# ==============================================================================


def run_tests() -> None:
    solution = Solution()

    # Формат: (список узлов, значение p, значение q, ожидаемый LCA, описание)
    test_cases: list[tuple[list[int | None], int, int, int, str]] = [
        # Базовые примеры
        (
            [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4],
            5,
            1,
            3,
            "Пример 1: p и q в разных поддеревьях",
        ),
        (
            [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4],
            5,
            4,
            5,
            "Пример 2: q является потомком p",
        ),
        ([1, 2], 1, 2, 1, "Пример 3: p — корень, q — потомок"),
        # Полное бинарное дерево
        (
            [1, 2, 3, 4, 5, 6, 7],
            4,
            7,
            1,
            "Полное дерево: узлы на противоположных концах",
        ),
        ([1, 2, 3, 4, 5, 6, 7], 4, 5, 2, "Полное дерево: узлы — братья (siblings)"),
        ([1, 2, 3, 4, 5, 6, 7], 2, 6, 1, "Полное дерево: узел и его племянник"),
        # Вырожденные деревья (списки)
        ([1, 2, 3, 4, 5], 4, 5, 3, "Вырожденное влево: глубокие узлы"),
        ([1, None, 2, None, 3, None, 4], 1, 4, 1, "Вырожденное вправо: корень и лист"),
        # Краевые случаи
        ([1, 2, 3, None, 4], 2, 4, 2, "Один узел является прямым родителем другого"),
        (
            [5, 3, 8, 1, 4, 7, 9],
            1,
            4,
            3,
            "Сбалансированное дерево, поиск в левом поддереве",
        ),
    ]

    print("=" * 80)
    print("ТЕСТИРОВАНИЕ LCA ЧЕРЕЗ ЭЙЛЕРОВ ОБХОД")
    print("=" * 80)

    passed = 0
    for idx, (nodes, p_val, q_val, expected, description) in enumerate(test_cases):
        root = build_tree(nodes)
        p = find_node(root, p_val)
        q = find_node(root, q_val)

        if not p or not q:
            print(f"❌ Ошибка: узел {p_val} или {q_val} не найден в дереве!")
            continue

        lca = solution.lowestCommonAncestor(root, p, q)
        result = lca.val if lca else None

        status = "✅" if result == expected else "❌"
        print(f"{status} Тест {idx + 1}: {description}")
        print(f"   Дерево: {nodes}")
        print(f"   LCA({p_val}, {q_val}) = {result} (Ожидалось: {expected})")

        # 🔥 ВИЗУАЛИЗАЦИЯ для первого теста, чтобы показать внутреннюю кухню
        if idx == 0:
            print("   📊 Внутренние массивы Эйлерова обхода:")
            # Выведем только ту часть, которая относится к запросу
            # (Для краткости выведем весь массив euler и depth)
            euler_vals = [
                node.val for node in solution.lowestCommonAncestor.__code__.co_consts
            ]  # хак, лучше пересчитать
            # Пересчитаем для чистоты вывода:
            euler_debug, depth_debug, first_debug = [], [], {}

            def debug_dfs(n, d):
                if not n:
                    return
                first_debug[n] = len(euler_debug)
                euler_debug.append(n.val)
                depth_debug.append(d)
                if n.left:
                    debug_dfs(n.left, d + 1)
                    euler_debug.append(n.val)
                    depth_debug.append(d)
                if n.right:
                    debug_dfs(n.right, d + 1)
                    euler_debug.append(n.val)
                    depth_debug.append(d)

            debug_dfs(root, 0)

            i, j = first_debug[p], first_debug[q]
            if i > j:
                i, j = j, i

            print(f"   Индексы: first[{p_val}] = {i}, first[{q_val}] = {j}")
            print(f"   Отрезок euler[{i}..{j}]: {euler_debug[i : j + 1]}")
            print(f"   Отрезок depth[{i}..{j}]: {depth_debug[i : j + 1]}")
            min_d = min(depth_debug[i : j + 1])
            print(
                f"   Минимальная глубина на отрезке: {min_d} (узел {euler_debug[i : j + 1][depth_debug[i : j + 1].index(min_d)]})"
            )
            print("-" * 80)

        if result == expected:
            passed += 1
        else:
            print(f"   ОЖИДАЛОСЬ: {expected}, ПОЛУЧЕНО: {result}")
            print("-" * 80)

    print(f"\n🏁 ИТОГ: Пройдено {passed} из {len(test_cases)} тестов.")
    print("=" * 80)


if __name__ == "__main__":
    run_tests()
