def heap_sort(arr: list[int]) -> None:
    """
    Пирамидальная сортировка.
    Изменяет исходный массив на месте (in-place).
    """
    n = len(arr)

    # Шаг 1: Строим max-heap из всего массива
    # Начинаем с последнего родительского узла и идем к корню
    for parent_index in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, parent_index)

    # Шаг 2: Извлекаем элементы из кучи по одному
    for last_index in range(n - 1, 0, -1):
        # Перемещаем текущий максимум (корень) в конец массива
        arr[0], arr[last_index] = arr[last_index], arr[0]

        # Восстанавливаем свойство кучи для уменьшенной кучи
        _heapify(arr, last_index, 0)


def _heapify(arr: list[int], heap_size: int, root_index: int) -> None:
    """
    Восстанавливает свойство max-heap для поддерева с корнем в root_index.
    heap_size — размер кучи (может быть меньше len(arr) при сортировке).
    """
    largest = root_index  # Предполагаем, что корень — наибольший

    left_child = 2 * root_index + 1  # Индекс левого ребенка
    right_child = 2 * root_index + 2  # Индекс правого ребенка

    # Если левый ребенок существует и больше корня
    if left_child < heap_size and arr[left_child] > arr[largest]:
        largest = left_child

    # Если правый ребенок существует и больше текущего наибольшего
    if right_child < heap_size and arr[right_child] > arr[largest]:
        largest = right_child

    # Если наибольший элемент не корень, меняем их местами
    if largest != root_index:
        arr[root_index], arr[largest] = arr[largest], arr[root_index]

        # Рекурсивно восстанавливаем кучу для пострадавшего поддерева
        _heapify(arr, heap_size, largest)


# Пример использования
if __name__ == "__main__":
    my_list = [3, 34, 4, 12, 5, 7, 8, 9, 11]
    print(f"Исходный: {my_list}")

    heap_sort(my_list)

    print(f"Результат: {my_list}")
