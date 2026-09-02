class Solution:
    def trap(self, height: list[int]) -> int:
        # Монотонно убывающий стек: хранит индексы столбцов
        stack = []
        water = 0

        for i, h in enumerate(height):
            # Пока текущий столбец выше вершины стека —
            # мы нашли правую стенку для впадины
            while stack and h > height[stack[-1]]:
                # Выталкиваем дно впадины
                bottom = stack.pop()

                # Если стек пуст — нет левой стенки, вода утекает
                if not stack:
                    break

                # Левая стенка — новый верх стека
                left = height[stack[-1]]

                # Уровень воды определяется меньшей из двух стенок
                water_level = min(left, h)

                # Высота слоя воды над дном
                water_height = water_level - height[bottom]

                # Ширина впадины (между стенками, не включая их)
                width = i - stack[-1] - 1

                water += water_height * width

            # Кладём текущий индекс в стек
            stack.append(i)

        return water
