class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # сортируем, чтобы дубликаты шли рядом
        n = len(nums)
        result = []

        for mask in range(1 << n):
            subset = []
            valid = True
            for i in range(n):
                if mask & (1 << i):
                    # Если это дубликат, и предыдущий такой же НЕ взят — пропускаем маску
                    if i > 0 and nums[i] == nums[i - 1] and not (mask & (1 << (i - 1))):
                        valid = False
                        break
                    subset.append(nums[i])
            if valid:
                result.append(subset)

        return result
