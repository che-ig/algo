from collections import Counter


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        """
        Возвращает сумму длин всех слов, которые можно составить из chars.

        Для каждого слова проверяем, является ли его Counter подмножеством
        Counter строки chars. Если да — добавляем длину слова к ответу.
        """
        # Считаем частоты символов в chars один раз.
        # Этот счётчик будет "эталонным" для проверки всех слов.
        chars_count = Counter(chars)

        total_length = 0

        # Проходим по каждому слову в массиве
        for word in words:
            # Counter(word) <= chars_count проверяет, что для каждого символа
            # в word его частота не превышает частоту в chars_count.
            # Это именно то условие, которое нужно: "можно ли составить слово".
            if Counter(word) <= chars_count:
                total_length += len(word)

        return total_length
