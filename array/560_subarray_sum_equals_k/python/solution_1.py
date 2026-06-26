class Solution:
    # time: O(n)
    # mem: O(n)
    def subarraySum(self, nums: list[int], targetSum: int) -> int:
        # ключ - префиксная сумма, значение - сколько раз встретили
        prefix_sums = {0: 1}

        # текущая префиксная сумма
        current_prefix_sum = 0

        # ответ
        count = 0
        for el in nums:
            current_prefix_sum += el

            # проверяем встречали ли мы уже префиксный массив с суммой current_prefix_sum - targetSum
            if (current_prefix_sum - targetSum) in prefix_sums:
                # если встречали - то к ответу прибавлем число сколько раз уже встретили
                count += prefix_sums[current_prefix_sum - targetSum]

            # добавляем текущую префиксную сумму в массив
            if current_prefix_sum not in prefix_sums:
                prefix_sums[current_prefix_sum] = 0
            prefix_sums[current_prefix_sum] += 1
        return count


# AI solution
def subarraySum(nums: list[int], k: int) -> int:
    # Словарь хранит: сколько раз встречалась каждая префиксная сумма
    # {0: 1} обязательно, чтобы обрабатывать подмассивы, начинающиеся с индекса 0
    prefix_count = {0: 1}

    prefix_sum = 0  # Текущая сумма от начала массива до текущего элемента
    count = 0  # Итоговое количество подмассивов с суммой k

    for num in nums:
        prefix_sum += num

        # Проверяем, встречалась ли сумма (prefix_sum - k) ранее
        if (prefix_sum - k) in prefix_count:
            count += prefix_count[prefix_sum - k]

        # Обновляем частоту текущей префиксной суммы в словаре
        prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

    return count
