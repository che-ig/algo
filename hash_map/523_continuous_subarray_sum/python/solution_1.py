class Solution:
    def checkSubarraySum(self, nums, k):
        # Словарь хранит ПЕРВЫЙ индекс, на котором встретился каждый остаток
        # {0: -1} — это "виртуальный" префикс до начала массива
        # Нужен для случая, когда префиксная сумма с самого начала кратна k
        remainder_map = {0: -1}

        prefix_sum = 0

        for i, num in enumerate(nums):
            prefix_sum += num
            remainder = prefix_sum % k

            # Если такой остаток уже встречался
            if remainder in remainder_map:
                # Проверяем, что длина подмассива >= 2
                # i - remainder_map[remainder] >= 2
                if i - remainder_map[remainder] >= 2:
                    return True
                # Если длина < 2 — не обновляем индекс,
                # чтобы оставить самую раннюю позицию для будущих проверок
            else:
                # Запоминаем ПЕРВЫЙ индекс с этим остатком
                remainder_map[remainder] = i

        return False
