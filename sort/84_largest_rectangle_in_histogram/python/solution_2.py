class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # Добавляем нулевой столбец в конец — это «страж»,
        # который гарантированно вытолкнет все оставшиеся столбцы из стека
        heights.append(0)

        # Стек хранит ИНДЕКСЫ столбцов.
        # Высоты столбцов в стеке всегда неубывающие (монотонный стек).
        stack = []

        max_area = 0

        for i, h in enumerate(heights):
            # Пока текущий столбец ниже, чем столбец на вершине стека,
            # выталкиваем и считаем площадь для вытолкнутого столбца
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]

                # Ширина: от нового верха стека (не включая) до текущего i (не включая)
                # Если стек пуст — столбец тянется от начала до i
                width = i if not stack else i - stack[-1] - 1

                max_area = max(max_area, height * width)

            # Кладём текущий индекс в стек
            stack.append(i)

        # Убираем добавленный нулевой столбец (чтобы не менять входные данные)
        heights.pop()

        return max_area
