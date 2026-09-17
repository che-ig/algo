class Solution:
    # time: O(n)
    # mem: O(1) т к размер массивов всегда 26
    def isAnagram(self, s: str, t: str) -> bool:
        # Если длины разные — точно не анаграммы
        if len(s) != len(t):
            return False

        # Массив для 26 букв английского алфавита
        count = [0] * 26

        # Считаем частоты символов в s и t одновременно
        for i in range(len(s)):
            count[ord(s[i]) - ord("a")] += 1  # добавляем для s
            count[ord(t[i]) - ord("a")] -= 1  # вычитаем для t

        # Если строки — анаграммы, все счётчики должны быть равны 0
        for c in count:
            if c != 0:
                return False

        return True
