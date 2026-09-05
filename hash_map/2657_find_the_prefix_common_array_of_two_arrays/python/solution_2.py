class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        n = len(A)
        result = []
        seen = set()  # Множество для хранения всех встреченных элементов

        for i in range(n):
            # Добавляем текущие элементы из обоих массивов в множество
            seen.add(A[i])
            seen.add(B[i])

            # Общее количество добавленных элементов к текущей итерации = 2 * (i + 1)
            # Количество уникальных элементов = len(seen)
            # Количество общих элементов = общее количество - уникальные
            common_count = 2 * (i + 1) - len(seen)

            result.append(common_count)

        return result
