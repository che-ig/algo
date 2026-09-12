from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        # Считаем частоты
        freq = Counter(s)

        # Находим максимальную частоту для определения размера корзин
        max_freq = max(freq.values())

        # Создаём корзины: buckets[i] = список символов с частотой i
        buckets = [[] for _ in range(max_freq + 1)]

        # Раскладываем символы по корзинам
        for char, count in freq.items():
            buckets[count].append(char)

        # Собираем результат, идя от максимальной частоты к минимальной
        result = []
        for count in range(max_freq, 0, -1):
            for char in buckets[count]:
                result.append(char * count)

        return "".join(result)
