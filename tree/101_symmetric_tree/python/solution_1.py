# Definition for a binary tree node.
class TreeNode:
    def init(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def check(self, l, r):
        if l is None or r is None:
            return l is None and r is None
        if l.val != r.val:
            return False
        return self.check(l.left, r.right) and self.check(l.right, r.left)

    def isSymmetric(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        return self.check(root.left, root.right)
