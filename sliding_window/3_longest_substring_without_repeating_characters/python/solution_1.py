class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Словарь хранит последний индекс, на котором встречался каждый символ
        last_seen = {}

        left = 0  # левая граница окна
        max_len = 0  # максимальная длина подстроки без повторов

        # right — правая граница окна, расширяем его по одному символу
        for right in range(len(s)):
            char = s[right]

            # Если символ уже встречался И находится внутри текущего окна
            # (его индекс >= left), сдвигаем левую границу за его последнее вхождение
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1

            # Обновляем последний индекс текущего символа
            last_seen[char] = right

            # Считаем длину текущего окна и обновляем максимум
            max_len = max(max_len, right - left + 1)

        return max_len
