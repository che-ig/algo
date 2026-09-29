class Solution:
    # time: O(n)
    # mem:  O(1)
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        l = 0
        r = 0
        result = 0
        while l < len(nums):
            # before
            # l
            # 1 1 1 1 0 0 1 1
            # r

            # бежим правым указателем пока в интервале [l, r]
            # находятся все последовательные числа
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                r += 1
            # after
            # l
            # 1 1 1 1 0 0 1 1
            #       r

            # обновляем ответ только если в палавающем окне были 1-цы
            # нас не просят искать нули, поэтому окна с нулями игнорируем
            if nums[r] == 1:
                result = max(result, r - l + 1)

            # интервалы не пересекаются, поэтому сдвигаем
            # на r + 1 - именно отсюда будет начинаться
            # следующий интервал
            l = r + 1
            r = r + 1
        return result
