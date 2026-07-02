class Solution:
    # time: O(n)
    # mem (дополнительная): O(1)
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        prev = float("-inf")
        max_length = 0  # максимальная длина возрастающей последовательности
        curr_length = 0  # текущая длина возрастающей последовательности
        for num in nums:
            # т к последовательности по условию не прерывающаяся
            # то мы на кажой итерации или увеличиваем ответ - если
            # приходит число больше чем предыдущее или делаем ответ 1
            # т к непрерывная возрастающая последовательности кончилась
            # и мы начинаем новую возрастающую последовательности
            if prev < num:
                curr_length += 1
            else:
                curr_length = 1
            max_length = max(
                max_length, curr_length
            )  # на каждой итерации обновляем ответ
            prev = num
        return max_length
