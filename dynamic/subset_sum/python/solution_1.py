def max_subset_sum_not_exceeding(numbers: list[int], max_sum: int) -> int:
    """
    Находит максимальную сумму подмножества, которая не превышает max_sum.

    Args:
        numbers: Список целых чисел
        max_sum: Максимально допустимая сумма

    Returns:
        Максимальная сумма подмножества <= max_sum
    """
    n = len(numbers)

    # dp[i][j] = True, если сумму j можно набрать используя первые i элементов
    # Создаем таблицу (n+1) x (max_sum+1)
    dp_table = [[False] * (max_sum + 1) for _ in range(n + 1)]

    # Базовый случай: сумму 0 можно набрать всегда (пустое подмножество)
    dp_table[0][0] = True

    # Заполняем таблицу ДП
    for i in range(1, n + 1):
        current_element = numbers[
            i - 1
        ]  # Текущий элемент (индекс i-1 т.к. i начинается с 1)

        for current_sum in range(max_sum + 1):
            # Вариант 1: НЕ берем текущий элемент
            # Наследуем значение из предыдущей строки
            dp_table[i][current_sum] = dp_table[i - 1][current_sum]

            # Вариант 2: Берем текущий элемент (если он помещается)
            if current_sum >= current_element:
                remaining_sum = current_sum - current_element
                # Если оставшуюся сумму можно было набрать без текущего элемента,
                # то и текущую сумму тоже можно набрать
                dp_table[i][current_sum] |= dp_table[i - 1][remaining_sum]

    # Ищем максимальную сумму, которую можно набрать (идем с конца)
    for target_sum in range(max_sum, -1, -1):
        if dp_table[n][target_sum]:
            return target_sum

    return (
        0  # Если ничего не удалось набрать (не должно произойти т.к. dp[n][0] = True)
    )


# ==================== ОПТИМИЗИРОВАННАЯ ВЕРСИЯ ====================
def max_subset_sum_optimized(numbers: list[int], max_sum: int) -> int:
    """
    Оптимизированная версия с использованием O(max_sum) памяти вместо O(n * max_sum).
    """
    # dp[j] = True, если сумму j можно набрать
    dp = [False] * (max_sum + 1)
    dp[0] = True  # Сумму 0 можно набрать всегда

    for num in numbers:
        # Идем справа налево, чтобы не использовать один элемент дважды
        for current_sum in range(max_sum, num - 1, -1):
            if dp[current_sum - num]:
                dp[current_sum] = True

    # Ищем максимальную достижимую сумму
    for target_sum in range(max_sum, -1, -1):
        if dp[target_sum]:
            return target_sum

    return 0


# ==================== ПРИМЕР ИСПОЛЬЗОВАНИЯ ====================
if __name__ == "__main__":
    arr = [3, 7, 2, 9, 4]
    W = 15

    result = max_subset_sum_not_exceeding(arr, W)
    print(f"Максимальная сумма подмножества ≤ {W}: {result}")
    # Ожидаемый ответ: 15 (3 + 2 + 4 + 6 = 15 или 7 + 2 + 4 = 13 или 3 + 7 + 4 = 14)

    # Тест оптимизированной версии
    result_opt = max_subset_sum_optimized(arr, W)
    print(f"Оптимизированная версия: {result_opt}")
