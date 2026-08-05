from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Вспомогательная функция для бинарного поиска
        # is_first = True ищем первое вхождение, False - последнее
        def find_bound(is_first: bool) -> int:
            left, right = 0, len(nums) - 1
            result = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    # Запоминаем текущую позицию как потенциальный ответ
                    result = mid

                    if is_first:
                        # Если ищем ПЕРВОЕ вхождение, продолжаем искать левее
                        right = mid - 1
                    else:
                        # Если ищем ПОСЛЕДНЕЕ вхождение, продолжаем искать правее
                        left = mid + 1

                elif nums[mid] < target:
                    # Если текущий элемент меньше target, ищем правее
                    left = mid + 1
                else:
                    # Если текущий элемент больше target, ищем левее
                    right = mid - 1

            return result

        # Находим первую позицию
        first_pos = find_bound(is_first=True)

        # Если элемента нет в массиве, первое вхождение вернет -1.
        # В этом случае нет смысла искать последнее вхождение.
        if first_pos == -1:
            return [-1, -1]

        # Находим последнюю позицию
        last_pos = find_bound(is_first=False)

        return [first_pos, last_pos]


# --- Проверка на примерах ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.searchRange([5, 7, 7, 8, 8, 10], 8))  # Ожидается: [3, 4]
    print(sol.searchRange([5, 7, 7, 8, 8, 10], 6))  # Ожидается: [-1, -1]
    print(sol.searchRange([], 0))  # Ожидается: [-1, -1]
