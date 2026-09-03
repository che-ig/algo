class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def constructMaximumBinaryTree(nums: list[int]) -> TreeNode | None:
    """
    Оптимизированная рекурсия: работаем с индексами, а не со срезами.

    Вместо копирования массива передаём границы [left, right) подмассива.
    Это снижает расход памяти и ускоряет работу.
    """

    # Внутренняя рекурсивная функция
    def build(left: int, right: int) -> TreeNode | None:
        """
        Строит максимальное дерево на подмассиве nums[left:right].

        :param left:  левая граница (включительно)
        :param right: правая граница (исключительно)
        :return: корень построенного поддерева или None
        """
        # Базовый случай: подмассив пуст
        if left >= right:
            return None

        # Ищем индекс максимума в nums[left:right]
        max_idx = left
        for i in range(left + 1, right):
            if nums[i] > nums[max_idx]:
                max_idx = i

        # Создаём корень с максимальным значением
        root = TreeNode(nums[max_idx])

        # Рекурсивно строим левое поддерево на [left, max_idx)
        root.left = build(left, max_idx)

        # Рекурсивно строим правое поддерево на [max_idx + 1, right)
        root.right = build(max_idx + 1, right)

        return root

    # Запускаем рекурсию на всём массиве
    return build(0, len(nums))


"""
Сложность

    Время: O(n log n) в среднем (дерево сбалансировано), O(n²) в худшем случае (отсортированный массив).
    Память: O(n) — только стек рекурсии, без копирования массивов.
"""
