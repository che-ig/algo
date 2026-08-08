class Solution:
    # time: O(n)
    # mem(доп): O(n)
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result = []  # тут храним массив квадратов в убывающем порядке
        p1 = 0  # указывает на начало массива
        p2 = len(nums) - 1  # указывает на конец массива
        while p1 <= p2:
            # больший элемент добавляем в конец ответа и двигаем указатель
            if abs(nums[p1]) > abs(nums[p2]):
                result.append(nums[p1] ** 2)
                p1 += 1
            else:
                result.append(nums[p2] ** 2)
                p2 -= 1
        return reversed(result)  # из убывающего делаем возрастающий
