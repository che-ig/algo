class Solution:
    def missingElement(self, nums: list[int], k: int) -> int:
        """
        Итеративное решение: двигаем левую и правую границы,
        считая пропуски относительно текущих границ (не от начала).
        """
        n = len(nums)

        def count_missing(left: int, right: int) -> int:
            """Количество пропущенных чисел в диапазоне [left, right]"""
            return nums[right] - nums[left] - (right - left)

        # Если k больше общего количества пропусков, ответ за пределами массива
        if k > count_missing(0, n - 1):
            return nums[-1] + (k - count_missing(0, n - 1))

        # Инициализируем границы поиска
        lo, hi = 0, n - 1

        # Сужаем диапазон до двух соседних элементов
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2

            # Сколько пропущенных чисел между lo и mid
            missing_between = count_missing(lo, mid)

            if missing_between < k:
                # В диапазоне [lo, mid] меньше k пропусков,
                # значит k-е пропущенное число находится правее mid
                # Уменьшаем k на количество пропусков в [lo, mid]
                k -= missing_between
                lo = mid
            else:
                # В диапазоне [lo, mid] >= k пропусков,
                # значит k-е пропущенное число находится между lo и mid
                # Сдвигаем правую границу, k не меняем
                hi = mid

        # Теперь lo и hi — соседние индексы
        # k-е пропущенное число находится между nums[lo] и nums[hi]
        return nums[lo] + k
