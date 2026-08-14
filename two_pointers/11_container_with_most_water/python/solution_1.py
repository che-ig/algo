class Solution:
    # time: O(n)
    # mem (дополнительная): O(1)
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        result_area = 0
        while l < r:
            curr_area = min(height[l], height[r]) * (r - l)
            result_area = max(result_area, curr_area)
            # Сдвигаем указатель, который указывает на меньшую высоту
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return result_area
