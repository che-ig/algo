class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        n = len(s)
        i = 0

        while i < n:
            # 1. Пропускаем все пробелы
            while i < n and s[i] == " ":
                i += 1

            # Если дошли до конца строки, прерываем цикл
            if i >= n:
                break

            # 2. Находим конец текущего слова
            j = i
            while j < n and s[j] != " ":
                j += 1

            # 3. Добавляем слово в список и сдвигаем указатель
            words.append(s[i:j])
            i = j

        # Разворачиваем список и склеиваем
        return " ".join(words[::-1])
