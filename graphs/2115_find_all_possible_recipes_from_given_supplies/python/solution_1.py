from collections import defaultdict, deque


class Solution:
    def findAllRecipes(
        self,
        recipes: list[str],
        ingredients: list[list[str]],
        supplies: list[str],
    ) -> list[str]:
        # Граф зависимостей: ингредиент -> список рецептов, которые его требуют
        graph = defaultdict(list)

        # in_degree[recipe] = количество недостающих ингредиентов для рецепта
        in_degree = {}

        # Строим граф и считаем зависимости
        for recipe, components in zip(recipes, ingredients):
            # Все ингредиенты рецепта изначально "недоступны"
            in_degree[recipe] = len(components)

            # Для каждого компонента добавляем ребро: компонент -> рецепт
            for component in components:
                graph[component].append(recipe)

        # Очередь инициализируется всеми базовыми ингредиентами (in_degree == 0)
        queue = deque(supplies)

        # Список рецептов, которые удалось приготовить
        result = []

        # Алгоритм Кана: обрабатываем узлы по мере "освобождения"
        while queue:
            current_supply = queue.popleft()

            # Проходим по всем рецептам, которые требуют текущий ингредиент
            for recipe in graph[current_supply]:
                # Один ингредиент стал доступен — уменьшаем счётчик
                in_degree[recipe] -= 1

                # Если все ингредиенты для рецепта собраны
                if in_degree[recipe] == 0:
                    # Рецепт теперь сам становится доступным ингредиентом
                    queue.append(recipe)
                    # Добавляем в результат
                    result.append(recipe)

        return result
