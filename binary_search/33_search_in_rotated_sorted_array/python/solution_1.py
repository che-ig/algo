class Solution:
    # time: O(log n)
    # mem:  O(1)
    def findOffset(self, nums: list[int]):
        # good   bad
        # [   |  1 2 3 4 5]
        #   l    r

        #  good        bad
        # [4 5 6 7  |  0 1 2]
        #        l     r
        def good(i: int):
            return nums[i] > nums[-1]

        l, r = -1, len(nums) - 1
        while r - l > 1:
            m = (l + r) // 2
            if good(m):
                l = m
            else:
                r = m
        return r

    # time: O(log n)
    # mem:  O(1)
    def search(self, nums: list[int], target: int) -> int:
        def good(i: int):
            return nums[i] <= target

        # обычный бинарный поиск, но смещаем на offset дополнительно
        offset = self.findOffset(nums)
        l, r = 0, len(nums)
        while r - l > 1:
            # Note: ошибка №1 это делать "m = (l + r + offset) // 2"
            m = (l + r) // 2
            if good((m + offset) % len(nums)):
                l = m
            else:
                r = m
        # Note: ошибка №2 это забыть сделать "(l + offset) % len(nums)"
        realLeft = (l + offset) % len(nums)
        return realLeft if nums[realLeft] == target else -1


"""
original_index = (i - shift) % N

# Универсальная формула, которая работает во всех языках
original_index = (i - shift + N) % N
"""
