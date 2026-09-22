Да, на LeetCode есть **много задач**, которые решаются алгоритмом Кана! Вот основные:

## 🔥 Основные задачи (топологическая сортировка)

### 1. **[Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)** (210) - Medium ⭐

**Самая популярная задача на алгоритм Кана!**

- **Условие:** Вернуть порядок прохождения курсов (не просто `True/False`, а сам порядок)
- **Решение:** Алгоритм Кана с возвратом `topo_order`

```python
# Примерно то же решение, что мы разбирали, но возвращаем order
def findOrder(self, numCourses, prerequisites):
    # ... алгоритм Кана ...
    return topo_order if len(topo_order) == numCourses else []
```

---

### 2. **[Parallel Courses](https://leetcode.com/problems/parallel-courses/)** (1136) - Hard

- **Условие:** Найти минимальное количество семестров для прохождения всех курсов
- **Решение:** Модифицированный алгоритм Кана с **подсчётом уровней**

```python
def minimumSemesters(self, n, relations):
    # Kahn's algorithm + подсчёт слоёв
    semester = 0
    while queue:
        semester += 1
        for _ in range(len(queue)):  # Обрабатываем весь уровень
            # ...
    return semester
```

---

### 3. **[Parallel Courses II](https://leetcode.com/problems/parallel-courses-ii/)** (1494) - Hard (Premium)

- **Условие:** То же, но с ограничением на количество курсов в семестр
- **Решение:** Kahn + жадный выбор + bitmask DP

---

### 4. **[Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)** (269) - Hard (Premium)

**Классическая задача на собеседованиях!**

- **Условие:** По отсортированному списку слов на неизвестном языке восстановить порядок букв
- **Решение:**
  1. Построить граф зависимостей между буквами
  2. Применить алгоритм Кана для топологической сортировки

```python
# Пример: ["wrt", "wrf", "er", "ett", "rftt"]
# Граф: t -> f, w -> e, r -> t, e -> r
# Ответ: "wertf"
```

---

### 5. **[Sequence Reconstruction](https://leetcode.com/problems/sequence-reconstruction/)** (444) - Medium (Premium)

- **Условие:** Проверить, является ли данная последовательность единственной возможной топологической сортировкой
- **Решение:** Kahn's algorithm + проверка однозначности (на каждом шаге в очереди должен быть ровно 1 узел)

---

### 6. **[Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/)** (310) - Medium

- **Условие:** Найти все корни деревьев минимальной высоты
- **Решение:** **Модифицированный алгоритм Кана** для неориентированных графов!
  - Удаляем листья (узлы со степенью 1) слой за слоем
  - Последние 1-2 оставшихся узла — ответ

```python
def findMinHeightTrees(self, n, edges):
    if n == 1: return [0]

    # Строим граф и считаем степени
    degree = [0] * n
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        degree[u] += 1
        degree[v] += 1

    # Начинаем с листьев (degree == 1)
    leaves = deque([i for i in range(n) if degree[i] == 1])

    remaining_nodes = n
    while remaining_nodes > 2:
        leaves_count = len(leaves)
        remaining_nodes -= leaves_count

        for _ in range(leaves_count):
            leaf = leaves.popleft()
            for neighbor in graph[leaf]:
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    leaves.append(neighbor)

    return list(leaves)
```

---

### 7. **[Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states/)** (802) - Medium

- **Условие:** Найти все узлы, из которых нельзя попасть в цикл
- **Решение:** Можно решить через **обратный граф + алгоритм Кана** (удаляем узлы с out_degree == 0)

---

### 8. **[Course Schedule IV](https://leetcode.com/problems/course-schedule-iv/)** (1462) - Medium

- **Условие:** Проверить, является ли курс A пререквизитом курса B (прямым или косвенным)
- **Решение:**
  - Вариант 1: DFS/BFS из каждого узла
  - Вариант 2: **Floyd-Warshall** или **топологическая сортировка + DP**

---

## Сводная таблица

| Задача                          | Сложность | Что нужно вернуть         | Алгоритм        |
| ------------------------------- | --------- | ------------------------- | --------------- |
| Course Schedule (207)           | Medium    | `True/False` (есть цикл?) | Kahn / DFS      |
| **Course Schedule II (210)**    | Medium    | **Порядок курсов**        | **Kahn** ⭐     |
| Parallel Courses (1136)         | Hard      | Мин. количество семестров | Kahn + уровни   |
| Alien Dictionary (269)          | Hard      | Порядок букв              | Kahn            |
| Minimum Height Trees (310)      | Medium    | Корни MHT                 | Kahn (обратный) |
| Find Eventual Safe States (802) | Medium    | Безопасные узлы           | Kahn (обратный) |

---

## 💡 Советы для собеседований

1. **Course Schedule II (210)** — самая частая задача на алгоритм Кана. Выучи её решение наизусть!
2. **Alien Dictionary (269)** — любимая задача Google/Amazon. Показывает, умеешь ли ты строить граф из неочевидных данных.
3. **Minimum Height Trees (310)** — показывает, понимаешь ли ты, что алгоритм Кана можно применять к неориентированным графам.

**Паттерн решения всех этих задач:**

```python
1. Построить граф + in_degree
2. Найти все узлы с in_degree == 0
3. BFS (Kahn):
   - Извлечь узел
   - Уменьшить in_degree соседей
   - Если in_degree == 0 → добавить в очередь
4. Проверить, все ли узлы обработаны
```

Если выучишь этот шаблон — решишь 90% задач на топологическую сортировку! 🎯
