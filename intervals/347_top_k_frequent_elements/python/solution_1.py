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
        # значение - список чисел, которые встретились столько раз
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


class Solution_2:
    def topKFrequent(self, nums, k):
        # Шаг 1: Считаем частоты каждого элемента
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

        # Шаг 2: Создаём "корзины" (buckets)
        # Индекс корзины = частота элемента
        # Максимальная возможная частота = len(nums)
        # buckets[0] не используется (частота 0 невозможна для существующего элемента)
        buckets = [[] for _ in range(len(nums) + 1)]

        # Раскладываем элементы по корзинам согласно их частоте
        for num, count in freq.items():
            buckets[count].append(num)

        # Шаг 3: Собираем результат, идя от самой высокой частоты к низкой
        result = []
        # Идём справа налево (от максимальной частоты к минимальной)
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                # Как только набрали k элементов — возвращаем ответ
                if len(result) == k:
                    return result

        return result
