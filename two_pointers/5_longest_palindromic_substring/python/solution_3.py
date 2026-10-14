class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        best_start = 0
        best_end = 0

        for i in range(len(s)):
            # Получаем индексы для нечётного палиндрома (центр в i)
            start1, end1 = self._expand_around_center(s, i, i)

            # Получаем индексы для чётного палиндрома (центр между i и i+1)
            start2, end2 = self._expand_around_center(s, i, i + 1)

            # Выбираем более длинный палиндром из двух вариантов для текущего центра
            # Длина вычисляется просто как end - start
            if (end1 - start1) > (end2 - start2):
                curr_start, curr_end = start1, end1
            else:
                curr_start, curr_end = start2, end2

            # Если текущий палиндром длиннее лучшего найденного — обновляем рекорд
            if (curr_end - curr_start) > (best_end - best_start):
                best_start, best_end = curr_start, curr_end

        # Возвращаем срез по найденным лучшим индексам
        return s[best_start : best_end + 1]

    def _expand_around_center(self, s: str, left: int, right: int) -> tuple:
        """
        Расширяется от центра и возвращает КОРТЕЖ (start, end)
        границ найденного палиндрома.
        """
        # Пока символы совпадают, расширяем границы
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        # В этот момент left и right указывают на символы, которые НЕ совпадают
        # (или вышли за границы строки).
        # Следовательно, реальные границы палиндрома находятся на шаг внутри:
        # start = left + 1
        # end = right - 1
        return (left + 1, right - 1)


def run_tests():
    solution = Solution()

    # Проверяем именно те случаи, где математика с длиной часто ломалась
    test_cases = [
        ("babad", "bab", "Нечётный палиндром"),
        ("cbbd", "bb", "Чётный палиндром"),
        ("a", "a", "Один символ (цикл while сработает 1 раз)"),
        ("ac", "a", "Два разных символа (while не сработает, вернёт (1, 0))"),
        ("ccc", "ccc", "Несколько одинаковых"),
    ]

    print("=" * 60)
    for s, expected, desc in test_cases:
        result = solution.longestPalindrome(s)
        status = (
            "✅" if result == expected or (s == "babad" and result == "aba") else "❌"
        )
        print(f"{status} {desc}: '{s}' -> '{result}'")


run_tests()
