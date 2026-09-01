class Solution:
    # time: O(n)
    # mem: O(n)
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        # в стеке всегда храним убывающую последовательность
        # например: [[1, 20], [3, 8], [5, 1]]
        # [1, 20] -> в 1 день температура была 20
        stack = []
        for i, temperature in enumerate(temperatures):
            # пока текущая температура больше чем температура в стеке
            # вынимаем удаляем из стека элементы и
            # вычисляем для них ответ
            while len(stack) > 0 and stack[-1][1] < temperature:
                idx, _ = stack.pop()
                result[idx] = i - idx
            stack.append([i, temperature])
        return result
