class Solution:
    # time: O(n)
    # mem:  O(1)
    def moveZeroes(self, nums: list[int]) -> None:
        # slow — позиция, куда должен встать
        # следующий встреченный ненулевой элемент
        slow = 0

        for fast in range(len(nums)):
            # Если нашли ненулевой элемент — меняем его местами
            # с элементом на позиции slow.
            # Так ненулевые уезжают влево по порядку,
            # а нули постепенно вытесняются вправо.
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
