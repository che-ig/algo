# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # time: O(n), n - число вершин
    # mem: O(h), где h - высота дерева. В худшем случае h = n
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p is None or q is None:
            return p is None and q is None
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    # Пример 1: p = [1,2,3], q = [1,2,3] → True
    p1 = TreeNode(1, TreeNode(2), TreeNode(3))
    q1 = TreeNode(1, TreeNode(2), TreeNode(3))
    print(Solution().isSameTree(p1, q1))  # True

    # Пример 2: p = [1,2], q = [1,null,2] → False (структура разная)
    p2 = TreeNode(1, TreeNode(2))
    q2 = TreeNode(1, None, TreeNode(2))
    print(Solution().isSameTree(p2, q2))  # False

    # Пример 3: p = [1,2,1], q = [1,1,2] → False (значения в разных местах)
    p3 = TreeNode(1, TreeNode(2), TreeNode(1))
    q3 = TreeNode(1, TreeNode(1), TreeNode(2))
    print(Solution().isSameTree(p3, q3))  # False

    # Граничный случай: оба пустые → True
    print(Solution().isSameTree(None, None))  # True

    # Один пустой, другой нет → False
    print(Solution().isSameTree(None, TreeNode(1)))  # False
