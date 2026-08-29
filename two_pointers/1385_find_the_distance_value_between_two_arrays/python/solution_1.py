import bisect


class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        # Сортируем arr2 для бинарного поиска
        arr2.sort()

        count = 0

        # Для каждого элемента в arr1 проверяем, подходит ли он
        for x in arr1:
            # Находим позицию, куда можно вставить x, сохраняя сортировку
            # Это индекс первого элемента >= x
            pos = bisect.bisect_left(arr2, x)

            # Проверяем, что элемент подходит (все элементы arr2 на расстоянии > d)
            is_valid = True

            # Проверяем элемент СЛЕВА (наибольший элемент < x)
            if pos > 0 and abs(arr2[pos - 1] - x) <= d:
                is_valid = False

            # Проверяем элемент СПРАВА (наименьший элемент >= x)
            if pos < len(arr2) and abs(arr2[pos] - x) <= d:
                is_valid = False

            # Если оба соседа на расстоянии > d (или их нет), засчитываем элемент
            if is_valid:
                count += 1

        return count


# --- Проверка на примерах ---
if __name__ == "__main__":
    sol = Solution()

    print(sol.findTheDistanceValue([4, 5, 8], [10, 9, 1, 8], 2))  # 2
    print(sol.findTheDistanceValue([1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3))  # 2
    print(sol.findTheDistanceValue([2, 1, 100, 3], [-5, -2, 10, -3, 7], 6))  # 1
