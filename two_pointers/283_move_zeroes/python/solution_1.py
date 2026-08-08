class Solution:
    # time: O(n)
    # mem: O(1)
    def moveZeroes(self, nums: list[int]) -> None:
        # Note: задача может формулироваться как "удалить все 0 из массива"
        # тут смысл такой же, просто делаем resize в конце или попаем (зависит от ЯП)

        freeIdx = 0  # указывает на какую позицию поставим следующий элемент не равный 0
        for num in nums:
            if num == 0:
                continue
            nums[freeIdx] = num
            freeIdx += 1

        for i in range(freeIdx, len(nums)):
            nums[i] = 0
