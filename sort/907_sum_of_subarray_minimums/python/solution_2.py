class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)

        # dp[i] = сумма минимумов всех подмассивов, заканчивающихся на индексе i
        dp = [0] * n

        # Монотонный стек (хранит индексы в порядке возрастания значений)
        stack = []

        total_sum = 0

        for i in range(n):
            # Удаляем элементы, которые >= arr[i]
            # (они больше не могут быть минимумом для подмассивов, заканчивающихся на i)
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            # Вычисляем dp[i]
            if not stack:
                # Нет меньшего элемента слева — arr[i] минимум для всех (i+1) подмассивов
                dp[i] = arr[i] * (i + 1)
            else:
                # j — индекс предыдущего меньшего элемента
                j = stack[-1]
                # dp[j] — сумма минимумов подмассивов, заканчивающихся на j
                # arr[i] * (i - j) — вклад arr[i] как минимума для подмассивов от j+1 до i
                dp[i] = dp[j] + arr[i] * (i - j)

            stack.append(i)
            total_sum = (total_sum + dp[i]) % MOD

        return total_sum


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
