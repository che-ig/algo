class Solution:
    # time: O(n)
    # mem: O(1)
    def moveZeroes(self, nums: list[int]) -> None:
        # Note: задача может формулироваться как "удалить все 0 из массива"
        # тут смысл такой же, просто делаем resize в конце или попаем (зависит от ЯП)

        freeIdx = 0  # указывает на какую позицию поставим следующий элемент не равный 0
        for num in nums:
            if num == 0:
                continue
            nums[freeIdx] = num
            freeIdx += 1

        for i in range(freeIdx, len(nums)):
            nums[i] = 0


class Solution_2:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Перемещает все нули в конец массива in-place.
        Минимизирует количество операций записи.
        """
        # write — индекс, куда будет записан следующий ненулевой элемент.
        # Изначально указывает на начало массива.
        write = 0

        # === ПРОХОД 1: Сдвигаем все ненулевые элементы влево ===
        # Проходим по массиву и каждый ненулевой элемент записываем
        # на позицию write, затем увеличиваем write.
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1

        # === ПРОХОД 2: Заполняем хвост нулями ===
        # Все позиции от write до конца массива должны быть нулями.
        for i in range(write, len(nums)):
            nums[i] = 0
