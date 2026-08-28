def counting_sort(arr: list[int]) -> list[int]:
    """
    Сортировка подсчётом для целых чисел.
    Временная сложность: O(n + k), где k — диапазон значений.
    Пространственная сложность: O(k).
    """
    if not arr:
        return arr

    # Шаг 1: Находим минимум и максимум
    min_val = min(arr)
    max_val = max(arr)

    # Шаг 2: Создаём массив подсчёта
    # Размер = диапазон значений + 1
    count_size = max_val - min_val + 1
    count = [0] * count_size

    # Шаг 3: Подсчитываем количество каждого элемента
    for num in arr:
        count[num - min_val] += 1  # Смещение на min_val для отрицательных чисел

    # Шаг 4: Вычисляем префиксные суммы (позиции в результате)
    # count[i] теперь содержит количество элементов <= (i + min_val)
    for i in range(1, count_size):
        count[i] += count[i - 1]

    # Шаг 5: Заполняем результат в обратном порядке (для устойчивости)
    result = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        num = arr[i]
        # Находим позицию элемента в результате
        pos = count[num - min_val] - 1
        result[pos] = num
        # Уменьшаем счётчик
        count[num - min_val] -= 1

    return result


# Пример использования
if __name__ == "__main__":
    my_list = [4, 2, 2, 8, 3, 3, 1, -2, 0, 5]
    print(f"Исходный: {my_list}")

    sorted_list = counting_sort(my_list)

    print(f"Результат: {sorted_list}")
