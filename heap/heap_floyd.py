def build_max_heap(arr: list[int]) -> None:
    """
    Строит max-heap из неупорядоченного массива за O(n).
    Изменяет массив на месте.
    """
    n = len(arr)

    # Начинаем с последнего родителя и идём к корню
    # Последний родитель находится на индексе n // 2 - 1
    for parent_index in range(n // 2 - 1, -1, -1):
        _heapify_down(arr, n, parent_index)


def _heapify_down(arr: list[int], heap_size: int, root_index: int) -> None:
    """
    Просеивает элемент вниз, восстанавливая свойство max-heap.
    """
    largest = root_index
    left_child = 2 * root_index + 1
    right_child = 2 * root_index + 2

    # Если левый ребенок больше текущего наибольшего
    if left_child < heap_size and arr[left_child] > arr[largest]:
        largest = left_child

    # Если правый ребенок больше текущего наибольшего
    if right_child < heap_size and arr[right_child] > arr[largest]:
        largest = right_child

    # Если наибольший элемент не корень, меняем их местами
    if largest != root_index:
        arr[root_index], arr[largest] = arr[largest], arr[root_index]

        # Рекурсивно просеиваем вниз для пострадавшего поддерева
        _heapify_down(arr, heap_size, largest)


# Пример использования
if __name__ == "__main__":
    my_list = [3, 34, 4, 12, 5, 7, 8, 9, 11]
    print(f"До построения кучи: {my_list}")

    build_max_heap(my_list)

    print(f"После построения кучи: {my_list}")

    # Проверка: корень должен быть максимальным элементом
    print(f"Максимальный элемент (корень): {my_list[0]}")
