class Solution:
    # time:     O(n)
    # mem(доп): O(1)
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            # переходим к следующей букве пока l и r
            # не будут указывать на буквы или цифры
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue

            # оба символа - буквы или цифры
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
