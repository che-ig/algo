from collections import defaultdict


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        counts = defaultdict(int)  # по умолчанию значение = 0

        for num in nums1:
            counts[num] += 1

        result = []
        for num in nums2:
            if counts[num] > 0:
                result.append(num)
                counts[num] -= 1

        return result


class Solution2:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Словарь для хранения частот элементов первого массива
        counts = {}

        # Считаем частоты вручную
        for num in nums1:
            # Проверяем, есть ли уже этот элемент в словаре
            if num in counts:
                counts[num] += 1  # если есть — увеличиваем счётчик
            else:
                counts[num] = 1  # если нет — создаём с начальным значением 1

        result = []

        # Проходим по второму массиву и собираем пересечение
        for num in nums2:
            # Проверяем, есть ли элемент в словаре и его счётчик > 0
            if num in counts and counts[num] > 0:
                result.append(num)  # добавляем в результат
                counts[num] -= 1  # уменьшаем счётчик

        return result
