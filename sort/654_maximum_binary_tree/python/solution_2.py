# Определение узла дерева (как в LeetCode)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def constructMaximumBinaryTree(nums: list[int]) -> TreeNode | None:
    """
    Линейный алгоритм через монотонный убывающий стек.

    Идея:
    - Идём по nums слева направо.
    - Стек хранит узлы в порядке убывания их значений.
    - Если текущий элемент больше вершины стека, вынимаем все меньшие:
        * последний вынутый узел становится ЛЕВЫМ ребёнком текущего;
        * если стек не пуст — текущая вершина стека получает текущий узел
          как ПРАВОГО ребёнка.
    - Кладём текущий узел в стек.
    - В конце корень — это stack[0] (самый «старый» и самый большой).
    """
    stack: list[TreeNode] = []

    for num in nums:
        # Создаём новый узел для текущего числа
        node = TreeNode(num)
        last_popped = None

        # Вынимаем из стека все узлы, которые меньше текущего.
        # Они находятся слева от текущего и образуют его левое поддерево.
        while stack and stack[-1].val < num:
            last_popped = stack.pop()

        # Последний вынутый узел — максимум среди всех, что были слева
        # и меньше текущего. Он становится левым ребёнком текущего узла.
        node.left = last_popped

        # Если стек не пуст, то его вершина больше текущего узла и стоит
        # слева от него. Значит, текущий узел — первый больший справа
        # для вершины стека, и становится её правым ребёнком.
        if stack:
            stack[-1].right = node

        # Кладём текущий узел в стек — он ждёт своего «следующего большего»
        stack.append(node)

    # Корень дерева — самый нижний элемент стека (первый по порядку,
    # так как стек убывающий: снизу большие, сверху маленькие).
    return stack[0] if stack else None


# ===== Вспомогательная функция для проверки (обход в ширину) =====
def tree_to_list(root: TreeNode | None) -> list[int | None]:
    """Преобразует дерево в список (level-order), как в примерах LeetCode."""
    if not root:
        return []

    result = []
    queue: list[TreeNode | None] = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Убираем лишние None в конце
    while result and result[-1] is None:
        result.pop()

    return result


# ===== Проверка на примерах =====
if __name__ == "__main__":
    # Пример 1
    nums1 = [3, 2, 1, 6, 0, 5]
    root1 = constructMaximumBinaryTree(nums1)
    print(tree_to_list(root1))
    # Ожидаем: [6, 3, 5, None, 2, 0, None, None, 1]

    # Пример 2
    nums2 = [3, 2, 1]
    root2 = constructMaximumBinaryTree(nums2)
    print(tree_to_list(root2))
    # Ожидаем: [3, None, 2, None, 1]
