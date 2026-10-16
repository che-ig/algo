# The guess API is already defined for you.
# @param num, your guess
# @return -1 if your guess is higher than the picked number (num > pick)
#         1 if your guess is lower than the picked number (num < pick)
#         0 if your guess is equal to the picked number (num == pick)
# def guess(num: int) -> int:

# Глобальная переменная для хранения загаданного числа
_pick = None


def guess(num: int) -> int:
    """
    API функция для сравнения предположения с загаданным числом.

    @param num: предполагаемое число
    @return: -1 если num > pick (слишком большое)
             1 если num < pick (слишком маленькое)
             0 если num == pick (угадали)
    """
    if num > _pick:
        return -1
    elif num < _pick:
        return 1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        """
        Находит загаданное число в диапазоне [1, n] с помощью бинарного поиска.
        """
        left = 1
        right = n

        while left <= right:
            # Безопасное вычисление середины (предотвращает переполнение в C++/Java)
            mid = left + (right - left) // 2

            # Вызываем API для проверки нашего предположения
            res = guess(mid)

            if res == 0:
                # Мы угадали!
                return mid
            elif res == -1:
                # Наше число (mid) БОЛЬШЕ загаданного (num > pick).
                # Значит, загаданное число находится в левой половине.
                right = mid - 1
            else:  # res == 1
                # Наше число (mid) МЕНЬШЕ загаданного (num < pick).
                # Значит, загаданное число находится в правой половине.
                left = mid + 1

        # По условию задачи число всегда существует в диапазоне,
        # поэтому эта строка теоретически недостижима.
        return -1
