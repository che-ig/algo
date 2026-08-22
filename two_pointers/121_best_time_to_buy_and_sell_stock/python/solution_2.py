class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Количество дней
        n = len(prices)

        # Словарь для мемоизации (кэширования результатов)
        # Ключ: кортеж (day, holding) — состояние системы
        # Значение: максимальная прибыль из этого состояния
        # Это нужно, чтобы не вычислять одно и то же состояние дважды
        memo = {}

        def solve(day: int, holding: bool) -> int:
            """
            Рекурсивная функция с ручной мемоизацией.
            """
            # ===== БАЗОВЫЙ СЛУЧАЙ =====
            # Если дни закончились, прибыль больше не получить
            if day >= n:
                return 0

            # ===== ПРОВЕРКА КЭША =====
            # Перед вычислением проверяем, не считали ли мы уже это состояние
            # Если результат есть в словаре memo, возвращаем его сразу
            if (day, holding) in memo:
                return memo[(day, holding)]

            # ===== ОСНОВНАЯ ЛОГИКА =====
            if holding:
                # Держим акцию: выбираем между продажей и ожиданием
                profit_if_sell = prices[day] + solve(day + 1, False)
                profit_if_skip = solve(day + 1, True)
                result = max(profit_if_sell, profit_if_skip)
            else:
                # Не держим: выбираем между покупкой и ожиданием
                profit_if_buy = -prices[day] + solve(day + 1, True)
                profit_if_skip = solve(day + 1, False)
                result = max(profit_if_buy, profit_if_skip)

            # ===== СОХРАНЕНИЕ В КЭШ =====
            # Перед возвратом сохраняем результат в словарь,
            # чтобы при следующем вызове с теми же параметрами
            # не вычислять заново, а просто вернуть из memo
            memo[(day, holding)] = result

            return result

        # Запускаем рекурсию с начального состояния
        return solve(0, False)
