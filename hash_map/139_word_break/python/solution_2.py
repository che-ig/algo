# оптимизированный вариант
class Solution_opt:
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)
        n = len(s)

        # Находим все уникальные длины слов в словаре
        # Это позволяет не перебирать все j, а только "осмысленные" длины
        word_lengths = set(len(w) for w in wordDict)

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            # Перебираем только длины, которые реально есть в словаре
            for length in word_lengths:
                # Если длина слова больше текущей позиции — пропускаем
                if length > i:
                    continue

                j = i - length  # начало потенциального слова

                # Если s[0:j] разбита И s[j:i] есть в словаре
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]


class Solution:
    def wordBreak(self, s, wordDict):
        # Преобразуем список слов в множество для O(1) проверки наличия
        word_set = set(wordDict)
        n = len(s)

        # dp[i] = True, если подстроку s[0:i] можно разбить на слова из словаря
        # dp[0] = True — пустая строка считается "разбитой" (базовый случай)
        dp = [False] * (n + 1)
        dp[0] = True

        # Для каждой позиции i в строке
        for i in range(1, n + 1):
            # Проверяем все возможные точки разреза j перед позицией i
            # Подстрока s[j:i] — это кандидат на слово из словаря
            for j in range(i):
                # Если s[0:j] уже разбита И s[j:i] есть в словаре
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # Достаточно одного способа разбить

        return dp[n]
