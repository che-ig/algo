class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        """
        Возвращает узлы, видимые с правой стороны дерева.
        Использует DFS в порядке root → right → left.
        Первый узел на каждом уровне — правыйmost.

        Args:
            root: Корень бинарного дерева

        Returns:
            Список значений узлов, видимых справа сверху вниз
        """
        result: list[int] = []

        def dfs(node: TreeNode | None, depth: int) -> None:
            """
            Рекурсивный DFS с отслеживанием глубины.

            Args:
                node: Текущий узел
                depth: Текущая глубина (уровень)
            """
            if not node:
                return

            # Если это первый узел на данном уровне — добавляем его
            # (он будет правымmost, так как сначала идём вправо)
            if depth == len(result):
                result.append(node.val)

            # Сначала идём вправо (чтобы правые узлы встретились первыми)
            dfs(node.right, depth + 1)
            # Затем идём влево
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return result
