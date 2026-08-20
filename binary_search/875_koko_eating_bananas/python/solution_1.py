class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def good(k: int) -> bool:
            """
            Проверяет, успеет ли Коко съесть все бананы за h часов,
            если будет есть со скоростью k бананов в час.

            Для каждой кучи piles[i] нужно ceil(piles[i] / k) часов.
            Суммируем по всем кучам и сравниваем с h.
            """
            total_hours = 0
            for pile in piles:
                # Округление вверх: (pile + k - 1) // k
                # Это то же самое, что math.ceil(pile / k), но быстрее
                total_hours += (pile + k - 1) // k
            return total_hours <= h

        # Диапазон поиска скорости:
        # lo = 1 (минимальная возможная скорость)
        # hi = max(piles) (максимальная — съесть самую большую кучу за 1 час)
        lo = 1
        hi = max(piles)
        ans = hi  # По умолчанию — максимальная скорость

        # Бинарный поиск первого значения, где good(k) = True
        while lo <= hi:
            mi = lo + (hi - lo) // 2

            if good(mi):
                # Если со скоростью mi успевает — запоминаем ответ
                # и пробуем уменьшить скорость (ищем минимум)
                ans = mi
                hi = mi - 1
            else:
                # Если не успевает — скорость слишком маленькая,
                # нужно увеличить
                lo = mi + 1

        return ans
