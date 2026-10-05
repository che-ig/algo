class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        """
        Проверяет возможность посадки n цветов без мутирования flowerbed.
        Использует переменную last_planted для отслеживания последней посадки.
        """
        if n == 0:
            return True

        # last_planted — индекс грядки, на которую мы последний раз посадили цветок.
        # Инициализируем -2 (любое число < -1), чтобы условие i - 1 != last_planted
        # было True для i == 0 (т.е. для первой грядки нет "предыдущей посадки").
        last_planted = -2

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                # Левый сосед пуст И не является только что посаженной грядкой.
                # Условие (i - 1 != last_planted) важно: без него алгоритм мог бы
                # посадить цветок на i, даже если i-1 была посажена на предыдущем шаге.
                left_empty = (i == 0) or (
                    flowerbed[i - 1] == 0 and i - 1 != last_planted
                )

                # Правый сосед пуст (проверка стандартная, так как мы ещё не сажали на i+1)
                right_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                if left_empty and right_empty:
                    # Запоминаем, что посадили на позицию i
                    last_planted = i
                    n -= 1

                    if n == 0:
                        return True

        return n == 0
