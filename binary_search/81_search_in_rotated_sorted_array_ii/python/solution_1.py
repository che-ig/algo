from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Если нашли target, сразу возвращаем True
            if nums[mid] == target:
                return True

            # Если значения слева, посередине и справа одинаковые,
            # мы не можем понять, какая часть отсортирована.
            # В этом случае просто сужаем область поиска по краям.
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1

            # Левая часть отсортирована
            elif nums[left] <= nums[mid]:
                # Если target лежит в левой отсортированной части,
                # идем влево
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # Иначе идем вправо
                else:
                    left = mid + 1

            # Правая часть отсортирована
            else:
                # Если target лежит в правой отсортированной части,
                # идем вправо
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # Иначе идем влево
                else:
                    right = mid - 1

        return False
