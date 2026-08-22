# Решение 1: Жадный алгоритм (самое простое)
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Инициализируем общую прибыль нулём
        total_profit = 0

        # Проходим по массиву, начиная со второго дня
        for i in range(1, len(prices)):
            # Если сегодняшняя цена выше вчерашней,
            # значит есть возможность заработать
            if prices[i] > prices[i - 1]:
                # Добавляем разницу к общей прибыли
                # Это эквивалентно: купить вчера, продать сегодня
                total_profit += prices[i] - prices[i - 1]

        return total_profit
