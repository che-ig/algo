class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        n = len(mat)
        total_sum = 0

        for i in range(n):
            total_sum += mat[i][i]  # Главная диагональ
            total_sum += mat[i][n - 1 - i]  # Побочная диагональ

        # Если размер матрицы нечётный, мы посчитали центральный элемент дважды.
        # Вычитаем его один раз, чтобы оставить в сумме ровно один раз.
        if n % 2 == 1:
            center = n // 2
            total_sum -= mat[center][center]

        return total_sum
