# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # time: O(n)
    # mem: O(n), n - максимальная высота дерева
    def preOrder(self, node: TreeNode | None, level: int, result: list[int]):
        if node is None:
            return
        # делаем pre order и на каждом уровне
        # запоминаем последнюю вершину для уровня
        if level == len(result):
            result.append(0)
        result[level] = node.val
        self.preOrder(node.left, level + 1, result)
        self.preOrder(node.right, level + 1, result)

    def rightSideView(self, root: TreeNode | None) -> list[int]:
        result = []
        self.preOrder(root, 0, result)
        return result
