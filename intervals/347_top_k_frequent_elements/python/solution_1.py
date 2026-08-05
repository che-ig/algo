class Solution:
    # time: O(n)
    # mem: O(n)
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # ключ - число, значение - сколько раз встретилось
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        # индекс массива - сколько раз встретилось число
        # значение - список чисел, которые стретились столько раз
        frequencyList = [[] for _ in range(len(nums) + 1)]
        for num in count:
            frequency = count[num]
            frequencyList[frequency].append(num)

        # допустим у нас получиллся такой frequencyList:
        # 0: []
        # 1: [2, 5]
        # 2: []
        # 3: [4]
        # 4: []
        # 5: []
        # при k = 2 нам нужно вернуть 4 и 2 или 4 и 5 - без разницы
        # для этого проходимся с конца и ищем первые k элементов
        result = []
        for numsList in reversed(frequencyList):
            for num in numsList:
                if k <= 0:
                    return result
                result.append(num)
                k -= 1
        return result
