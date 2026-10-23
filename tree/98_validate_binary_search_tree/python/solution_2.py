from __future__ import annotations


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        """
        Проверка через inorder обход.
        В BST inorder даёт строго возрастающую последовательность.
        """
        prev: TreeNode | None = None

        def inorder(node: TreeNode | None) -> bool:
            nonlocal prev

            if node is None:
                return True

            # Сначала проверяем левое поддерево
            if not inorder(node.left):
                return False

            # Проверяем текущий узел: он должен быть строго больше предыдущего
            if prev is not None and node.val <= prev.val:
                return False
            prev = node

            # Потом проверяем правое поддерево
            return inorder(node.right)

        return inorder(root)
