class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        """
        Вычисляет префиксную сумму массива рекурсивно.

        Args:
            nums: Исходный массив целых чисел

        Returns:
            Новый массив, где каждый элемент — сумма всех предыдущих
            элементов исходного массива включая текущий
        """
        result: list[int] = []

        def recursive_sum(index: int, current_sum: int) -> None:
            """
            Рекурсивно вычисляет префиксную сумму.

            Args:
                index: Текущий индекс в массиве
                current_sum: Накопленная сумма до текущего элемента
            """
            # Базовый случай: достигли конца массива
            if index >= len(nums):
                return

            # Добавляем текущий элемент к накопленной сумме
            current_sum += nums[index]

            # Добавляем текущую префиксную сумму в результат
            result.append(current_sum)

            # Рекурсивно обрабатываем следующий элемент
            recursive_sum(index + 1, current_sum)

        # Начинаем рекурсию с индекса 0 и начальной суммой 0
        recursive_sum(0, 0)

        return result
