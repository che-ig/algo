from collections import defaultdict
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        # Шаг 1: Вычисляем префиксные суммы для каждой строки
        # prefix[i][j] = сумма элементов matrix[i][0..j-1]
        prefix = [[0] * (cols + 1) for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                prefix[i][j + 1] = prefix[i][j] + matrix[i][j]

        count = 0

        # Шаг 2: Перебираем все возможные пары левой и правой колонок
        for c1 in range(cols):
            for c2 in range(c1, cols):
                # Теперь для фиксированных c1 и c2 задача сводится к 1D:
                # Найти количество подмассивов строк с суммой = target

                # Используем хеш-таблицу для подсчета префиксных сумм
                # Это классический алгоритм "Subarray Sum Equals K"
                current_sum = 0
                freq = defaultdict(int)
                freq[0] = 1  # Пустой префикс имеет сумму 0

                # Проходим по всем строкам
                for i in range(rows):
                    # Сумма элементов в строке i от колонки c1 до c2
                    row_sum = prefix[i][c2 + 1] - prefix[i][c1]
                    current_sum += row_sum

                    # Ищем, сколько раз встречалась сумма (current_sum - target)
                    # Если она была, значит есть подмассив с суммой = target
                    count += freq[current_sum - target]

                    # Добавляем текущую префиксную сумму в хеш-таблицу
                    freq[current_sum] += 1

        return count


# Если rows > cols, можно транспонировать матрицу и поменять роли строк и колонок, чтобы минимизировать количество итераций внешнего цикла:
# Это гарантирует, что временная сложность будет O(min⁡(rows,cols)2⋅max⁡(rows,cols))O(\min(rows, cols)^2 \cdot \max(rows, cols))O(min(rows,cols)2⋅max(rows,cols)), что оптимально для любых размеров матрицы.
class SolutionOptimize:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # Транспонируем, если строк больше, чем колонок
        if len(matrix) > len(matrix[0]):
            matrix = [list(row) for row in zip(*matrix)]

        rows = len(matrix)
        cols = len(matrix[0])

        prefix = [[0] * (cols + 1) for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                prefix[i][j + 1] = prefix[i][j] + matrix[i][j]

        count = 0
        for c1 in range(cols):
            for c2 in range(c1, cols):
                current_sum = 0
                freq = defaultdict(int)
                freq[0] = 1

                for i in range(rows):
                    row_sum = prefix[i][c2 + 1] - prefix[i][c1]
                    current_sum += row_sum
                    count += freq[current_sum - target]
                    freq[current_sum] += 1

        return count


# --- Проверка на примерах ---
if __name__ == "__main__":
    sol = Solution()

    matrix1 = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
    print(sol.numSubmatrixSumTarget(matrix1, 0))  # Ожидается: 4

    matrix2 = [[1, -1], [-1, 1]]
    print(sol.numSubmatrixSumTarget(matrix2, 0))  # Ожидается: 5

    matrix3 = [[904]]
    print(sol.numSubmatrixSumTarget(matrix3, 0))  # Ожидается: 0
