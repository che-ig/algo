class Solution:
    def missingElement(self, nums: list[int], k: int) -> int:
        """
        Рекурсивное решение: делим массив пополам и определяем,
        в какой половине находится k-е пропущенное число.
        """

        def count_missing(left: int, right: int) -> int:
            """
            Считает количество пропущенных чисел в диапазоне [left, right].
            Формула: (ожидаемое количество) - (фактическое количество)
            """
            return nums[right] - nums[left] - (right - left)

        def solve(left: int, right: int, k: int) -> int:
            """
            Рекурсивно находит k-е пропущенное число в диапазоне [left, right].

            Args:
                left: левая граница диапазона
                right: правая граница диапазона
                k: какое пропущенное число ищем (относительно left)
            """
            # Базовый случай: если между left и right нет промежуточных элементов
            # Когда left + 1 == right, это значит, что мы сузили диапазон до двух
            # соседних элементов массива.
            # Между ними нет других элементов из массива — только пропущенные числа.
            if left + 1 == right:
                # Просто добавляем k к nums[left]
                # Когда мы дошли до соседних элементов, мы уже знаем, что k-е пропущенное число находится между ними. Поскольку между nums[left] и nums[right] нет других элементов массива, все числа в этом промежутке — пропущенные.
                return nums[left] + k

            mid = left + (right - left) // 2

            # Сколько пропущенных чисел в ЛЕВОЙ половине [left, mid]
            missing_left = count_missing(left, mid)

            if missing_left >= k:
                # k-е пропущенное число находится в левой половине
                # Ищем его там же, с тем же k
                return solve(left, mid, k)
            else:
                # k-е пропущенное число находится в правой половине
                # Но теперь нам нужно найти (k - missing_left)-е число
                # (потому что missing_left чисел уже "использованы" в левой половине)
                return solve(mid, right, k - missing_left)

        # Проверяем, находится ли ответ за пределами массива
        total_missing = count_missing(0, len(nums) - 1)
        if k > total_missing:
            return nums[-1] + (k - total_missing)

        return solve(0, len(nums) - 1, k)
