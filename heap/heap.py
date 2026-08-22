# Импортируем необходимые типы для типизации и работы с дженериками
from typing import Any, Generic, Protocol, Sequence, TypeVar


# Протокол Comparable определяет интерфейс для объектов, поддерживающих
# операции сравнения "меньше" (<) и "больше" (>).
class Comparable(Protocol):
    def __lt__(self, param: Any) -> bool: ...

    def __gt__(self, param: Any) -> bool: ...


# Объявляем переменную типа T, которая ограничена протоколом Comparable.
# Это значит, что в наши структуры данных можно будет класть только сравниваемые объекты.
T = TypeVar("T", bound=Comparable)


# Протокол Heapable описывает интерфейс структуры данных, подходящей для реализации кучи.
# Она должна поддерживать получение длины, доступ по индексу, изменение элементов,
# а также методы добавления в конец (append) и удаления с конца (pop).
class Heapable(Protocol[T]):
    def __len__(self) -> int: ...

    def __getitem__(self, idx: Any) -> T: ...

    def __setitem__(self, idx: Any, val: T) -> None: ...

    def append(self, val: T) -> None: ...

    def pop(self) -> T: ...


# Вспомогательная функция для сравнения двух элементов.
# Возвращает True, если a > b. Это обеспечивает построение мин-кучи (min-heap),
# так как условие нарушения кучи срабатывает, когда родитель больше потомка.
def compare(a: T, b: T) -> bool:
    return a > b


# Функция "просеивания" элемента вниз (sift down).
# Используется для восстановления свойств кучи, когда элемент на позиции i
# может быть больше своих потомков. Параметр n ограничивает рабочую область кучи.
def heap_heapify_down(heap: Heapable[T], i: int, n: int) -> None:
    while True:
        # Вычисляем индексы левого и правого потомков для текущего узла i
        left = i * 2 + 1
        right = i * 2 + 2
        # Изначально предполагаем, что текущий узел — самый маленький (для мин-кучи)
        smallest = i

        # Если левый потомок существует и он меньше текущего "самого маленького", обновляем индекс
        if left < n and compare(heap[smallest], heap[left]):
            smallest = left

        # Если правый потомок существует и он меньше текущего "самого маленького", обновляем индекс
        if right < n and compare(heap[smallest], heap[right]):
            smallest = right

        # Если текущий узел уже является самым маленьким среди себя и потомков,
        # свойство кучи восстановлено, прерываем цикл.
        if i == smallest:
            break

        # Меняем местами текущий узел и наименьшего из его потомков
        heap[smallest], heap[i] = heap[i], heap[smallest]

        # Спускаемся ниже к потомку и продолжаем просеивание
        i = smallest


