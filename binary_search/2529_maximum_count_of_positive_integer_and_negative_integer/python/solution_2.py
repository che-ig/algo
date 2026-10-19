class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        n = len(nums)

        # Вспомогательная функция, реализующая строгий Красно-Синий шаблон
        def find_first_true(good_func) -> int:
            l = -1  # ГАРАНТИРОВАННО False (Красный)
            r = n  # ГАРАНТИРОВАННО True (Синий)

            while r - l > 1:
                m = (l + r) // 2

                if good_func(m):
                    r = m  # m подошел (Синий), он кандидат на первый True
                else:
                    l = m  # m не подошел (Красный), отбрасываем его и всё слева

            # По инварианту, r ВСЕГДА указывает на первый True
            return r

        # 1. Ищем количество отрицательных чисел.
        # Нам нужен индекс первого элемента, который >= 0.
        # good_neg возвращает True, когда отрицательные числа закончились.
        def good_neg(i: int) -> bool:
            return nums[i] >= 0

        first_non_negative = find_first_true(good_neg)
        neg_count = first_non_negative  # Индекс как раз равен количеству элементов слева от него

        # 2. Ищем количество положительных чисел.
        # Нам нужен индекс первого элемента, который строго > 0.
        # good_pos возвращает True, когда начинаются положительные числа.
        def good_pos(i: int) -> bool:
            return nums[i] > 0

        first_positive = find_first_true(good_pos)
        pos_count = (
            n - first_positive
        )  # Количество элементов от first_positive до конца

        return max(neg_count, pos_count)
