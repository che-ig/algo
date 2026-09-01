class Solution:
    def reverseWords(self, s: str) -> str:
        # s.split() разбивает строку на список слов, игнорируя лишние пробелы
        # [::-1] разворачивает список
        # ' '.join() склеивает слова через один пробел
        return " ".join(s.split()[::-1])
