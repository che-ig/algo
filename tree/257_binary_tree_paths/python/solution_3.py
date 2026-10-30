# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        """
        Находит все пути от корня до листьев через backtracking.

        Идея:
        - Используем ОДИН изменяемый список current_path для всех путей
        - При спуске вниз: добавляем узел в путь
        - При подъёме вверх: удаляем узел из пути (backtrack)
        - Когда достигаем листа: собираем строку из списка

        Args:
            root: Корень бинарного дерева

        Returns:
            Список строк вида "1->2->5" для каждого пути от корня до листа
        """
        if not root:
            return []

        result: list[str] = []
        current_path: list[str] = []

        def backtrack(node: TreeNode | None) -> None:
            """
            Backtracking-функция: исследует все пути от текущего узла.
            """
            if not node:
                return

            # 1. ДЕЛАЕМ ВЫБОР: добавляем текущий узел в путь
            current_path.append(str(node.val))

            # 2. ПРОВЕРЯЕМ: если это лист — собираем строку и добавляем в результат
            if not node.left and not node.right:
                # Собираем строку из текущего пути: "1->2->5"
                path_str = "->".join(current_path)
                result.append(path_str)
            else:
                # 3. ИССЛЕДУЕМ: рекурсивно идём к детям
                backtrack(node.left)
                backtrack(node.right)

            # 4. ОТКАТЫВАЕМ ВЫБОР: удаляем текущий узел из пути
            # Это позволяет переиспользовать один список для всех путей
            current_path.pop()

        backtrack(root)
        return result
