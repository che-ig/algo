class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """
        Возвращает количество камней в stones, которые являются драгоценными.

        Используем set для jewels, чтобы поиск занимал O(1) вместо O(M).
        """
        # Превращаем строку jewels в множество символов.
        # Это занимает O(M) времени и O(M) памяти, где M = len(jewels).
        # По условию все символы в jewels уникальны, так что set здесь идеален.
        #
        # Пример: jewels = "aA" → jewel_set = {'a', 'A'}
        jewel_set = set(jewels)

        # Счётчик драгоценных камней
        count = 0

        # Проходим по всем камням, которые у нас есть
        for stone in stones:
            # Проверяем, является ли камень драгоценным.
            # Поиск в set работает за O(1) в среднем (хеш-таблица).
            if stone in jewel_set:
                count += 1

        return count
