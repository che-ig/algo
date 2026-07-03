from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # Начальная высота байкера равна 0
        current_altitude = 0

        # Максимальная высота также инициализируется 0,
        # так как байкер как минимум находился в точке 0.
        max_altitude = 0

        # Проходим по всем изменениям высоты
        for g in gain:
            # Обновляем текущую высоту, прибавляя изменение
            current_altitude += g

            # Если текущая высота стала больше зафиксированного максимума,
            # обновляем максимум
            if current_altitude > max_altitude:
                max_altitude = current_altitude

        return max_altitude


# --- Проверка на примерах ---
if __name__ == "__main__":
    sol = Solution()
    print(sol.largestAltitude([-5, 1, 5, 0, -7]))  # Ожидается: 1
    print(sol.largestAltitude([-4, -3, -2, -1, 4, 3, 2]))  # Ожидается: 0
