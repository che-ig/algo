class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        memo = {}  # кэш: индекс i -> мин. стоимость пути с i до верха

        def helper(i: int) -> int:
            # Вышли за последнюю ступеньку — мы на верху, платить нечего
            if i >= len(cost):
                return 0
            # Подзадача решена — берём из кэша
            if i in memo:
                return memo[i]
            # Платим cost[i] и идём на 1 или 2 шага вперёд —
            # выбираем более дешёвое продолжение пути
            memo[i] = cost[i] + min(helper(i + 1), helper(i + 2))
            return memo[i]

        # Старт разрешён с индекса 0 или 1 — выбираем лучший старт
        return min(helper(0), helper(1))
