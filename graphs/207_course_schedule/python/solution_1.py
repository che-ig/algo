class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Шаг 1: Строим ориентированный граф (список смежности)
        # graph[course] = список курсов, которые можно пройти ПОСЛЕ course
        graph = [[] for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        # Шаг 2: Массив состояний узлов
        # 0 — не посещён, 1 — в процессе обхода, 2 — полностью обработан
        node_state = [0] * numCourses

        def dfs(current_course: int) -> bool:
            """
            Возвращает True, если начиная с current_course цикла нет.
            Возвращает False, если найден цикл.
            """
            # Если узел уже полностью обработан — цикла через него нет
            if node_state[current_course] == 2:
                return True

            # Если узел в процессе обхода — мы нашли цикл!
            # Мы вернулись к узлу, который ещё не завершил обработку
            if node_state[current_course] == 1:
                return False

            # Помечаем узел как "в процессе обхода"
            node_state[current_course] = 1

            # Рекурсивно обходим всех соседей (следующие курсы)
            for next_course in graph[current_course]:
                if not dfs(next_course):
                    return False  # Цикл найден в поддереве

            # Все потомки обработаны без цикла — помечаем как завершённый
            node_state[current_course] = 2
            return True

        # Шаг 3: Запускаем DFS из каждого непосещённого узла
        # (граф может быть несвязным)
        for course in range(numCourses):
            if node_state[course] == 0:
                if not dfs(course):
                    return False  # Найден цикл

        return True
