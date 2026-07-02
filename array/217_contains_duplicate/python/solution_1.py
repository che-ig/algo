from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Создаем пустое множество для хранения уже встреченных чисел
        seen = set()

        # Проходим по каждому числу в массиве
        for num in nums:
            # Если число уже есть в множестве, значит, мы нашли дубликат
            if num in seen:
                return True
            # Иначе добавляем число в множество
            seen.add(num)

        # Если цикл завершился и мы не вернули True, значит все элементы уникальны
        return False
