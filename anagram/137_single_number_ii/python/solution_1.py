class Solution:
    # time: O(n)
    # mem: O(1) - т к массив всегда фиксированного размера 64
    def singleNumber(self, nums: list[int]) -> int:
        bitsCount = [0 for _ in range(64)]
        for num in nums:
            # делаем + 2 ** 31 чтобы работать
            # с положительными числами
            num = num + 2**31
            i = 0
            while num != 0:
                bitsCount[i] += num % 2
                num //= 2
                i += 1

        result = 0
        for i in reversed(range(len(bitsCount))):
            result = result * 2 + bitsCount[i] % 3
        # делаем - 2 ** 31 чтобы получить оригинальное
        # число, которые было в начале
        return result - 2**31
