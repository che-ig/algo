from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Проверяет, можно ли составить ransomNote из символов magazine.

        Используем Counter: создаём счётчики символов для обеих строк
        и проверяем, что для каждого символа в ransomNote его частота
        не превышает частоту в magazine.
        """
        # Создаём счётчики символов для обеих строк.
        # Counter("aab") → {'a': 2, 'b': 1}
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        # Проверяем, что для каждого символа в ransomNote
        # его количество в magazine не меньше требуемого.
        # Оператор <= для Counter проверяет именно это:
        # ransom_count <= magazine_count возвращает True,
        # если для всех ключей ransom_count[key] <= magazine_count[key].
        return ransom_count <= magazine_count
