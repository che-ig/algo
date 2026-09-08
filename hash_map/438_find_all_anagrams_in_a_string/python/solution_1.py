class Solution:
    def findAnagrams(self, s, p):
        n, m = len(s), len(p)

        # Если строка p длиннее s — анаграмм быть не может
        if m > n:
            return []

        # Массивы частот для 26 букв английского алфавита
        p_count = [0] * 26
        window_count = [0] * 26

        # Заполняем частоты для p
        for char in p:
            p_count[ord(char) - ord("a")] += 1

        # Инициализируем первое окно размера m
        for i in range(m):
            window_count[ord(s[i]) - ord("a")] += 1

        result = []

        # Проверяем первое окно
        if window_count == p_count:
            result.append(0)

        # Сдвигаем окно по строке s
        for i in range(m, n):
            # Добавляем новый символ справа
            window_count[ord(s[i]) - ord("a")] += 1
            # Удаляем старый символ слева
            window_count[ord(s[i - m]) - ord("a")] -= 1

            # Сравниваем частоты
            if window_count == p_count:
                result.append(i - m + 1)

        return result
