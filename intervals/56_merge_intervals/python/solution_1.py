class Solution:
    # проверяем пересекаются ли интервалы
    def is_overlapping(self, a, b):
        return max(a[0], b[0]) <= min(a[1], b[1])

    def merge_two_intervals(self, a, b):
        # интервалы обязательно должны пересекаться
        # берем a[0] так как знаем что интревал отсортирован и
        # в нулевом индексе находится меньшее значение.
        return [a[0], max(a[1], b[1])]

    # time: O(N*logN)
    # mem: O(n)
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # O(NlogN)
        intervals.sort()  # start <= end по условию (это важно)

        result = []
        result.append(intervals[0])

        # O(n)
        for i in range(1, len(intervals)):
            interval = intervals[i]
            # если текущий интервал и последний в ответе пересекаются,
            # значит объединяем их, иначе добавляем интервал к ответу и это значит,
            # что ни один интервал, который имеет точку начала меньше текущего интервала
            # не будет пересечен ни с одним лежащим правее и не с текущим
            if self.is_overlapping(result[-1], interval):
                result[-1] = self.merge_two_intervals(result[-1], interval)
            else:
                result.append(interval)
        return result
