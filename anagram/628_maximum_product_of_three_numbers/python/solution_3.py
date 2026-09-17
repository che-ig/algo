class Solution:
    def maximumProduct(self, nums):
        # Шаг 1: Создаём массив частот для диапазона [-1000, 1000]
        # Сдвиг на +1000, чтобы индексы были неотрицательными
        offset = 1000
        counts = [0] * 2001

        # Подсчитываем частоты
        for num in nums:
            counts[num + offset] += 1

        # Шаг 2: Находим 3 наибольших и 2 наименьших числа
        # Идём справа налево для наибольших
        max1 = max2 = max3 = None
        for i in range(2000, -1, -1):
            if counts[i] > 0:
                val = i - offset
                # Добавляем число столько раз, сколько оно встречается
                # (но не более 3 раз для максимумов)
                for _ in range(counts[i]):
                    if max1 is None:
                        max1 = val
                    elif max2 is None:
                        max2 = val
                    elif max3 is None:
                        max3 = val
                        break  # Нашли 3 наибольших

        # Идём слева направо для наименьших
        min1 = min2 = None
        for i in range(2001):
            if counts[i] > 0:
                val = i - offset
                for _ in range(counts[i]):
                    if min1 is None:
                        min1 = val
                    elif min2 is None:
                        min2 = val
                        break  # Нашли 2 наименьших

        # Шаг 3: Вычисляем два варианта и возвращаем максимум
        product1 = max1 * max2 * max3
        product2 = min1 * min2 * max1

        return max(product1, product2)
