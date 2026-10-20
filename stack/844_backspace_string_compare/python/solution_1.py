class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        Сравнивает две строки после обработки backspace (#).
        Использует стек для имитации ввода в текстовый редактор.
        """

        def build_string(text):
            stack = []
            for char in text:
                if char == "#":
                    if stack:  # Удаляем предыдущий символ, если стек не пуст
                        stack.pop()
                else:
                    stack.append(char)
            return "".join(stack)

        return build_string(s) == build_string(t)
