def quick_sort(arr: list[int]) -> None:
    """Публичная функция сортировки."""
    if not arr or len(arr) <= 1:
        return
    _quick_sort_hoare(arr, 0, len(arr) - 1)


def _quick_sort_hoare(arr: list[int], start: int, end: int) -> None:
    """Рекурсивная функция быстрой сортировки."""
    if start < end:
        pivot_index = _hoare_partition(arr, start, end)

        # Рекурсивно сортируем левую и правую части
        _quick_sort_hoare(arr, start, pivot_index)
        _quick_sort_hoare(arr, pivot_index + 1, end)


def _hoare_partition(arr: list[int], start: int, end: int) -> int:
    """Схема разделения Хоара с понятными именами переменных."""
    pivot = arr[(start + end) // 2]

    left = start  # Указатель, идущий слева направо
    right = end  # Указатель, идущий справа налево

    while True:
        # Двигаем левый указатель, пока элемент меньше опорного
        while arr[left] < pivot:
            left += 1

        # Двигаем правый указатель, пока элемент больше опорного
        while arr[right] > pivot:
            right -= 1

        # Если указатели встретились или пересеклись
        if left >= right:
            return right  # Возвращаем правый указатель как границу

        # Меняем элементы местами
        arr[left], arr[right] = arr[right], arr[left]

        # Обязательно сдвигаем указатели после обмена
        left += 1
        right -= 1


# Пример
if __name__ == "__main__":
    my_list = [3, 34, 4, 12, 5, 7, 8, 9, 11]
    quick_sort(my_list)
    print(my_list)
