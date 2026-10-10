class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Решение через массив из 26 элементов.
        Так как строки содержат только lowercase English letters,
        можно использовать массив вместо словаря для экономии памяти.
        """
        # Массив для хранения частот символов в magazine.
        # Индекс 0 соответствует 'a', 1 — 'b', ..., 25 — 'z'.
        # Инициализируем нулями.
        count = [0] * 26

        # Считаем частоты символов в magazine
        for char in magazine:
            # ord(char) - ord('a') даёт индекс от 0 до 25
            # Например: ord('a') - ord('a') = 0, ord('b') - ord('a') = 1
            count[ord(char) - ord("a")] += 1

        # Проверяем, хватает ли символов для ransomNote
        for char in ransomNote:
            idx = ord(char) - ord("a")

            # Если счётчик равен 0 — символов не хватает
            if count[idx] == 0:
                return False

            # Уменьшаем счётчик
            count[idx] -= 1

        return True
