class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        Рекурсивное решение с ручной мемоизацией через словарь.
        """
        # Словарь для кэширования: сумма → минимальное количество монет
        memo = {}

        def solve(remaining: int) -> int:
            # Проверяем кэш
            if remaining in memo:
                return memo[remaining]

            # Базовый случай
            if remaining == 0:
                return 0

            if remaining < 0:
                return -1

            # Рекурсивный случай
            min_coins = float("inf")

            for coin in coins:
                result = solve(remaining - coin)

                if result != -1:
                    min_coins = min(min_coins, result + 1)

            # Сохраняем результат в кэш
            memo[remaining] = -1 if min_coins == float("inf") else min_coins

            return memo[remaining]

        return solve(amount)
