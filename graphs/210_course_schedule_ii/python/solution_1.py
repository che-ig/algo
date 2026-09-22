from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        """
        Возвращает порядок прохождения курсов (топологическая сортировка).
        Если пройти все курсы невозможно (есть цикл), возвращает пустой список.
        """
        # Шаг 1: Строим ориентированный граф и считаем входящие степени
        # graph[course] = список курсов, которые можно пройти ПОСЛЕ course
        graph = [[] for _ in range(numCourses)]

        # in_degree[course] = количество пререквизитов для course
        in_degree = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            in_degree[course] += 1

        # Шаг 2: Находим все курсы без пререквизитов (in_degree == 0)
        # Это наши "стартовые" курсы — их можно проходить сразу
        queue = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)

        # Шаг 3: Запускаем BFS (алгоритм Кана)
        course_order = []

        while queue:
            current_course = queue.popleft()
            course_order.append(current_course)  # Добавляем в итоговый порядок

            # "Проходим" текущий курс — освобождаем зависимые от него курсы
            for next_course in graph[current_course]:
                in_degree[next_course] -= 1  # Один пререквизит выполнен

                # Если все пререквизиты next_course выполнены — добавляем в очередь
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        # Шаг 4: Проверяем, прошли ли мы все курсы
        # Если нет — значит, в графе есть цикл, и пройти все курсы невозможно
        if len(course_order) == numCourses:
            return course_order
        else:
            return []  # Возвращаем пустой список при наличии цикла
