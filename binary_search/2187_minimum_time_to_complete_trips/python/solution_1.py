class Solution:
    def minimumTime(self, time: list[int], totalTrips: int) -> int:
        def good(t: int) -> bool:
            """
            Проверяет, успеют ли все автобусы вместе совершить
            как минимум totalTrips рейсов за время t.

            За время t автобус i совершает t // time[i] рейсов.
            Суммируем по всем автобусам и сравниваем с totalTrips.

            Args:
                t: проверяемое время

            Returns:
                True если суммарное количество рейсов >= totalTrips
            """
            total = 0
            for trip_time in time:
                total += t // trip_time
                # Ранний выход: как только набрали нужное количество,
                # дальше считать нет смысла (оптимизация)
                if total >= totalTrips:
                    return True
            return total >= totalTrips

        # Диапазон бинарного поиска:
        # lo = 1 (минимально возможное время)
        # hi = min(time) * totalTrips (худший случай: работает только самый быстрый автобус)
        # Например: time = [1,2,3], totalTrips = 5 → hi = 1 * 5 = 5
        lo = 1
        hi = min(time) * totalTrips

        # Переменная для хранения ответа (минимального подходящего времени)
        ans = hi

        # Бинарный поиск первого значения, где good(t) = True
        while lo <= hi:
            mi = lo + (hi - lo) // 2

            if good(mi):
                # Если за время mi автобусы успевают совершить totalTrips рейсов:
                # 1. Запоминаем mi как потенциальный ответ
                ans = mi
                # 2. Пробуем уменьшить время (ищем минимум)
                hi = mi - 1
            else:
                # Если не успевают — времени слишком мало, нужно увеличить
                lo = mi + 1

        return ans
