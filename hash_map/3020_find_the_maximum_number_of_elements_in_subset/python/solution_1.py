class Solution:
    def maxFrequencyLength(self, nums: list[int]) -> int:
        # Подсчитываем частоты всех чисел вручную (без Counter)
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        max_len = 0

        # Особый случай: x = 1
        # Все степени 1 равны 1, поэтому паттерн из единиц может быть любой нечётной длины
        if 1 in freq:
            count_1 = freq[1]
            # Если количество нечётное — берём все
            # Если чётное — убираем одну, чтобы длина стала нечётной
            if count_1 % 2 == 1:
                max_len = count_1
            else:
                max_len = count_1 - 1

        # Для каждого числа x > 1 пытаемся построить цепочку степеней
        for x in freq:
            if x == 1:
                continue

            current = x
            length = 0

            # Строим цепочку: x → x² → x⁴ → x⁸ → ...
            while True:
                count = freq.get(current, 0)

                if count == 0:
                    # Текущее число не найдено — предыдущее было центром
                    break
                elif count == 1:
                    # Нашли центр (нужна 1 копия)
                    length += 1
                    break
                else:
                    # count >= 2 — берём 2 копии для симметрии и идём дальше
                    length += 2
                    current = current * current

                    # Защита от переполнения: если current > 10^9,
                    # его точно нет в массиве (ограничение задачи)
                    if current > 10**9:
                        break

            max_len = max(max_len, length)

        return max_len
