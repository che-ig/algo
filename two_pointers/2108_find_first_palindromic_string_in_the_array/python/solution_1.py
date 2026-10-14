class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        """
        Проверяет палиндромность через два указателя.
        Не создаёт развёрнутую копию строки — O(1) доп. памяти.
        """
        for word in words:
            if self._is_palindrome(word):
                return word
        return ""

    def _is_palindrome(self, s: str) -> bool:
        """
        Проверяет, является ли строка палиндромом.
        Использует два указателя, сходящихся к центру.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            # Если символы на указателях не совпадают — не палиндром
            if s[left] != s[right]:
                return False
            # Двигаем указатели к центру
            left += 1
            right -= 1

        # Все пары символов совпали — это палиндром
        return True
