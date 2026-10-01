class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        """
        Находит максимальное расстояние до ближайшего человека,
        если Алекс сядет на оптимальное пустое место.
        """
        num_seats = len(seats)
        max_distance = 0

        # last_occupied_index — индекс последнего встреченного занятого кресла.
        # Инициализируем -1, чтобы обработать случай "пустое начало ряда".
        last_occupied_index = -1

        for current_index in range(num_seats):
            if seats[current_index] == 1:
                if last_occupied_index == -1:
                    # Случай 1: пустые места в начале ряда.
                    # Алекс сядет на самое первое место (индекс 0),
                    # расстояние до ближайшего человека = индекс первого занятого кресла.
                    max_distance = current_index
                else:
                    # Случай 3: пустые места между двумя людьми.
                    # Алекс сядет ровно посередине между ними.
                    # Расстояние = половина расстояния между индексами двух людей.
                    # ВАЖНО: используем (current - last) // 2, а не gap // 2,
                    # потому что расстояние считается от позиции человека,
                    # а не от края пустого места.
                    max_distance = max(
                        max_distance, (current_index - last_occupied_index) // 2
                    )

                # Запоминаем индекс текущего занятого кресла
                last_occupied_index = current_index

        # Случай 2: пустые места в конце ряда.
        # Алекс сядет на самое последнее место (индекс num_seats - 1),
        # расстояние = количество мест от последнего занятого до конца ряда.
        tail_gap = num_seats - 1 - last_occupied_index
        max_distance = max(max_distance, tail_gap)

        return max_distance
