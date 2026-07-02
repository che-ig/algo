class Solution:
    # time: O(n), где n - длина массива (оценка сверху, а не точная)
    # mem: O(1)
    def rotateSubArr(self, nums: list[int], i: int, j: int):
        # nums - передается по ссылке
        # nums=[1, 2, 3, 4], i=1, j=3 -> [1, 3, 2, 4]
        j -= 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return nums

    # time: O(n)
    # mem: O(1)
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # если есть массив [1, 2, 3] то сдвиг на 1 и сдвиг на 4 равны
        # и мы вместо того чтобы сдигать на 4 сдвигать хотим на 1
        k = k % len(nums)

        self.rotateSubArr(nums, 0, len(nums))
        self.rotateSubArr(nums, 0, k)
        self.rotateSubArr(nums, k, len(nums))
