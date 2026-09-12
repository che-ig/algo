from collections import Counter, defaultdict


class Solution:
    def beautifulSubsets(self, nums: list[int], k: int) -> int:
        # Шаг 1: Группируем числа по остатку от деления на k
        # Числа из разных групп не могут конфликтовать
        groups = defaultdict(list)
        for num in nums:
            groups[num % k].append(num)

        total_beautiful = 1  # Будем перемножать результаты групп

        # Шаг 2: Решаем задачу для каждой группы независимо
        for remainder, group in groups.items():
            # Считаем частоты каждого числа в группе
            freq = Counter(group)

            # Получаем отсортированные уникальные числа группы
            unique_nums = sorted(freq.keys())
            m = len(unique_nums)

            # dp[i] — количество красивых подмножеств (включая пустое),
            # используя первые i уникальных чисел
            # dp[0] = 1 — база (пустое множество)
            dp = [0] * (m + 1)
            dp[0] = 1

            for i in range(1, m + 1):
                num = unique_nums[i - 1]
                count = freq[num]

                # Количество способов выбрать непустое подмножество из count копий
                ways_to_choose = (1 << count) - 1  # 2^count - 1

                # Проверяем конфликт с предыдущим уникальным числом
                if i >= 2 and num - unique_nums[i - 2] == k:
                    # Конфликт: не можем брать текущее и предыдущее одновременно
                    # Берем текущее → должны пропустить предыдущее → берем dp[i-2]
                    dp[i] = dp[i - 1] + dp[i - 2] * ways_to_choose
                else:
                    # Нет конфликта: можем брать независимо
                    dp[i] = dp[i - 1] * (1 << count)  # dp[i-1] * 2^count

            # Умножаем результат этой группы на общий ответ
            total_beautiful *= dp[m]

        # Вычитаем 1, чтобы исключить пустое подмножество
        return total_beautiful - 1
