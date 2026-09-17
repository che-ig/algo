class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Быстрая отсечка: если длины разные — точно не анаграммы
        if len(s) != len(t):
            return False

        # Шаг 1: Строим мапу частот для строки s
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        # Шаг 2: Проходим по строке t и "расходуем" символы из мапы
        for char in t:
            # Если символа нет в мапе — t содержит лишний символ
            if char not in freq:
                return False

            # Уменьшаем счётчик
            freq[char] -= 1

            # Оптимизация: удаляем ключ, когда счётчик стал 0
            # Это нужно для быстрой финальной проверки
            if freq[char] == 0:
                del freq[char]

        # Шаг 3: Если мапа пуста — все символы "списаны" попарно
        return len(freq) == 0
