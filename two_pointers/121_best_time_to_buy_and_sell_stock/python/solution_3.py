class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Решение через возрастающий монотонный стек.
        stack[0] всегда содержит индекс минимального элемента.
        """
        # Возрастающий стек: значения растут от дна к вершине
        # stack[0] — индекс минимального элемента (лучшая цена покупки)
        stack = []
        max_profit = 0

        for i, price in enumerate(prices):
            # Удаляем из стека все элементы >= текущей цены.
            # Они больше не могут быть оптимальной ценой покупки,
            # потому что текущий элемент меньше и находится правее.
            while stack and prices[stack[-1]] >= price:
                stack.pop()

            # stack[0] — это индекс минимальной цены среди всех элементов слева.
            # Вычисляем прибыль, если бы мы продали сегодня.
            if stack:
                min_price_index = stack[0]  # ДНО стека, не вершина!
                profit = price - prices[min_price_index]
                max_profit = max(max_profit, profit)

            # Добавляем текущий индекс в стек
            stack.append(i)

        return max_profit
