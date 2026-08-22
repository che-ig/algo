class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # dp[i] — минимальное количество монет для суммы i
        # Инициализируем бесконечностью (невозможно)
        dp = [float("inf")] * (amount + 1)

        # Базовый случай: для суммы 0 нужно 0 монет
        dp[0] = 0

        # Для каждой суммы от 1 до amount
        for i in range(1, amount + 1):
            # Пробуем каждую монету
            for coin in coins:
                if coin <= i:
                    # Если используем эту монету, то нужно
                    # 1 монета + минимальное количество для суммы (i - coin)
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # Если dp[amount] всё ещё бесконечность — невозможно
        return dp[amount] if dp[amount] != float("inf") else -1
