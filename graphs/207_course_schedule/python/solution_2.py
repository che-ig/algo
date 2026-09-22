class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """
        Проверяет, можно ли пройти все курсы (нет ли цикла в графе).
        Использует итеративный DFS с явным стеком.
        """
        # Шаг 1: Строим ориентированный граф (список смежности)
        # graph[course] = список курсов, которые можно пройти ПОСЛЕ course
        graph = [[] for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        # Шаг 2: Массив состояний узлов
        # 0 — не посещён, 1 — в процессе обхода, 2 — полностью обработан
        node_state = [0] * numCourses

        # Шаг 3: Итеративный DFS с явным стеком
        for start_course in range(numCourses):
            # Пропускаем уже обработанные узлы
            if node_state[start_course] != 0:
                continue

            # Стек хранит пары: (узел, is_returning)
            # is_returning = False → начало обработки узла
            # is_returning = True  → завершение обработки (все соседи проверены)
            stack = [(start_course, False)]

            while stack:
                current_course, is_returning = stack.pop()

                if is_returning:
                    # Все соседи current_course обработаны без цикла.
                    # Помечаем узел как "полностью обработанный".
                    node_state[current_course] = 2
                    continue

                # Проверяем текущее состояние узла
                if node_state[current_course] == 2:
                    # Узел уже полностью обработан в предыдущих обходах.
                    # Цикла через него нет — пропускаем.
                    continue

                if node_state[current_course] == 1:
                    # Узел уже в процессе обхода (состояние 1).
                    # Мы вернулись к нему, не завершив обработку — это ЦИКЛ!
                    return False

                # Помечаем узел как "в процессе обхода"
                node_state[current_course] = 1

                # ВАЖНО: сначала добавляем маркер завершения,
                # потом всех соседей. Так мы гарантируем, что маркер
                # будет извлечён ПОСЛЕ обработки всех соседей (LIFO).
                stack.append((current_course, True))

                # Добавляем всех соседей в стек для обработки
                for next_course in graph[current_course]:
                    stack.append((next_course, False))

        # Если прошли все узлы и не нашли цикл — курсы можно завершить
        return True
