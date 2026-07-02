class Solution:
    # time: O(n)
    # mem: O(1)
    def isMonotonic(self, nums: list[int]) -> bool:
        # идея в том что нам не важно монотонно возрастает массив
        # или монотонно убыват, поэтому мы заводим 2 флага:
        # на монотонное возрастание и на монотонное убывание
        is_inc = True
        is_dec = True
        for i in range(1, len(nums)):
            is_inc = is_inc and nums[i - 1] <= nums[i]
            is_dec = is_dec and nums[i - 1] >= nums[i]
        return is_inc or is_dec
