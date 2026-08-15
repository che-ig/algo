class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        # База: старт возможен с 0 или 1 индекса,
        # a = dp[0], b = dp[1] — стоим на них и уже оплатили cost[0]/cost[1]
        a, b = cost[0], cost[1]

        # Считаем dp[2..n-1]: на каждую ступень приходим
        # с более дешёвой из двух предыдущих и оплачиваем cost[i]
        for i in range(2, len(cost)):
            # справа значения СТАРЫЕ: a=dp[i-2], b=dp[i-1];
            # новое b = dp[i]; окно сдвигается вправо
            a, b = b, cost[i] + min(a, b)

        # Верх достижим одним шагом и с dp[n-1] (b), и с dp[n-2] (a) —
        # берём дешевле
        return min(a, b)
