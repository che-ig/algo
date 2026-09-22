from collections import deque

"""
BFS / Алгоритм Кана (топологическая сортировка)
Идея: считаем входящие степени (in-degree) каждого узла — количество пререквизитов. Узлы с in-degree = 0 можно пройти сразу (у них нет пререквизитов). Проходим их, "освобождаем" зависимые курсы (уменьшаем их in-degree), и повторяем.
Если в конце все курсы прошли — цикла нет. Если остались непройденные — есть цикл.
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Шаг 1: Строим граф и считаем входящие степени
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses  # in_degree[course] = кол-во пререквизитов

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            in_degree[course] += 1

        # Шаг 2: Находим все курсы без пререквизитов (in-degree == 0)
        # Это наши "стартовые" курсы — можно проходить сразу
        queue = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)

        # Шаг 3: Обрабатываем курсы в порядке готовности
        courses_completed = 0

        while queue:
            current_course = queue.popleft()
            courses_completed += 1

            # "Проходим" текущий курс — освобождаем зависимые от него
            for next_course in graph[current_course]:
                in_degree[next_course] -= 1  # Один пререквизит выполнен

                # Если все пререквизиты next_course выполнены — добавляем в очередь
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        # Шаг 4: Если прошли все курсы — цикла нет
        return courses_completed == numCourses
