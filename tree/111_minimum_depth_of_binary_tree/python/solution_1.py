# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isLeaf(self, node: TreeNode) -> bool:
        return node.left is None and node.right is None

    # time: O(n)
    # mem: O(n) т к n - максимальная высота дерева
    def traverse(self, node: TreeNode) -> int:
        # идя в том, чтобы не заходить в вершины которые являются None
        # если мы будем туда заходить, то получим неправильный ответ для
        # 2 примера
        if self.isLeaf(node):
            return 1
        minDepthVal = float("inf")
        # если дошли до сюда, значит 1 ребенок точно есть а значит находим
        # минимальную высоту для 2 поддеревьев
        if node.left is not None:
            minDepthVal = min(minDepthVal, self.minDepth(node.left) + 1)
        if node.right is not None:
            minDepthVal = min(minDepthVal, self.minDepth(node.right) + 1)
        return minDepthVal

    def minDepth(self, node: TreeNode | None) -> int:
        if node is None:
            return 0
        return self.traverse(node)
