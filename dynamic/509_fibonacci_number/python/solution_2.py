class Solution:
    def fib(self, n: int) -> int:
        memo = {}

        def helper(k: int) -> int:
            if k <= 1:
                return k
            if k in memo:  # уже посчитано — берём из кэша
                return memo[k]
            memo[k] = helper(k - 1) + helper(k - 2)
            return memo[k]

        return helper(n)
