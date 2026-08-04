class Solution:
    # проверяем пересекаются ли интервалы
    def is_overlapping(self, a, b):
        return max(a[0], b[0]) <= min(a[1], b[1])

    # интервалы обязательно должны пересекаться
    def overlap_two_intervals(self, a, b):
        return [max(a[0], b[0]), min(a[1], b[1])]

    # time: O(n * log n)
    # mem: O(1) при условии, что сортировка делается in-place (т е не создает доп массивы и т д)
    def findMinArrowShots(self, intervals: list[list[int]]) -> int:
        intervals.sort()  # O(n * log n)
        result = 1
        last_interval = intervals[0]
        for interval in intervals:
            # если интервалы пересекаются, то для них используем 1 стрелу
            # и стараемся набрать как можно больше интервалов под 1 стрелу
            if self.is_overlapping(last_interval, interval):
                last_interval = self.overlap_two_intervals(last_interval, interval)
                continue
            # если нет пересичений значит нужна еще 1 доп стрела и обновляем
            # последний интервал (last_point)
            last_interval = interval
            result += 1
        return result
