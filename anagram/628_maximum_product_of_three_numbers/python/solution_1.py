class Solution:
    def maximumProduct(self, nums):
        # Сортируем массив
        nums.sort()
        n = len(nums)

        # Вариант 1: три наибольших числа (в конце отсортированного массива)
        product1 = nums[n - 1] * nums[n - 2] * nums[n - 3]

        # Вариант 2: два наименьших (возможно отрицательных) + наибольшее
        product2 = nums[0] * nums[1] * nums[n - 1]

        # Возвращаем максимум из двух вариантов
        return max(product1, product2)
