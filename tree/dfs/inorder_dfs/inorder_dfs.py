from __future__ import annotations


class TreeNode:
    """Класс, представляющий узел бинарного дерева."""

    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


def inorder_recursive(root: TreeNode | None) -> list[int]:
    """
    Рекурсивная реализация Inorder DFS.

    :param root: Корень бинарного дерева.
    :return: Список значений узлов в порядке inorder.
    """
    result: list[int] = []

    # Вложенная функция для рекурсивного обхода
    def dfs(node: TreeNode | None) -> None:
        if node is None:
            return

        # 1. Рекурсивно обходим левое поддерево
        dfs(node.left)
        # 2. Посещаем текущий узел (Корень)
        result.append(node.val)
        # 3. Рекурсивно обходим правое поддерево
        dfs(node.right)

    dfs(root)
    return result


def inorder_iterative(root: TreeNode | None) -> list[int]:
    """
    Итеративная реализация Inorder DFS с использованием явного стека.

    Идея алгоритма:
    - Идём по левым потомкам до упора, складывая все узлы в стек.
    - Когда левого потомка нет, извлекаем узел из стека, посещаем его
      и переключаемся на его правого потомка.
    - Повторяем, пока есть что обрабатывать (стек не пуст или есть текущий узел).

    :param root: Корень бинарного дерева.
    :return: Список значений узлов в порядке inorder.
    """
    result: list[int] = []
    stack: list[TreeNode] = []
    curr: TreeNode | None = root

    # Продолжаем, пока есть непройденные узлы (в стеке или в виде curr)
    while stack or curr is not None:
        # Шаг 1: спускаемся по левым потомкам до самого нижнего,
        # попутно складывая все узлы в стек
        while curr is not None:
            stack.append(curr)
            curr = curr.left

        # Шаг 2: левого потомка нет — извлекаем последний узел из стека
        curr = stack.pop()
        # Посещаем его (это самый левый из ещё не посещённых узлов)
        result.append(curr.val)

        # Шаг 3: переключаемся на правого потомка.
        # Если он None — на следующей итерации снова сработает pop из стека.
        curr = curr.right

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

    print("Рекурсивный обход:", inorder_recursive(root))
    # Ожидаемый вывод: [4, 2, 5, 1, 3, 6]

    print("Итеративный обход:", inorder_iterative(root))
    # Ожидаемый вывод: [4, 2, 5, 1, 3, 6]

    # Проверка на BST: для дерева поиска inorder даёт отсортированный список
    bst = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(9)), TreeNode(8))
    print("Inorder для BST:", inorder_iterative(bst))
    # Ожидаемый вывод: [2, 3, 9, 5, 8]
