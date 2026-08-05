class Solution:
    def good(self, val: int, target: int):
        return val <= target

    # time: O(log n)
    # mem:  O(1)
    def search(self, nums: list[int], target: int) -> int:
        # ответ будет находится в элементе указывающим на l
        # поэтому сдвигаем r на 1 вправо, чтобы l мог принимать
        # значения [0, len(nums) - 1] т е от первого и до последнего
        # индекса включительно
        l, r = 0, len(nums)
        while r - l > 1:
            m = (l + r) // 2
            if self.good(nums[m], target):
                l = m
            else:
                r = m
        return l if nums[l] == target else -1
