# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isLeaf(self, node: TreeNode):
        return node.left is None and node.right is None

    # time: O(n)
    # mem: O(n)
    # note: можно не заводить до переменную а делать
    # targetSum = targetSum - node.val и сравнивать targetSum c 0
    def hasSum(self, node: TreeNode | None, currSum: int, targetSum: int) -> bool:
        # currSum - префиксный массив
        if node is None:
            return False
        # если лист и дает нужную сумму, то мы нашли ответ
        if self.isLeaf(node) and node.val + currSum == targetSum:
            return True
        isLeftSubTreeHasSum = self.hasSum(node.left, currSum + node.val, targetSum)
        isRightSubTreeHasSum = self.hasSum(node.right, currSum + node.val, targetSum)
        return isLeftSubTreeHasSum or isRightSubTreeHasSum

    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        return self.hasSum(root, 0, targetSum)
