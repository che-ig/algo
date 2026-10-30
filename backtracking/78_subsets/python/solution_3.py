class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        Битовая генерация всех подмножеств.

        Идея: каждое подмножество — это двоичное число от 0 до 2^n - 1.
        Если i-й бит числа равен 1, включаем nums[i] в подмножество.

        Пример для [1, 2, 3]:
        000 → []
        001 → [1]
        010 → [2]
        011 → [1, 2]
        100 → [3]
        101 → [1, 3]
        110 → [2, 3]
        111 → [1, 2, 3]
        """
        n = len(nums)
        result: list[list[int]] = []

        # Перебираем все числа от 0 до 2^n - 1
        for mask in range(1 << n):  # 1 << n = 2^n
            subset: list[int] = []

            # Проверяем каждый бит
            for i in range(n):
                if mask & (1 << i):  # Если i-й бит равен 1
                    subset.append(nums[i])

            result.append(subset)

        return result
