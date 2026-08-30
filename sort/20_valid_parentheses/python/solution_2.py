class Solution:
    # time: O(n)
    # mem: O(n)
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"{": "}", "(": ")", "[": "]"}
        for char in s:
            if char in pairs:
                # если скобка открытая - просто добавляем в стек
                stack.append(char)
                continue

            # перед нами закрывающаяся скобка, но стек пуст
            if len(stack) == 0:
                return False
            # удаляем последний элемент из стека
            lastChar = stack.pop()
            # проверяем что последний элемент в стеке и текущий образуют пару
            # если пару не образуют, то вернем False
            if pairs[lastChar] != char:
                return False
        return len(stack) == 0
