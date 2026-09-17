class Solution:
    def countPrimes(self, n: int) -> int:
        # Если n <= 2, простых чисел меньше n нет
        if n <= 2:
            return 0

        # Шаг 1: Создаём массив, где is_prime[i] = True означает,
        # что i потенциально простое число
        is_prime = [True] * n
        is_prime[0] = False  # 0 — не простое
        is_prime[1] = False  # 1 — не простое

        # Шаг 2: Решето Эратосфена
        # Достаточно идти только до sqrt(n), потому что
        # если число составное, у него есть делитель <= sqrt(n)
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:  # Если i ещё не вычеркнуто — оно простое
                # Вычёркиваем все кратные i, начиная с i*i
                # Шаг цикла = i (идём по кратным: i*i, i*i+i, i*i+2i, ...)
                for j in range(i * i, n, i):
                    is_prime[j] = False

        # Шаг 3: Считаем количество True в массиве
        return sum(is_prime)
