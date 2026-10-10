class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        """
        Классическое решение через явный словарь частот.
        """
        # Считаем частоты каждого элемента
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        # Проверяем уникальность частот
        seen_frequencies = set()

        for count in freq.values():
            # Если эта частота уже встречалась — не уникальна
            if count in seen_frequencies:
                return False
            seen_frequencies.add(count)

        # Все частоты уникальны
        return True
