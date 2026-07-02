class Solution:
    def maxPower(self, s: str) -> int:
        # Так как по ограничениям длина строки минимум 1,
        # начальное значение максимума и текущего счетчика равно 1.
        max_power = 1
        current_power = 1

        # Начинаем обход строки со второго символа (индекс 1)
        for i in range(1, len(s)):
            # Если текущий символ совпадает с предыдущим
            if s[i] == s[i - 1]:
                current_power += 1
                # Обновляем глобальный максимум, если текущая последовательность длиннее
                if current_power > max_power:
                    max_power = current_power
            else:
                # Если символ отличается, начинаем новую последовательность
                current_power = 1

        return max_power


# --- Проверка на примерах ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxPower("leetcode"))  # Ожидается: 2 ("ee")
    print(sol.maxPower("abbcccddddeeeeedcba"))  # Ожидается: 5 ("eeeee")
