class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SparseTableIndex:
    def __init__(self, arr: list[int]) -> None:
        """
        Sparse Table, которая возвращает ИНДЕКС минимального элемента.
        Нужно для алгоритма LCA через Эйлеров обход.
        """
        self.n = len(arr)
        if self.n == 0:
            return

        self.arr = arr

        # ПРЕДПОДСЧЕТ ЛОГАРИФМОВ
        self.log_table = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.log_table[i] = self.log_table[i // 2] + 1

        self.k_max = self.log_table[self.n] + 1

        # table[k][i] = ИНДЕКС минимального элемента на отрезке [i, i + 2^k - 1]
        self.table: list[list[int]] = [[0] * self.n for _ in range(self.k_max)]

        # База: k=0
        for i in range(self.n):
            self.table[0][i] = i

        # Заполнение таблицы
        for k in range(1, self.k_max):
            step = 1 << (k - 1)
            for i in range(self.n - (1 << k) + 1):
                left_idx = self.table[k - 1][i]
                right_idx = self.table[k - 1][i + step]

                # Сравниваем ЗНАЧЕНИЯ по индексам
                if arr[left_idx] <= arr[right_idx]:
                    self.table[k][i] = left_idx
                else:
                    self.table[k][i] = right_idx

    def query_index(self, left: int, right: int) -> int:
        """
        Возвращает ИНДЕКС минимального элемента на отрезке [left, right].
        """
        length = right - left + 1
        k = self.log_table[length]  # БЫСТРО!

        left_idx = self.table[k][left]
        right_idx = self.table[k][right - (1 << k) + 1]

        if self.arr[left_idx] <= self.arr[right_idx]:
            return left_idx
        else:
            return right_idx

    def query(self, left: int, right: int) -> int:
        """
        Возвращает ЗНАЧЕНИЕ минимального элемента на отрезке [left, right].
        """
        min_idx = self.query_index(left, right)
        return self.arr[min_idx]


# Препроцессинг: O(NlogN)
# Запрос LCA: O(1)
# Для Q запросов: O(NlogN+Q)
class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode | None, p: TreeNode, q: TreeNode
    ) -> TreeNode | None:
        """
        LCA через Эйлеров обход + Sparse Table с предподсчетом логарифмов.
        Препроцессинг: O(N log N)
        Запрос: O(1)
        """
        euler: list[TreeNode] = []
        depth: list[int] = []
        first: dict[TreeNode, int] = {}

        def dfs(node: TreeNode | None, d: int) -> None:
            if not node:
                return
            first[node] = len(euler)
            euler.append(node)
            depth.append(d)
            if node.left:
                dfs(node.left, d + 1)
                euler.append(node)
                depth.append(d)
            if node.right:
                dfs(node.right, d + 1)
                euler.append(node)
                depth.append(d)

        dfs(root, 0)

        # Строим Sparse Table с предподсчетом логарифмов
        st = SparseTableIndex(depth)

        # Отвечаем на запрос за O(1)
        i, j = first[p], first[q]
        if i > j:
            i, j = j, i

        min_idx = st.query_index(i, j)
        return euler[min_idx]
