class Solution:
    # time: O(n)
    # mem (дополнительная): O(1)
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        p1 = 0
        p2 = len(numbers) - 1
        while p1 < p2:
            curr_sum = numbers[p1] + numbers[p2]
            if curr_sum == target:
                return [p1 + 1, p2 + 1]
            elif curr_sum < target:
                # если текущая сумма меньше target то увеличиваем ее за счет сдвига p1
                p1 += 1
            else:
                # если текущая сумма больше target то уменьшаем ее за счет сдвига p2
                p2 -= 1
        return [-1, -1]
