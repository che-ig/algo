class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(t) > len(s):
            # меняем строки местами, что s была всегда больше t
            return self.isOneEditDistance(t, s)

        # не асимптотическая оптимизация
        if len(s) - len(t) > 1:
            return False

        for i in range(0, len(t)):
            if s[i] == t[i]:
                continue
            if len(s) == len(t):
                # операция replace
                return s[i + 1 :] == t[i + 1 :]
            # операция delete
            return s[i + 1 :] == t[i:]

        # заходим если первые len(t) символов совпали в строках
        # в таком случае если len(s) == len(t) нужно вернть false
        # т.к. нам обязательно нужно применить одну из операций
        return len(t) + 1 == len(s)
