class Solution:
    # делаем слияние списков:
    # arr1 = [1, 2, 8] arr2 = [3, 100]
    # result = [1, 2, 3, 8, 100]
    # time: O(n + m)
    # mem: O(n + m)
    def merge(self, arr1: list[int], arr2: list[int]) -> list[int]:
        p1, p2 = 0, 0
        result = []
        while p1 != len(arr1) or p2 != len(arr2):
            if p2 >= len(arr2) or (p1 < len(arr1) and arr1[p1] <= arr2[p2]):
                result.append(arr1[p1])
                p1 += 1
            else:
                result.append(arr2[p2])
                p2 += 1
        return result

    # Merge sort
    # time:      O(n log n)
    # mem (доп): O(n)
    # Note: по памяти можно оптимальнее сделать
    # сейчас много копирований лишних
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) == 1:
            return nums

        leftPart = self.sortArray(nums[: len(nums) // 2])
        rightPart = self.sortArray(nums[len(nums) // 2 :])
        return self.merge(leftPart, rightPart)
