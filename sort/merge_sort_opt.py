def merge_sort_optimized(arr: list) -> list:
    """
    Оптимизированная сортировка слиянием.
    Работает непосредственно с исходным массивом (in-place по отношению к переданному списку).
    """
    if not arr:
        return arr

    # Оптимизация 1: Выделяем временный буфер ОДИН раз на весь алгоритм.
    # Это избавляет нас от тысяч аллокаций памяти в рекурсии.
    temp = [0] * len(arr)

    _merge_sort_recursive(arr, temp, 0, len(arr) - 1)
    return arr


def _merge_sort_recursive(arr: list, temp: list, left: int, right: int):
    # Оптимизация 2: Для маленьких подмассивов используем сортировку вставками.
    # Она имеет меньшие константные накладные расходы и быстрее на размерах <= 16-32.
    THRESHOLD = 16
    if right - left <= THRESHOLD:
        _insertion_sort(arr, left, right)
        return

    mid = (left + right) // 2

    # Рекурсивно сортируем половины
    _merge_sort_recursive(arr, temp, left, mid)
    _merge_sort_recursive(arr, temp, mid + 1, right)

    # Оптимизация 3: Пропускаем слияние, если массив уже отсортирован.
    # Если последний элемент левой части меньше или равен первому элементу правой,
    # значит, они уже идут в правильном порядке. Слияние не нужно!
    if arr[mid] <= arr[mid + 1]:
        return

    # Если дошли сюда, сливаем
    _merge(arr, temp, left, mid, right)


def _merge(arr: list, temp: list, left: int, mid: int, right: int):
    # Оптимизация 4: Копируем в буфер ТОЛЬКО левую часть.
    # Правая часть уже находится в исходном массиве, и мы можем читать её оттуда.
    # Это сокращает объем копируемых данных вдвое.
    for i in range(left, mid + 1):
        temp[i] = arr[i]

    i = left  # Указатель на левую часть (в буфере temp)
    j = mid + 1  # Указатель на правую часть (в исходном arr)
    k = left  # Указатель для записи результата в исходный arr

    # Слияние
    while i <= mid and j <= right:
        if temp[i] <= arr[j]:
            arr[k] = temp[i]
            i += 1
        else:
            arr[k] = arr[j]
            j += 1
        k += 1

    # Если в левой части (в буфере) остались элементы, копируем их в конец.
    # (Остатки правой части копировать не нужно, они уже на своих местах в arr).
    while i <= mid:
        arr[k] = temp[i]
        k += 1
        i += 1


def _insertion_sort(arr: list, left: int, right: int):
    """Вспомогательная функция: сортировка вставками для малого диапазона."""
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        # Двигаем элементы вправо, пока они больше key
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# ==========================================
# Пример использования
# ==========================================
if __name__ == "__main__":
    my_list = [38, 27, 43, 3, 9, 82, 10, 19, -5, 0, 15, 2, 88, 41, 55, 12, 7]
    print(f"Исходный: {my_list}")

    merge_sort_optimized(my_list)

    print(f"Результат:  {my_list}")
