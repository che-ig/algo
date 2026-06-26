class NumMatrix:
    # time: O(n * m)
    # mem: O(n * m)
    def __init__(self, matrix: list[list[int]]):
        # 2 матрица из 0 на 1 больше размера исходного массива
        # по горизонтали и вертикали
        n = len(matrix)
        m = len(matrix[0])

        # ps - prefix sum. написал сокращенно, чтобы было компактнее
        ps = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # other_sum - сумма всех элементов квадрата кроме текущего
                other_sum = ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1]
                ps[i][j] = matrix[i - 1][j - 1] + other_sum

        self.ps = ps

    # time: O(1)
    # mem: O(1)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # когда у вас префиксный макссив начинается с 0, и при этом
        # запросы тоже с 0 ( т е row1 - имеет минимальное значение 0, а не 1)
        # то при запросе мы все что касается row2 и col2 мы прибавляем 1
        # а row1 и col1 оставляем без изменений
        row2 += 1
        col2 += 1
        return (
            self.ps[row2][col2]
            - self.ps[row1][col2]
            - self.ps[row2][col1]
            + self.ps[row1][col1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
