class Solution:
    # time: O(n)
    # mem:  O(n)
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n
        l, r = 0, n - 1

        # Заполняем массив с конца, вставляя самые большие квадраты
        for i in range(n - 1, -1, -1):
            left_sq = nums[l] ** 2
            right_sq = nums[r] ** 2

            if left_sq > right_sq:
                res[i] = left_sq
                l += 1
            else:
                res[i] = right_sq
                r -= 1

        return res
