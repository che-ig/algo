class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        """
        Вычисляет префиксную сумму in-place, модифицируя входной массив.

        Args:
            nums: Исходный массив (будет модифицирован)

        Returns:
            Модифицированный массив с префиксными суммами
        """
        # Начинаем со второго элемента
        for i in range(1, len(nums)):
            # Текущий элемент = предыдущая префиксная сумма + текущий элемент
            nums[i] = nums[i - 1] + nums[i]

        return nums
