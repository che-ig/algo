"""
Проверка stack[-1].lower() == char.lower() and stack[-1] != char очень читаема. Но в алгоритмических задачах часто любят использовать ASCII-трюк.
В таблице ASCII разница между строчной и заглавной буквой всегда равна 32 (например, 'a' = 97, 'A' = 65). Поэтому условие "плохой пары" можно записать в одну строчку через модуль разности:
"""


class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            # Разница кодов символов равна 32, если это одна буква в разных регистрах
            if stack and abs(ord(stack[-1]) - ord(char)) == 32:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
