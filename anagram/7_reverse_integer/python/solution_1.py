class Solution:
    def reverse(self, x: int) -> int:
        # Границы 32-битного знакового целого числа
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -(2**31)  # -2147483648

        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)  # Работаем с положительным числом

        while x != 0:
            # 1. Извлекаем последнюю цифру (pop)
            digit = x % 10
            x //= 10

            # 2. ПРОВЕРКА НА ПЕРЕПОЛНЕНИЕ ДО умножения и сложения
            # Так как мы работаем с положительным res, сравниваем только с INT_MAX
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > INT_MAX % 10):
                return 0

            # 3. Добавляем цифру к результату (push)
            res = res * 10 + digit

        return res * sign
