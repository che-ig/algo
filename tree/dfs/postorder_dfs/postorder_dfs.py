from __future__ import annotations


class TreeNode:
    """Класс, представляющий узел бинарного дерева."""

    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


def postorder_recursive(root: TreeNode | None) -> list[int]:
    """
    Рекурсивная реализация Postorder DFS.

    :param root: Корень бинарного дерева.
    :return: Список значений узлов в порядке postorder.
    """
    result: list[int] = []

    def dfs(node: TreeNode | None) -> None:
        if node is None:
            return

        # 1. Рекурсивно обходим левое поддерево
        dfs(node.left)
        # 2. Рекурсивно обходим правое поддерево
        dfs(node.right)
        # 3. Посещаем текущий узел (Корень) — в самом конце
        result.append(node.val)

    dfs(root)
    return result


def postorder_iterative(root: TreeNode | None) -> list[int]:
    """
    Итеративная реализация Postorder DFS с использованием явного стека
    и отслеживанием последнего посещённого узла.

    Идея алгоритма:
    - Идём по левым потомкам до упора, складывая узлы в стек.
    - Когда левого потомка нет, смотрим на вершину стека (peek):
        * Если у неё есть правый потомок и мы его ещё НЕ посещали —
          переключаемся на правого потомка.
        * Иначе (правого нет, либо он уже посещён) — посещаем текущий узел,
          удаляем его из стека и запоминаем как last_visited.
    - Повторяем, пока стек не пуст.

    :param root: Корень бинарного дерева.
    :return: Список значений узлов в порядке postorder.
    """
    if root is None:
        return []

    result: list[int] = []
    stack: list[TreeNode] = []
    curr: TreeNode | None = root
    last_visited: TreeNode | None = (
        None  # Последний узел, чьё значение добавлено в result
    )

    while stack or curr is not None:
        # Шаг 1: спускаемся по левым потомкам до упора
        while curr is not None:
            stack.append(curr)
            curr = curr.left

        # Шаг 2: смотрим на вершину стека, НЕ извлекая её
        peek_node = stack[-1]

        # Шаг 3: если у вершины есть правый потомок и мы его ещё не посещали —
        # переключаемся на него (начнём спуск по его левым потомкам)
        if peek_node.right is not None and last_visited != peek_node.right:
            curr = peek_node.right
        else:
            # Иначе правого потомка нет (или он уже обработан) —
            # значит, оба поддерева пройдены, можно посещать сам узел
            result.append(peek_node.val)
            stack.pop()
            last_visited = peek_node  # фиксируем, что этот узел уже посещён

    return result


def postorder_iterative_via_reverse(root: TreeNode | None) -> list[int]:
    """
    Альтернативная итеративная реализация Postorder DFS через разворот
    модифицированного Preorder.

    Идея:
    - Модифицированный preorder: Корень -> Правый -> Левый
      (в обычном preorder было Корень -> Левый -> Правый).
    - Если собрать такой обход и развернуть список, получим:
      Левый -> Правый -> Корень, что и есть postorder.

    Этот вариант короче и часто быстрее на практике,
    но вариант с last_visited считается более «классическим» и поучительным.

    :param root: Корень бинарного дерева.
    :return: Список значений узлов в порядке postorder.
    """
    if root is None:
        return []

    result: list[int] = []
    stack: list[TreeNode] = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)  # Посещаем корень ПЕРВЫМ

        # Сначала кладём ЛЕВЫЙ (он будет обработан позже),
        # потом ПРАВЫЙ (он будет извлечён раньше) —
        # получаем порядок: Корень -> Правый -> Левый
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)

    # Разворачиваем список: получаем Левый -> Правый -> Корень
    result.reverse()
    return result


# ==========================================
# Пример использования и проверки
# ==========================================
if __name__ == "__main__":
    # Создаем дерево:
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6

    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3, None, TreeNode(6))

    print("Рекурсивный обход:       ", postorder_recursive(root))
    print("Итеративный обход:       ", postorder_iterative(root))
    print("Итеративный (reverse):   ", postorder_iterative_via_reverse(root))
    # Ожидаемый вывод для всех трёх: [4, 5, 2, 6, 3, 1]
