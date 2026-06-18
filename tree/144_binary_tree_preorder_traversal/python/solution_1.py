# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # time: O(n)
    # mem: O(h), где h - высота дерева, в худшем случае h = n, поэтому
    #      можно сказать что mem: O(n)
    def traverse(self, node: TreeNode | None, result: list[int]):
        if node is None:
            return
        # Pre order - значит перед тем как рекурсивно идти в левое и
        # правное поддерево добавляем значение узла в ответ
        result.append(node.val)
        self.traverse(node.left, result)
        self.traverse(node.right, result)

    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []
        self.traverse(root, result)
        return result
