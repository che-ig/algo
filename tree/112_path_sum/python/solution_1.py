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


if __name__ == "__main__":
    # Пример 1: [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
    # Путь 5 → 4 → 11 → 2 = 22 ✓
    root1 = TreeNode(5)
    root1.left = TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)))
    root1.right = TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))
    print(Solution().hasPathSum(root1, 22))  # True

    # Пример 2: [1,2,3], targetSum = 5
    # Пути: 1→2=3 и 1→3=4 — ни один не равен 5
    root2 = TreeNode(1, TreeNode(2), TreeNode(3))
    print(Solution().hasPathSum(root2, 5))  # False

    # Пример 3: пустое дерево, targetSum = 0
    print(Solution().hasPathSum(None, 0))  # False
