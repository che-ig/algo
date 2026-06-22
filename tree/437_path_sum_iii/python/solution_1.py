# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # time: O(n)
    # mem: O(n)
    def pathSumCount(
        self, node: TreeNode | None, currSum: int, allSums: dict, targetSum: int
    ) -> int:
        if node is None:
            return 0
        currSum = currSum + node.val

        # нашли число путей с окончанием в данной вершине
        countPaths = (
            allSums[currSum - targetSum] if (currSum - targetSum) in allSums else 0
        )

        if currSum not in allSums:
            # в python нет дефолтных значений поэтому нужно явно создать ключ
            # если его нет в словаре
            allSums[currSum] = 0
        allSums[currSum] += 1

        # посчитали число путей для поддеревьев
        leftSubTreePathsCount = self.pathSumCount(
            node.left, currSum, allSums, targetSum
        )
        rightSubTreePathsCount = self.pathSumCount(
            node.right, currSum, allSums, targetSum
        )

        allSums[currSum] -= 1

        return countPaths + leftSubTreePathsCount + rightSubTreePathsCount

    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        return self.pathSumCount(root, 0, {0: 1}, targetSum)
