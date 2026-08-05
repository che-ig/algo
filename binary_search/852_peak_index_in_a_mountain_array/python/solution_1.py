class Solution:
    def good(self, i, arr):
        if i == 0:
            return True
        return arr[i - 1] < arr[i]

    # time: O(log n)
    # mem:  O(1)
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        # arr - гарантированно mountain, поэтому ответ
        # будет лежать в диапазоне [0, len(arr) - 2] включительно
        # а значит r = len(arr) - 1 (на 1 больше чтобы l мог встать
        # в крайнюю позицию)
        l, r = 0, len(arr) - 1
        while r - l > 1:
            m = (l + r) // 2
            if self.good(m, arr):
                l = m
            else:
                r = m
        return l
