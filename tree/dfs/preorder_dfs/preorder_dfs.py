from __future__ import annotations

"""
    Итеративный подход и стек (LIFO):
        В Preorder нам нужно сначала обработать Корень, затем Левый узел, и только потом Правый.
        Поскольку стек извлекает элементы в обратном порядке (LIFO), мы обязаны сначала добавить в стек node.right, а уже затем node.left. Тогда node.left окажется на вершине стека и будет извлечен следующим.
    Сложность:
        Временная сложность: O(N)
        O(N) для обоих методов, где NN
        N — количество узлов в дереве (каждый узел посещается ровно один раз).
        Пространственная сложность: O(H)
        O(H), где H
        H — высота дерева. 
            В рекурсивном методе память тратится на стек вызовов (call stack).
            В итеративном методе память тратится на явный список stack.
            В худшем случае (вырожденное дерево в linked list) H=N
            H=N, сложность O(N)
            O(N). В лучшем случае (сбалансированное дерево) H=logN
            H=logN, сложность O(logN)
            O(logN).


"""


class TreeNode:
    """Класс, представляющий узел бинарного дерева."""

    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


def preorder_recursive(root: TreeNode | None) -> list[int]:
    """
    Рекурсивная реализация Preorder DFS.

    :param root: Корень бинарного дерева.
    :return: Список значений узлов в порядке preorder.
    """
    result: list[int] = []

    # Вложенная функция для рекурсивного обхода
    def dfs(node: TreeNode | None) -> None:
        if node is None:
            return

        # 1. Посещаем текущий узел (Корень)
        result.append(node.val)
        # 2. Рекурсивно обходим левое поддерево
        dfs(node.left)
        # 3. Рекурсивно обходим правое поддерево
        dfs(node.right)

    dfs(root)
    return result


def preorder_iterative(root: TreeNode | None) -> list[int]:
    """
    Итеративная реализация Preorder DFS с использованием явного стека.

    :param root: Корень бинарного дерева.
    :return: Список значений узлов в порядке preorder.
    """
    if root is None:
        return []

    result: list[int] = []
    # Инициализируем стек корневым узлом
    stack: list[TreeNode] = [root]

    while stack:
        # Извлекаем узел из стека
        node = stack.pop()

        # 1. Посещаем текущий узел (Корень)
        result.append(node.val)

        # 2. Добавляем правый узел в стек (если он есть)
        # Важно: так как стек работает по принципу LIFO (последний зашел — первый вышел),
        # мы сначала кладем ПРАВЫЙ узел, чтобы он обработался позже.
        if node.right is not None:
            stack.append(node.right)

        # 3. Добавляем левый узел в стек (если он есть)
        # Левый узел будет извлечен из стека первым, обеспечивая правильный порядок обхода.
        if node.left is not None:
            stack.append(node.left)

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

    print("Рекурсивный обход:", preorder_recursive(root))
    # Ожидаемый вывод: [1, 2, 4, 5, 3, 6]

    print("Итеративный обход:", preorder_iterative(root))
    # Ожидаемый вывод: [1, 2, 4, 5, 3, 6]
