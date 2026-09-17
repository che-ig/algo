class Solution:
    def isThree(self, n: int) -> bool:
        # Шаг 1: Проверяем, является ли n полным квадратом
        root = int(n**0.5)
        if root * root != n:
            return False

        # Шаг 2: Проверяем, является ли корень простым числом
        if root < 2:
            return False

        for i in range(2, int(root**0.5) + 1):
            if root % i == 0:
                return False

        return True


class Solution_2:
    def isThree(self, n: int) -> bool:
        count = 0
        # Ищем делители до √n
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                count += 1  # i — делитель
                # Математическая суть: делители приходят парами
                # Если число i делит n без остатка, то существует парный делитель j, такой что i * j = n.
                # Следовательно, j = n // i.
                # это условие для пропуска полного квадрата нам нужны уникальные делители.
                if i != n // i:
                    count += 1  # n//i — парный делитель

            # Ранний выход: если уже больше 3 делителей
            if count > 3:
                return False

        return count == 3
