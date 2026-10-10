class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        """
        Классическое решение через явный словарь частот.
        Два прохода: сначала считаем частоты, потом суммируем уникальные.
        """
        # Словарь для хранения частоты каждого элемента
        freq = {}

        # === ПЕРВЫЙ ПРОХОД: считаем частоты ===
        for num in nums:
            # Метод get(key, default) возвращает значение по ключу,
            # или default (0), если ключа нет в словаре.
            freq[num] = freq.get(num, 0) + 1

        # === ВТОРОЙ ПРОХОД: суммируем элементы с частотой 1 ===
        total_sum = 0
        for num, count in freq.items():
            if count == 1:
                total_sum += num

        return total_sum
