class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}

        def helper(k: int) -> int:
            if k == 0:
                return 0
            if k <= 2:
                return 1
            if k in memo:
                return memo[k]
            memo[k] = helper(k - 1) + helper(k - 2) + helper(k - 3)
            return memo[k]

        return helper(n)
