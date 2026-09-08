class Solution:
    def longestConsecutive(self, nums):
        # Преобразуем список в множество для O(1) проверки наличия элемента
        num_set = set(nums)
        max_len = 0

        for num in nums:
            # КЛЮЧЕВАЯ ОПТИМИЗАЦИЯ:
            # Начинаем считать последовательность ТОЛЬКО если num — её начало
            # То есть num - 1 отсутствует в множестве
            if num - 1 not in num_set:
                # Считаем длину последовательности, начиная с num
                current_num = num
                current_len = 1

                # Пока следующее число есть в множестве — продолжаем
                while current_num + 1 in num_set:
                    current_num += 1
                    current_len += 1

                # Обновляем максимум
                if current_len > max_len:
                    max_len = current_len

        return max_len
