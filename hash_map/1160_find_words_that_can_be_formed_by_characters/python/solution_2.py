class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        """
        Классическое решение через массив частот.
        Для каждого слова создаём копию массива частот chars
        и "расходуем" символы при проверке.
        """
        # Считаем частоты символов в chars.
        # Индекс 0 — 'a', 1 — 'b', ..., 25 — 'z'.
        chars_count = [0] * 26
        for char in chars:
            chars_count[ord(char) - ord("a")] += 1

        total_length = 0

        # Проверяем каждое слово
        for word in words:
            # Создаём КОПИЮ массива chars_count для текущего слова.
            # Это важно: каждый символ можно использовать один раз
            # в пределах одного слова, но для следующего слова
            # chars "перезаряжается".
            word_count = chars_count[:]  # или list(chars_count)

            # Проверяем, можно ли составить слово
            can_form = True
            for char in word:
                idx = ord(char) - ord("a")
                word_count[idx] -= 1

                # Если счётчик стал отрицательным — символов не хватает
                if word_count[idx] < 0:
                    can_form = False
                    break

            # Если слово можно составить — добавляем его длину
            if can_form:
                total_length += len(word)

        return total_length
