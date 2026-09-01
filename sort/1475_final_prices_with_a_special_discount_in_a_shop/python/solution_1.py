class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        # Копируем массив, чтобы сразу хранить итоговые цены
        answer = prices[:]
        # Стек будет хранить индексы элементов
        stack = []

        for i in range(len(prices)):
            # Пока стек не пуст и текущая цена <= цены элемента на вершине стека
            while stack and prices[stack[-1]] >= prices[i]:
                # Мы нашли скидку для элемента на вершине стека!
                idx = stack.pop()
                # Вычитаем скидку (текущую цену) из исходной цены
                answer[idx] -= prices[i]

            # Добавляем индекс текущего элемента в стек
            stack.append(i)

        return answer
