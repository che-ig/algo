class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # Задаем границы поиска: от первого до последнего элемента массива
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            # Вычисляем средний индекс (защита от переполнения)
            mi = lo + (hi - lo) // 2

            if nums[mi] == target:
                # Если элемент найден, просто возвращаем его индекс
                return mi
            elif nums[mi] < target:
                # Если средний элемент меньше target, значит target находится правее.
                # Сдвигаем левую границу за mid.
                lo = mi + 1
            else:
                # Если средний элемент больше target, значит target находится левее.
                # Сдвигаем правую границу за mid.
                hi = mi - 1

        # Если мы вышли из цикла, значит элемент не найден.
        # В этот момент lo указывает на первый элемент, который больше target,
        # либо на конец массива. Это и есть идеальная позиция для вставки.
        return lo


# решение в стиле красно-синего шаблона бинарного поиска
def searchInsert_red_blue(nums: list[int], target: int) -> int:
    # Ищем первый True (первое число >= target)
    # Значит, l начинает с 0, r с len(nums)
    l = 0
    r = len(nums)

    while r - l > 1:
        m = (l + r) // 2

        if nums[m] >= target:
            r = m  # m может быть ответом, сужаем вправо
        else:
            l = m  # m точно не ответ, сужаем влево

    # После цикла l и r соседи.
    # Если nums[l] >= target, ответ l, иначе r.
    if nums[l] >= target:
        return l
    return r


# Проверка:
print(searchInsert_red_blue([1, 3, 5, 8], 11))  # Вернет 4
