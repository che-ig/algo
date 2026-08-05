from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # Сортируем клипы по времени начала (start)
        clips.sort(key=lambda x: x[0])

        clips_count = 0  # Счетчик использованных клипов
        current_end = 0  # Текущая правая граница покрытия
        next_end = 0  # Максимальная граница, которую мы можем достичь на следующем шаге
        i = 0  # Указатель для прохода по отсортированным клипам
        n = len(clips)

        # Пока мы не покрыли весь отрезок [0, time]
        while current_end < time:
            # Пока есть клипы, которые начинаются до или в точке current_end,
            # мы можем их использовать для расширения покрытия
            while i < n and clips[i][0] <= current_end:
                # Ищем клип, который заходит дальше всего
                next_end = max(next_end, clips[i][1])
                i += 1

            # Если после проверки всех доступных клипов мы не смогли продвинуться дальше,
            # значит, образовался разрыв, и покрыть [0, time] невозможно
            if next_end <= current_end:
                return -1

            # Иначе мы делаем "прыжок": добавляем клип и обновляем границу покрытия
            clips_count += 1
            current_end = next_end

        return clips_count
