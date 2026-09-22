class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # Строим граф
        graph = [[] for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        # Состояния узлов: 0 — не посещён, 1 — в процессе, 2 — обработан
        node_state = [0] * numCourses
        course_order = []

        def dfs(current_course: int) -> bool:
            """
            Возвращает True, если цикла нет.
            Добавляет current_course в course_order после обработки всех потомков.
            """
            if node_state[current_course] == 2:
                return True  # Уже обработан

            if node_state[current_course] == 1:
                return False  # Найден цикл

            node_state[current_course] = 1  # Помечаем как "в процессе"

            for next_course in graph[current_course]:
                if not dfs(next_course):
                    return False

            node_state[current_course] = 2  # Помечаем как "обработан"
            course_order.append(current_course)  # Добавляем ПОСЛЕ потомков

            return True

        # Запускаем DFS из каждого непосещённого узла
        for course in range(numCourses):
            if node_state[course] == 0:
                if not dfs(course):
                    return []  # Найден цикл

        # Разворачиваем порядок (потому что добавляли после потомков)
        return course_order[::-1]


class Solution_2:
    def hasCycle(
        self,
        currCourseNum: int,
        cources: list[list[int]],
        colors: list[int],
        topologicalOrder: list[int],
    ) -> bool:
        if colors[currCourseNum] == 1:
            return True
        if colors[currCourseNum] == 2:
            return False
        colors[currCourseNum] = 1
        for nextCourseNum in cources[currCourseNum]:
            # проверяем имеется ли цикл
            if self.hasCycle(nextCourseNum, cources, colors, topologicalOrder):
                return True
        topologicalOrder.append(currCourseNum)
        colors[currCourseNum] = 2
        return False

    # time: O(max(n, m))
    # mem:  O(max(n, m)), где n = numCourses, а m = len(prerequisites)
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # делаем список смежности
        cources = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            cources[prerequisite[0]].append(prerequisite[1])

        colors = [0 for _ in range(numCourses)]
        topologicalOrder = []

        for i in range(numCourses):
            isHasCycle = self.hasCycle(i, cources, colors, topologicalOrder)
            if isHasCycle:
                return []
        return topologicalOrder
