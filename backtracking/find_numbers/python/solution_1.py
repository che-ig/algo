def find_numbers(base: int, n: int, target_sum: int) -> list[str]:
    result = []

    def backtrack(pos: int, current_sum: int, path: list[int]):
        # Базовый случай: все N разрядов заполнены
        if pos == n:
            if current_sum == target_sum:
                # Собираем число из цифр
                result.append("".join(map(str, path)))
            return

        # === ОТСЕЧЕНИЯ (PRUNING) ===

        # 1. Если сумма уже превышена — дальше идти бессмысленно
        if current_sum > target_sum:
            return

        # 2. Если даже максимумом не доберем нужную сумму
        remaining = n - pos
        max_possible = current_sum + remaining * (base - 1)
        if max_possible < target_sum:
            return

        # === ВЫБОР ЦИФРЫ ДЛЯ ТЕКУЩЕГО РАЗРЯДА ===

        # Первая цифра не может быть 0 (иначе число не N-значное)
        start_digit = 1 if pos == 0 else 0

        for digit in range(start_digit, base):
            path.append(digit)
            backtrack(pos + 1, current_sum + digit, path)
            path.pop()  # ОТКАТ (BACKTRACK)

    backtrack(0, 0, [])
    return result


# === Пример запуска ===
# Найдем все 3-значные числа в 10-ричной системе с суммой цифр = 5
print(find_numbers(base=10, n=3, target_sum=5))
# Вывод: ['104', '113', '122', '131', '140', '203', '212', '221', '230',
#         '302', '311', '320', '401', '410', '500']
