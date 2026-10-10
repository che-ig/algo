class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Классическое решение через словарь частот.
        Сначала считаем частоты символов в magazine,
        затем для каждого символа в ransomNote уменьшаем счётчик.
        Если счётчик становится отрицательным — символов не хватает.
        """
        # Словарь частот символов в magazine
        magazine_count = {}

        # === ПЕРВЫЙ ПРОХОД: считаем частоты символов в magazine ===
        for char in magazine:
            magazine_count[char] = magazine_count.get(char, 0) + 1

        # === ВТОРОЙ ПРОХОД: проверяем, хватает ли символов для ransomNote ===
        for char in ransomNote:
            # Если символа нет в magazine или его частота уже 0 — не хватает
            if magazine_count.get(char, 0) == 0:
                return False

            # Уменьшаем счётчик — мы "использовали" один символ
            magazine_count[char] -= 1

        # Если дошли до конца — всех символов хватило
        return True
