class Solution:
    # time: O(n)
    # mem: O(n) - в python лучше не получится т к нужна
    # обязательно новая строка для ответа (строки не меняются)
    def minRemoveToMakeValid(self, s: str) -> str:
        # в python строки не изменяемы поэтому нужно сделать список из символов
        # который уже можно менять
        result = list(s)
        stack = []  # храним индексы для символа (
        for i in range(len(result)):
            char = result[i]
            if char == "(":
                stack.append(i)
            elif char == ")" and len(stack) == 0:
                # скобка ")" лишняя и должна быть удалена
                result[i] = ""
            elif char == ")" and len(stack) != 0:
                stack.pop()

        # проходимся по всем лишним скобкам "(" и удаляем их
        for i in stack:
            result[i] = ""

        # делаем строку из элементов списка
        return "".join(result)
