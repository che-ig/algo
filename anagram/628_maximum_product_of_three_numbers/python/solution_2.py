class Solution:
    def maximumProduct(self, nums):
        # Инициализируем переменные
        # Три наибольших (начинаем с минимально возможных значений)
        max1 = max2 = max3 = float("-inf")

        # Два наименьших (начинаем с максимально возможных значений)
        min1 = min2 = float("inf")

        # Один проход по массиву
        for num in nums:
            # Обновляем три наибольших
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num

            # Обновляем два наименьших
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num

        # Вариант 1: три наибольших
        product1 = max1 * max2 * max3

        # Вариант 2: два наименьших + наибольшее
        product2 = min1 * min2 * max1

        return max(product1, product2)
