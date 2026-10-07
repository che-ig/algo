class Solution:
    def checkRecord(self, s: str) -> bool:
        absences = 0
        count_l = 0
        last_idx_l = -2  # Инициализируем так, чтобы первый 'L' начал серию с 1

        for i, char in enumerate(s):
            if char == "A":
                absences += 1
                if absences >= 2:
                    return False

            elif char == "L":
                if i - last_idx_l == 1:
                    # 'L' идёт сразу после предыдущего 'L' — серия продолжается
                    count_l += 1
                else:
                    # Разрыв в серии — начинаем новую серию с 1
                    count_l = 1

                last_idx_l = i  # Обновляем индекс последнего 'L'

                if count_l >= 3:
                    return False

        return True
