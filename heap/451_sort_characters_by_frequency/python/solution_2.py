class Solution:
    def frequencySort(self, s: str) -> str:
        # Шаг 1: Считаем частоты вручную (без Counter)
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        # Шаг 2: Находим максимальную частоту
        max_freq = 0
        for count in freq.values():
            if count > max_freq:
                max_freq = count

        # Шаг 3: Создаём корзины
        # buckets[i] — список символов с частотой i
        buckets = [[] for _ in range(max_freq + 1)]

        # Раскладываем символы по корзинам согласно их частоте
        for char, count in freq.items():
            buckets[count].append(char)

        # Шаг 4: Собираем результат, идя от максимальной частоты к минимальной
        result = []
        for count in range(max_freq, 0, -1):
            for char in buckets[count]:
                # Добавляем символ count раз
                result.append(char * count)

        # Склеиваем список строк в одну строку
        return "".join(result)
