# Для nums = [1, 2, 3] дерево решений такое:
#                         []
#                 /               \
#              взять 1           не взять 1
#              [1]                  []
#           /       \            /       \
#       взять 2   не взять 2  взять 2   не взять 2
#       [1,2]       [1]        [2]        []
#       /   \       /  \       /  \       /  \
#     +3    -3    +3   -3    +3   -3    +3   -3
#
# [1,2,3] [1,2] [1,3] [1] [2,3] [2] [3] []
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
