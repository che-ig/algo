class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # dp[i][j] — мин. операций для превращения word1[:i] в word2[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # ── База: word1 пуст → вставляем все j символов word2 ──
        for j in range(n + 1):
            dp[0][j] = j
        # ── База: word2 пуст → удаляем все i символов word1 ──
        for i in range(m + 1):
            dp[i][0] = i

        # ── Основная часть ──
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # символы совпадают
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],  # удаление
                        dp[i][j - 1],  # вставка
                        dp[i - 1][j - 1],  # замена
                    )

        return dp[m][n]
