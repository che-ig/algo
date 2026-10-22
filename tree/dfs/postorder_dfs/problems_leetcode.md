# Задачи на LeetCode, где Postorder DFS — естественный выбор

Postorder особенно полезен, когда **для принятия решения о текущем узле нужно сначала знать что-то о его потомках**. Вот подборка задач с нарастающей сложностью.

---

## 🟢 Базовые (для тренировки самого обхода)

### 1. [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)

> Классика — просто реализовать postorder итеративно и рекурсивно.

### 2. [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

> Глубина дерева = `1 + max(глубина_левого, глубина_правого)`. Сначала нужно знать глубины детей.

### 3. [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)

> Проверить, является ли дерево сбалансированным. Для каждого узла нужно знать высоты обоих поддеревьев.

---

## 🟡 Средние (нужны агрегированные данные от детей)

### 4. [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)

> Диаметр = максимальный путь между любыми двумя узлами. Для каждого узла считаем `depth(left) + depth(right)` и обновляем глобальный максимум.

```python
def diameterOfBinaryTree(root):
    ans = 0
    def depth(node):
        nonlocal ans
        if not node: return 0
        l, r = depth(node.left), depth(node.right)
        ans = max(ans, l + r)          # postorder: используем l и r
        return 1 + max(l, r)
    depth(root)
    return ans
```

### 5. [563. Binary Tree Tilt](https://leetcode.com/problems/binary-tree-tilt/)

> Tilt узла = `|sum(left) - sum(right)|`. Нужно сначала посчитать суммы поддеревьев.

### 6. [337. House Robber III](https://leetcode.com/problems/house-robber-iii/)

> Нельзя грабить две связанные квартиры. Для каждого узла возвращаем пару `(rob, skip)` — максимум, если грабим/не грабим текущий дом. Значения детей должны быть известны.

### 7. [1110. Delete Nodes And Return Forest](https://leetcode.com/problems/delete-nodes-and-return-forest/)

> Удалить узлы с заданными значениями. Обрабатываем детей **до** родителя, чтобы корректно отсоединять поддеревья и добавлять их в результат.

### 8. [106. Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder/)

> Восстановить дерево по inorder и postorder. **Корень — последний элемент postorder**, поэтому обход идёт справа налево.

---

## 🔴 Продвинутые (greedy / DP на дереве)

### 9. [968. Binary Tree Cameras](https://leetcode.com/problems/binary-tree-cameras/) ⭐

> Расставить минимальное число камер так, чтобы каждое ребро было покрыто. Классика postorder + greedy.
> Возвращаем статус узла: `0` — не покрыт, `1` — с камерой, `2` — покрыт.

```python
def minCameraCover(root):
    self.ans = 0
    def dfs(node):
        if not node: return 2          # листья-родители считаем "покрытыми"
        l, r = dfs(node.left), dfs(node.right)
        if l == 0 or r == 0:           # хотя бы один ребёнок не покрыт
            self.ans += 1
            return 1                   # ставим камеру здесь
        if l == 1 or r == 1:           # хотя бы один ребёнок с камерой
            return 2                   # этот узел покрыт
        return 0                       # оба ребёнка покрыты, но без камеры
    if dfs(root) == 0: self.ans += 1   # корень не покрыт
    return self.ans
```

### 10. [979. Distribute Coins in Binary Tree](https://leetcode.com/problems/distribute-coins-in-binary-tree/)

> В каждом узле может быть разное число монет, всего их `N`. Нужно за минимальное число ходов сделать так, чтобы в каждом узле была ровно 1 монета.
> Для каждого узла считаем «избыток/недостаток» монет в поддереве: `balance = left + right + node.val - 1`. Ответ += `|balance|`.

```python
def distributeCoins(root):
    self.ans = 0
    def dfs(node):
        if not node: return 0
        l, r = dfs(node.left), dfs(node.right)
        self.ans += abs(l) + abs(r)
        return l + r + node.val - 1
    dfs(root)
    return self.ans
```

### 11. [687. Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/)

> Самый длинный путь, где все узлы имеют одинаковое значение. Для каждого узла нужно знать длины путей в обоих поддеревьях.

### 12. [333. Closest Binary Search Tree Value II](https://leetcode.com/problems/closest-binary-search-tree-value-ii/) / [272. Closest Binary Search Tree Value II](https://leetcode.com/problems/closest-binary-search-tree-value-ii/)

> В некоторых вариациях требуется обход, при котором значения обрабатываются в определённом порядке — postorder помогает «собирать» результаты снизу вверх.

---

## 🧭 Когда выбирать Postorder?

| Признак задачи                                                               | Подсказка    |
| ---------------------------------------------------------------------------- | ------------ |
| Нужно знать что-то о **детях**, чтобы решить задачу для **родителя**         | ✅ Postorder |
| Нужно **удалить/отсоединить** узлы, сохраняя ссылки на детей                 | ✅ Postorder |
| Задача на **агрегацию** (суммы, высоты, балансы)                             | ✅ Postorder |
| **Greedy/DP** на дереве, где решение в узле зависит от решений в поддеревьях | ✅ Postorder |
| Нужно обработать узлы **до** того, как станет доступен родитель              | ✅ Postorder |

Если в задаче вы ловите себя на мысли _«мне бы сначала узнать ответ для детей»_ — почти наверняка это postorder.
