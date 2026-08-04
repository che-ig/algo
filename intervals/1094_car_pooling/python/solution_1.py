class Solution:
    # time: O(n * log n) - тут самое долгое это сортировка
    # mem: O(n)
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        points = []
        for trip in trips:
            # координата точки, сколько ЗАШЛО людей в этой координате
            points.append([trip[1], trip[0]])
            # координата точки, сколько ВЫШЛО людей в этой координате
            # т к люди выходили то указываем их со знаком -
            points.append([trip[2], -trip[0]])
        # нам важно чтобы [1, -1] была раньше точки [1, 10]
        # если [1, 10] до [1, -1], то получается что у нас сначало зашло 10 человек,
        #     а потом вышел 1
        # у нас же люди сначала выходят, а потом уже заходят новые, поэтому
        #     [1, -1] сначала, а потом [1, 10]
        # базовая сортировка обеспечит нужный порядок
        points.sort()
        curr_passangers_count = 0
        # проходим и на каждой точке считаем сколько было пассажиров в каждый момент времени
        # если в какой-то момент их больше, чем capacity, возвращаем False
        for point in points:
            curr_passangers_count += point[1]
            if curr_passangers_count > capacity:
                return False
        return True
