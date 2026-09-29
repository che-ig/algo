"""
Сложность алгоритма

    Время: O(N), где N — длина массива. Мы делаем ровно один проход по массиву. Операции внутри цикла занимают
    O(1).
    Память: O(1) дополнительной памяти (не считая массива result, который требуется по условию задачи для возврата ответа).


"""


class Solution:
    # time: O(n)
    # mem:  O(n), без учета памяти на ответ O(1)
    def summaryRanges(self, nums: list[int]) -> list[str]:
        l = 0
        r = 0
        result = []
        while l < len(nums):
            # before
            # l
            # 1 2 3 5 7 8
            # r

            # бежим правым указателем пока в интервале [l, r]
            # находятся все последовательные числа
            while r + 1 < len(nums) and nums[r] + 1 == nums[r + 1]:
                r += 1
            # after
            # l
            # 1 2 3 5 7 8
            #     r
            # бежим правым указателем

            # добавлем в ответ
            if r != l:
                result.append(f"{nums[l]}->{nums[r]}")
            else:
                result.append(f"{nums[l]}")

            # интервалы не пересекаются, поэтому сдвигаем
            # на r + 1 - именно отсюда будет начинаться
            # следующий интервал
            l = r + 1
            r = r + 1
        return result


def main():
    """Тест-кейсы для задачи Summary Ranges."""
    solution = Solution()

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ЗАДАЧИ SUMMARY RANGES")
    print("=" * 60)

    # Тест 1: Стандартный случай из примера LeetCode
    nums = [0, 1, 2, 4, 5, 7]
    result = solution.summaryRanges(nums)
    expected = ["0->2", "4->5", "7"]
    print(f"\nТест 1: nums = {nums}")
    print(f"Результат: {result}")
    assert result == expected, (
        f"Тест 1 провален! Ожидалось {expected}, получено {result}"
    )
    print("✓ Пройден")

    # Тест 2: Второй пример из LeetCode
    nums = [0, 2, 3, 4, 6, 8, 9]
    result = solution.summaryRanges(nums)
    expected = ["0", "2->4", "6", "8->9"]
    print(f"\nТест 2: nums = {nums}")
    print(f"Результат: {result}")
    assert result == expected, (
        f"Тест 2 провален! Ожидалось {expected}, получено {result}"
    )
    print("✓ Пройден")

    # Тест 3: Пустой массив (Edge case)
    nums = []
    result = solution.summaryRanges(nums)
    expected = []
    print(f"\nТест 3: nums = {nums} (пустой массив)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 3 провален!"
    print("✓ Пройден")

    # Тест 4: Массив из одного элемента
    nums = [1]
    result = solution.summaryRanges(nums)
    expected = ["1"]
    print(f"\nТест 4: nums = {nums} (один элемент)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 4 провален!"
    print("✓ Пройден")

    # Тест 5: Все элементы идут подряд (один большой диапазон)
    nums = [1, 2, 3, 4, 5]
    result = solution.summaryRanges(nums)
    expected = ["1->5"]
    print(f"\nТест 5: nums = {nums} (один сплошной диапазон)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 5 провален!"
    print("✓ Пройден")

    # Тест 6: Ни один элемент не идет подряд (все диапазоны по 1)
    nums = [1, 3, 5, 7, 9]
    result = solution.summaryRanges(nums)
    expected = ["1", "3", "5", "7", "9"]
    print(f"\nТест 6: nums = {nums} (все элементы изолированы)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 6 провален!"
    print("✓ Пройден")

    # Тест 7: Отрицательные числа и большие значения (проверка границ)
    nums = [-2147483648, -2147483647, 2147483647]
    result = solution.summaryRanges(nums)
    expected = ["-2147483648->-2147483647", "2147483647"]
    print(f"\nТест 7: nums = {nums} (границы 32-битного int)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 7 провален!"
    print("✓ Пройден")

    print("\n" + "=" * 60)
    print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО! ✓")
    print("=" * 60)


"""
На собеседовании

    Сразу укажите на отсортированность: "Так как массив уже отсортирован и уникален, нам не нужно использовать хэш-таблицы или сортировку. Достаточно одного линейного прохода"
    Обозначьте главную ловушку: "Самая частая ошибка в этой задаче — забыть добавить последний диапазон после завершения цикла. Я использую пост-обработку (или два указателя), чтобы этого избежать"
    Упомяните ограничения: "В условиях указаны границы 32-битного целого числа (−231-2^{31}−231 до 231−12^{31}-1231−1). В Python переполнения не будет, но в Java или C++ нужно быть осторожным при вычислении nums[i-1] + 1, чтобы не произошло integer overflow" (Хотя в данном случае мы сравниваем с nums[i], который гарантированно влезает в int, так что переполнения не будет, но упомянуть это — знак опытного разработчика).
"""
if __name__ == "__main__":
    main()
