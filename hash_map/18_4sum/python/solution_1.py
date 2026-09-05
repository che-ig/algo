class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        # Сортируем массив для использования двух указателей и пропуска дубликатов
        nums.sort()
        n = len(nums)
        res = []

        # Фиксируем первый элемент четверки
        # Цикл до n-3, потому что после i нужно минимум 3 элемента (j, left, right)
        for i in range(n - 3):
            # Пропускаем дубликаты для первого элемента
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Оптимизация: минимально возможная сумма с текущим i уже больше target
            # Значит, все последующие суммы тоже будут больше — прерываем цикл
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break

            # Оптимизация: максимально возможная сумма с текущим i меньше target
            # Значит, с этим i нужную сумму не получить — переходим к следующему i
            if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
                continue

            # Фиксируем второй элемент четверки
            # Цикл до n-2, потому что после j нужно минимум 2 элемента (left, right)
            for j in range(i + 1, n - 2):
                # Пропускаем дубликаты для второго элемента
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Оптимизация: минимальная сумма с текущими i и j уже больше target
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break

                # Оптимизация: максимальная сумма с текущими i и j меньше target
                if nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target:
                    continue

                # Два указателя для поиска оставшейся пары
                left = j + 1
                right = n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total < target:
                        # Сумма слишком мала — сдвигаем левый указатель вправо
                        left += 1
                    elif total > target:
                        # Сумма слишком велика — сдвигаем правый указатель влево
                        right -= 1
                    else:
                        # Нашли подходящую четверку
                        res.append([nums[i], nums[j], nums[left], nums[right]])

                        # Пропускаем дубликаты для третьего элемента
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Пропускаем дубликаты для четвертого элемента
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        # Сдвигаем оба указателя для поиска следующих пар
                        left += 1
                        right -= 1

        return res
