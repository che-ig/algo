class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Вспомогательная функция: проверяет, является ли подстрока
        # s[left:right+1] палиндромом
        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        # Два указателя с концов строки
        left = 0
        right = len(s) - 1

        while left < right:
            # Если символы совпадают, двигаемся дальше к центру
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # Нашли первое несовпадение.
                # У нас есть право удалить ОДИН символ.
                # Пробуем два варианта:

                # Вариант 1: пропускаем левый символ
                option1 = is_palindrome(left + 1, right)

                # Вариант 2: пропускаем правый символ
                option2 = is_palindrome(left, right - 1)

                # Если хоть один вариант работает — строку можно сделать палиндромом
                return option1 or option2

        # Если дошли до центра без несовпадений — это уже палиндром
        # (0 удалений тоже <= 1, подходит)
        return True


# --- Проверка на примерах ---
if __name__ == "__main__":
    sol = Solution()

    print(sol.validPalindrome("aba"))  # True (уже палиндром)
    print(sol.validPalindrome("abca"))  # True (удаляем 'c' → "aba")
    print(sol.validPalindrome("abc"))  # False
    print(sol.validPalindrome("deeee"))  # True (удаляем 'd' → "eeee")
