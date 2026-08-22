from functools import lru_cache


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        Рекурсивное решение с мемоизацией.
        Кэшируем результаты для каждой суммы, чтобы не вычислять повторно.
        """

        @lru_cache(maxsize=None)
        def solve(remaining: int) -> int:
            """
            Находит минимальное количество монет для суммы remaining.
            Использует мемоизацию для ускорения вычислений.

            Args:
                remaining: Оставшаяся сумма, которую нужно составить

            Returns:
                Минимальное количество монет, или -1 если невозможно
            """
            # ===== БАЗОВЫЙ СЛУЧАЙ =====
            # Если сумма равна 0, монеты не нужны
            if remaining == 0:
                return 0

            # Если сумма отрицательная — это недопустимый путь
            if remaining < 0:
                return -1

            # ===== РЕКУРСИВНЫЙ СЛУЧАЙ =====
            # Инициализируем минимальное количество как бесконечность
            min_coins = float("inf")

            # Пробуем каждую монету
            for coin in coins:
                # Рекурсивно решаем задачу для суммы (remaining - coin)
                # @lru_cache автоматически запоминает результат
                result = solve(remaining - coin)

                # Если получилось составить сумму (remaining - coin)
                if result != -1:
                    # Обновляем минимум: 1 (текущая монета) + результат
                    min_coins = min(min_coins, result + 1)

            # Возвращаем -1 если не получилось, иначе минимальное количество
            return -1 if min_coins == float("inf") else min_coins

        # Запускаем рекурсию с целевой суммой
        return solve(amount)
