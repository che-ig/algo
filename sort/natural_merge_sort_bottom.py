def natural_merge_sort_bottom_up(arr: list[int]) -> list[int]:
    """
    Natural Merge Sort Bottom-Up.
    Ищет естественные отсортированные серии и сливает их.
    """
    if len(arr) <= 1:
        return arr

    n = len(arr)
    buf = [0] * n  # Один буфер на весь алгоритм (как в прошлой оптимизации)

    while True:
        # Шаг 1: Находим все естественные серии (runs) в массиве
        runs = []
        i = 0
        while i < n:
            start = i
            # Идем вправо, пока элементы не убывают
            while i + 1 < n and arr[i] <= arr[i + 1]:
                i += 1
            i += 1  # Переходим к следующему элементу
            runs.append((start, i))  # (начало, конец) серии

        # Если серия всего одна — массив уже отсортирован!
        if len(runs) == 1:
            break

        # Шаг 2: Сливаем соседние серии попарно
        new_runs = []
        k = 0  # Позиция для записи в buf

        for j in range(0, len(runs) - 1, 2):
            # Берем пару серий: runs[j] и runs[j+1]
            l, mid = runs[j][0], runs[j][1]
            r = runs[j + 1][1]

            # Сливаем их в buf (как в оптимизированной версии)
            buf[l:mid] = arr[l:mid]  # Копируем только левую часть
            p1, p2, idx = 0, mid, l

            while p1 < (mid - l) and p2 < r:
                if buf[p1] <= arr[p2]:
                    arr[idx] = buf[p1]
                    p1 += 1
                else:
                    arr[idx] = arr[p2]
                    p2 += 1
                idx += 1

            # Дописываем остатки
            while p1 < (mid - l):
                arr[idx] = buf[p1]
                p1 += 1
                idx += 1

            new_runs.append((l, r))

        # Если серий нечетное количество — последняя остается без пары
        if len(runs) % 2 == 1:
            last = runs[-1]
            new_runs.append(last)

        runs = new_runs

    return arr
