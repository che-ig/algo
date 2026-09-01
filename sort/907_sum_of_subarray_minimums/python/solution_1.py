class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)

        # left[i] = количество элементов слева от i (включая i),
        # пока не встретим элемент строго меньше arr[i]
        left = [0] * n

        # right[i] = количество элементов справа от i (включая i),
        # пока не встретим элемент меньше или равен arr[i]
        right = [0] * n

        # Вычисляем left с помощью монотонного стека
        stack = []
        for i in range(n):
            # Удаляем элементы, которые >= arr[i]
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            # Если стек пуст — меньшего элемента слева нет
            if not stack:
                left[i] = i + 1
            else:
                # Иначе расстояние до предыдущего меньшего элемента
                left[i] = i - stack[-1]

            stack.append(i)

        # Вычисляем right с помощью монотонного стека (идем справа налево)
        stack = []
        for i in range(n - 1, -1, -1):
            # Удаляем элементы, которые > arr[i] (строго больше!)
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            # Если стек пуст — меньшего или равного элемента справа нет
            if not stack:
                right[i] = n - i
            else:
                # Иначе расстояние до следующего меньшего или равного элемента
                right[i] = stack[-1] - i

            stack.append(i)

        # Считаем общую сумму
        result = 0
        for i in range(n):
            result = (result + arr[i] * left[i] * right[i]) % MOD

        return result


# ==========================================
# Тесты
# ==========================================
if __name__ == "__main__":
    solution = Solution()

    # Пример 1
    arr1 = [3, 1, 2, 4]
    print(f"Input: {arr1}")
    print(f"Output: {solution.sumSubarrayMins(arr1)}")
    print(f"Ожидание: 17\n")

    # Пример 2
    arr2 = [11, 81, 94, 43, 3]
    print(f"Input: {arr2}")
    print(f"Output: {solution.sumSubarrayMins(arr2)}")
    print(f"Ожидание: 444\n")

    # Пример с дубликатами
    arr3 = [2, 2, 2]
    print(f"Input: {arr3}")
    print(f"Output: {solution.sumSubarrayMins(arr3)}")
    print(f"Ожидание: 12\n")

    # Детальный разбор для arr1
    print("=" * 50)
    print("Детальный разбор для [3, 1, 2, 4]:")
    print("=" * 50)

    arr_detail = [3, 1, 2, 4]
    n = len(arr_detail)
    left = [0] * n
    right = [0] * n

    stack = []
    for i in range(n):
        while stack and arr_detail[stack[-1]] >= arr_detail[i]:
            stack.pop()
        left[i] = i + 1 if not stack else i - stack[-1]
        stack.append(i)

    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr_detail[stack[-1]] > arr_detail[i]:
            stack.pop()
        right[i] = n - i if not stack else stack[-1] - i
        stack.append(i)

    print(f"Элемент: {arr_detail}")
    print(f"Left:    {left}")
    print(f"Right:   {right}")
    print(f"Вклад:   {[arr_detail[i] * left[i] * right[i] for i in range(n)]}")
    print(f"Сумма:   {sum(arr_detail[i] * left[i] * right[i] for i in range(n))}")
