def isReflected_manual_dict(points: list[list[int]]) -> bool:
    """
    Проверка симметрии с учётом дубликатов через обычный словарь.

    Сложность: O(n) по времени, O(n) по памяти.
    """
    if not points:
        return True

    # 1. Находим границы по оси X
    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    sum_x = min_x + max_x  # удвоенная координата оси симметрии

    # 2. Считаем количество каждой точки вручную
    counts = {}
    for x, y in points:
        # Если точки ещё нет в словаре, .get вернёт 0, затем прибавим 1
        counts[(x, y)] = counts.get((x, y), 0) + 1

    # 3. Проверяем симметрию для каждой уникальной точки
    for (x, y), count in counts.items():
        reflected_x = sum_x - x

        # Если количество отражённой точки не совпадает с исходной — симметрии нет
        # .get(..., 0) нужен на случай, если отражённой точки вообще нет в словаре
        if counts.get((reflected_x, y), 0) != count:
            return False

    return True
