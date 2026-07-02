from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Инициализируем два максимума минимально возможными значениями
        # max1 - наибольший элемент, max2 - второй по величине
        max1 = 0
        max2 = 0

        # Проходим по массиву один раз
        for num in nums:
            if num > max1:
                # Нашли новый максимум.
                # Старый максимум становится вторым по величине
                max2 = max1
                max1 = num
            elif num > max2:
                # Число не больше max1, но больше max2.
                # Обновляем только второй максимум
                max2 = num

        # Вычисляем и возвращаем итоговое произведение
        return (max1 - 1) * (max2 - 1)


# --- Проверка на примерах ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProduct([3, 4, 5, 2]))  # Ожидается: 12  -> (5-1)*(4-1)
    print(sol.maxProduct([1, 5, 4, 5]))  # Ожидается: 16  -> (5-1)*(5-1)
    print(sol.maxProduct([3, 7]))  # Ожидается: 12  -> (7-1)*(3-1)
