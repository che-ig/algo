def knapsack(N, W, weights, values):
    INF = float("-inf")
    dp = [[INF] * (W + 1) for _ in range(N + 1)]

    # Начальное условие: 0 ценность при весе 0
    dp[0][0] = 0

    for i in range(1, N + 1):
        for j in range(W + 1):
            # Если не берём предмет i-1
            dp[i][j] = dp[i - 1][j]

            # Если берём предмет i-1 (проверяем, влезает ли)
            if j >= weights[i - 1] and dp[i - 1][j - weights[i - 1]] != INF:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])

    max_value = max(dp[N][j] for j in range(W + 1) if dp[N][j] != INF)
    return max_value


def knapsack_optimized(N: int, W: int, weights: list[int], values: list[int]) -> int:
    """
    Классическая задача о рюкзаке 0/1.

    Args:
        N: количество предметов
        W: вместимость рюкзака
        weights: веса предметов
        values: стоимости предметов

    Returns:
        Максимальная стоимость, которую можно набрать
    """
    # dp[i][j] = максимальная стоимость при использовании первых i предметов и весе <= j
    dp = [[0] * (W + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        current_weight = weights[i - 1]
        current_value = values[i - 1]

        for j in range(W + 1):
            # Не берём предмет — наследуем значение
            dp[i][j] = dp[i - 1][j]

            # Берём предмет, если он влезает
            if j >= current_weight:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - current_weight] + current_value)

    return dp[N][W]


# Оптимизация по памяти: O(W) вместо O(N*W)
def knapsack_memory_optimized(
    N: int, W: int, weights: list[int], values: list[int]
) -> int:
    dp = [0] * (W + 1)

    for i in range(N):
        weight = weights[i]
        value = values[i]

        # Идём справа налево, чтобы не использовать предмет дважды
        for j in range(W, weight - 1, -1):
            dp[j] = max(dp[j], dp[j - weight] + value)

    return dp[W]


# Пример использования
if __name__ == "__main__":
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    W = 8
    N = len(weights)

    print(f"Максимальная стоимость: {knapsack_optimized(N, W, weights, values)}")
    # Ожидаемый ответ: 10 (предметы с весами 3+5=8, стоимости 4+6=10)

    print(
        f"Оптимизированная версия: {knapsack_memory_optimized(N, W, weights, values)}"
    )
