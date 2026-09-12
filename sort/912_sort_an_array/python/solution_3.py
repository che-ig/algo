class Solution:
    # time: O(n)
    # mem: O(n)
    def sortArray(self, nums: list[int]) -> list[int]:
        # считаем сколько каких чисел в массиве
        # ключ - число, значение - сколько встретилось

        # 5 * 10 ** 4 - т к минимальный элемент это
        # -5 * 10 ** 4 (по условию), то сдвиг будет
        # +5 * 10 ** 4, чтобы count[0] - показывал
        # сколько элементов в массиве равных -5 * 10 ** 4
        offset = 5 * 10**4
        count = [0 for _ in range(5 * 10**4 * 2 + 1)]
        for num in nums:
            count[num + offset] += 1

        # я создаю новый а вы при желании можете изменить массив nums
        sorted_nums = []
        for num in range(len(count)):
            for _ in range(count[num]):
                sorted_nums.append(num - offset)
        return sorted_nums
