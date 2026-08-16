class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # i = 0: пустой word1 превращается в word2[:j] за j вставок
        row = list(range(n + 1))

        for i in range(1, m + 1):
            prev_diag = row[0]  # dp[i-1][0] — будущая «диагональ» для j=1
            row[0] = i  # dp[i][0]: word2 пуст → i удалений
            for j in range(1, n + 1):
                temp = row[j]  # запоминаем dp[i-1][j] до перезаписи
                if word1[i - 1] == word2[j - 1]:
                    row[j] = prev_diag  # совпали: бесплатно
                else:
                    # row[j]   = dp[i-1][j]   удаление (старое, сверху)
                    # row[j-1] = dp[i][j-1]   вставка  (новое, слева)
                    # prev_diag= dp[i-1][j-1] замена   (спасённая диагональ)
                    row[j] = 1 + min(row[j], row[j - 1], prev_diag)
                prev_diag = temp  # старое dp[i-1][j] станет диагональю для j+1
            # конец строки
        return row[n]