# Функция "просеивания" элемента вверх (sift up).
# Применяется, когда новый элемент добавляется в конец кучи и может быть меньше своего родителя.
def heap_heapify_up(heap: Heapable[T], i: int) -> None:
    # Цикл выполняется, пока мы не достигли корня (i > 0) и пока родитель больше текущего элемента
    while i > 0 and compare(heap[(i - 1) // 2], heap[i]):
        # Меняем местами элемент и его родителя
        heap[(i - 1) // 2], heap[i] = heap[i], heap[(i - 1) // 2]
        # Перемещаемся на позицию родителя для следующей итерации
        i = (i - 1) // 2


# Добавление нового элемента в кучу.
# Элемент добавляется в самый конец массива, после чего "просеивается" вверх.
def heap_push(heap: Heapable[T], val: T) -> None:
    heap.append(val)
    heap_heapify_up(heap, len(heap) - 1)


# Извлечение корневого (минимального) элемента из кучи.
# На место корня ставится последний элемент массива, который затем просеивается вниз.
def heap_pop(heap: Heapable[T]):
    heap[0] = heap[-1]
    heap.pop()
    heap_heapify_down(heap, 0, len(heap))


# Построение кучи из произвольного неотсортированного массива за время O(n).
# Мы начинаем с последнего узла, у которого есть потомки, и идем к корню,
# вызывая просеивание вниз для каждого узла.
def heap_make(heap: Heapable[T]) -> None:
    for i in range(len(heap) // 2, -1, -1):
        heap_heapify_down(heap, i, len(heap))


# Пирамидальная сортировка (Heap Sort).
def heap_sort(heap: Heapable[T]) -> None:
    N = len(heap)
    # 1. Строим мин-кучу из исходного массива
    heap_make(heap)

    # 2. Так как у нас мин-куча, корень всегда содержит минимум.
    # Мы меняем его местами с последним элементом текущей неотсортированной части.
    for i in range(N - 1, 0, -1):
        heap[0], heap[i] = heap[i], heap[0]
        # После обмена восстанавливаем свойства кучи для оставшейся части (размером i)
        heap_heapify_down(heap, 0, i)

    # 3. В результате предыдущего шага массив оказался отсортирован по убыванию
    # (минимумы уходили в конец). Разворачиваем массив, чтобы получить сортировку по возрастанию.
    for i in range(N // 2):
        heap[i], heap[N - i - 1] = heap[N - i - 1], heap[i]


# Рекурсивная функция для проверки, является ли структура данных валидной мин-кучей.
# Проверяет свойство кучи для узла idx и всех его потомков.
def heap_isheap(heap: Heapable[T], idx: int) -> bool:
    # Базовый случай рекурсии: если индекс вышел за пределы массива, возвращаем True
    if idx >= len(heap):
        return True

    # Индексы левого и правого потомков
    left = 2 * idx + 1
    right = 2 * idx + 2

    # Если левый потомок существует и родитель больше него, свойство мин-кучи нарушено
    if left < len(heap) and compare(heap[idx], heap[left]):
        return False

    # Если правый потомок существует и родитель больше него, свойство мин-кучи нарушено
    if right < len(heap) and compare(heap[idx], heap[right]):
        return False

    # Если для текущего узла свойство выполнено, рекурсивно проверяем левое и правое поддеревья
    return heap_isheap(heap, left) and heap_isheap(heap, right)


# Тестовый блок, выполняемый при прямом запуске скрипта
if __name__ == "__main__":
    # Тестовый набор данных
    DATA = [5, 3, 1, 2, 4, -2, -40, 100]
    # Ожидаемый отсортированный результат
    DATA_SORTED = [-40, -2, 1, 2, 3, 4, 5, 100]

    # Вспомогательная функция: создает кучу, последовательно добавляя элементы через heap_push
    def ConstructByPushing(nums: list[int]) -> list[int]:
        heap: list[int] = []
        for num in nums:
            heap_push(heap, num)
        return heap

    # Вспомогательная функция: извлекает все элементы из кучи по одному (с начала)
    def RemoveOneByOne(heap) -> list[int]:
        removed = []
        while heap:
            removed.append(heap[0])
            heap_pop(heap)
        return removed

    # Вспомогательная функция: применяет пирамидальную сортировку к копии массива
    def ApplyHeapSort(nums):
        ans = nums[:]
        heap_sort(ans)
        return ans

    # Вспомогательная функция: строит кучу из копии массива с помощью heap_make
    def ApplyMakeHeap(nums):
        ans = nums[:]
        heap_make(ans)
        return ans

    # Тест 1: Проверяем, что куча, созданная последовательными push-ами, валидна
    assert heap_isheap(ConstructByPushing(DATA), 0) == True
    # Тест 2: Проверяем, что поочередное извлечение дает отсортированный массив
    assert RemoveOneByOne(ConstructByPushing(DATA)) == DATA_SORTED
    # Тест 3: Проверяем корректность работы алгоритма heap_sort
    assert ApplyHeapSort(DATA) == DATA_SORTED
    # Тест 4: Проверяем, что heap_make корректно строит валидную кучу за O(n)
    assert heap_isheap(ApplyMakeHeap(DATA), 0) == True
    # Тест 5: Проверяем извлечение элементов из кучи, построенной через heap_make
    assert RemoveOneByOne(ApplyMakeHeap(DATA)) == DATA_SORTED

    # Выводим сообщение, если все тесты пройдены успешно
    print("OK")
