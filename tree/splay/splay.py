from __future__ import annotations

from typing import Iterator

# ============================================================================
# Узел Splay-дерева
# ============================================================================


class SplayNode:
    """Узел Splay-дерева."""

    __slots__ = ("key", "left", "right", "parent")

    def __init__(self, key: int) -> None:
        self.key: int = key
        self.left: SplayNode | None = None
        self.right: SplayNode | None = None
        self.parent: SplayNode | None = None


# ============================================================================
# Splay-дерево
# ============================================================================


class SplayTree:
    """
    Splay-дерево (самобалансирующееся бинарное дерево поиска).

    После каждого обращения к узлу он поднимается к корню операцией splay.
    Амортизированная сложность всех операций: O(log n).

    Поддерживает:
    - insert(key)       — вставка
    - search(key)       — поиск
    - delete(key)       — удаление
    - split(key)        — разрезание на два дерева (< key и >= key)
    - merge(left, right) — слияние двух деревьев
    - inorder()         — симметричный обход (для отладки)
    """

    def __init__(self) -> None:
        self.root: SplayNode | None = None

    # -------------------------------------------------------------------------
    # Внутренние операции: rotate и splay
    # -------------------------------------------------------------------------

    def _rotate(self, x: SplayNode) -> None:
        """
        Поворот узла x вверх на одну позицию.
        Направление поворота определяется тем, является ли x левым или правым ребёнком.
        """
        p = x.parent
        g = p.parent

        if x == p.left:
            # Правый поворот: x поднимается, p становится правым ребёнком x
            p.left = x.right
            if x.right is not None:
                x.right.parent = p
            x.right = p
        else:
            # Левый поворот: x поднимается, p становится левым ребёнком x
            p.right = x.left
            if x.left is not None:
                x.left.parent = p
            x.left = p

        p.parent = x
        x.parent = g

        if g is None:
            self.root = x
        elif p == g.left:
            g.left = x
        else:
            g.right = x

    def _splay(self, x: SplayNode) -> None:
        """
        Поднимает узел x к корню, применяя zig/zig-zig/zig-zag повороты.
        """
        while x.parent is not None:
            p = x.parent
            g = p.parent

            if g is None:
                # Zig: родитель — корень, один поворот
                self._rotate(x)
            elif (x == p.left) == (p == g.left):
                # Zig-Zig: x и p — дети одного направления
                # Сначала поворачиваем родителя, потом x
                self._rotate(p)
                self._rotate(x)
            else:
                # Zig-Zag: x и p — дети разного направления
                # Два поворота x
                self._rotate(x)
                self._rotate(x)

    def _find(self, key: int) -> SplayNode | None:
        """
        Ищет узел с ключом key.
        Если найден — поднимает его к корню и возвращает.
        Если не найден — поднимает последний посещённый узел и возвращает None.
        """
        if self.root is None:
            return None

        node = self.root
        last = None

        while node is not None:
            last = node
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                # Точное совпадение — поднимаем к корню
                self._splay(node)
                return node

        # Ключ не найден — поднимаем последний посещённый узел
        # (это важно для корректной работы split)
        if last is not None:
            self._splay(last)
        return None

    # -------------------------------------------------------------------------
    # Основные операции
    # -------------------------------------------------------------------------

    def insert(self, key: int) -> None:
        """
        Вставляет ключ key в дерево.
        Если ключ уже существует — ничего не делает (поднимает существующий узел).
        """
        if self.root is None:
            self.root = SplayNode(key)
            return

        # Ищем место для вставки, запоминая последнего предка
        node = self.root
        parent: SplayNode | None = None

        while node is not None:
            parent = node
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                # Ключ уже есть — просто поднимаем его
                self._splay(node)
                return

        new_node = SplayNode(key)
        new_node.parent = parent

        if parent is not None:
            if key < parent.key:
                parent.left = new_node
            else:
                parent.right = new_node

        # Поднимаем новый узел к корню
        self._splay(new_node)

    def search(self, key: int) -> bool:
        """
        Ищет ключ key в дереве.
        Возвращает True, если найден.
        Побочный эффект: найденный (или ближайший) узел поднимается к корню.
        """
        return self._find(key) is not None

    def delete(self, key: int) -> bool:
        """
        Удаляет ключ key из дерева.
        Возвращает True, если узел был удалён.
        """
        node = self._find(key)
        if node is None:
            return False

        # После _find узел уже в корне
        if node.left is None:
            self.root = node.right
            if self.root is not None:
                self.root.parent = None
        elif node.right is None:
            self.root = node.left
            if self.root is not None:
                self.root.parent = None
        else:
            # Оба ребёнка есть.
            # Находим максимальный элемент в левом поддереве,
            # поднимаем его к корню левого поддерева — у него не будет правого ребёнка.
            left_max = node.left
            while left_max.right is not None:
                left_max = left_max.right

            # Отсоединяем левое поддерево и работаем с ним
            left_subtree = node.left
            if left_subtree is not None:
                left_subtree.parent = None

            # Создаём временное дерево из левого поддерева и делаем splay
            temp_root = self.root
            self.root = left_subtree
            self._splay(left_max)

            # Теперь left_max — корень левого поддерева, правого ребёнка у него нет
            left_max.right = node.right
            if node.right is not None:
                node.right.parent = left_max

            self.root = left_max

        return True

    # -------------------------------------------------------------------------
    # Split и Merge
    # -------------------------------------------------------------------------

    def split(self, key: int) -> tuple[SplayTree, SplayTree]:
        """
        Разбивает дерево на два:
          - left:  все ключи < key
          - right: все ключи >= key

        Возвращает пару (left_tree, right_tree).
        Исходное дерево после вызова становится пустым.
        """
        left_tree = SplayTree()
        right_tree = SplayTree()

        if self.root is None:
            return left_tree, right_tree

        # Находим ключ (или ближайший) и поднимаем к корню
        self._find(key)

        root = self.root
        assert root is not None

        if root.key < key:
            # Корень и всё его левое поддерево — в left
            # Правое поддерево корня — в right
            left_tree.root = root
            right_tree.root = root.right

            root.right = None
            if right_tree.root is not None:
                right_tree.root.parent = None
        else:
            # Корень и всё его правое поддерево — в right
            # Левое поддерево корня — в left
            right_tree.root = root
            left_tree.root = root.left

            root.left = None
            if left_tree.root is not None:
                left_tree.root.parent = None

        # Исходное дерево опустошаем
        self.root = None

        return left_tree, right_tree

    @staticmethod
    def merge(left: SplayTree, right: SplayTree) -> SplayTree:
        """
        Сливает два дерева в одно.
        Требование: все ключи в left < все ключи в right.

        Возвращает новое дерево. Исходные деревья left и right становятся пустыми.
        """
        result = SplayTree()

        if left.root is None:
            result.root = right.root
            right.root = None
            return result

        if right.root is None:
            result.root = left.root
            left.root = None
            return result

        # Находим максимальный элемент в left
        node = left.root
        while node.right is not None:
            node = node.right

        # Поднимаем максимум к корню left-дерева
        left._splay(node)

        # Теперь у node (корня left) нет правого ребёнка —
        # присоединяем right как правое поддерево
        node.right = right.root
        if right.root is not None:
            right.root.parent = node

        result.root = left.root

        # Опустошаем исходные деревья
        left.root = None
        right.root = None

        return result

    # -------------------------------------------------------------------------
    # Утилиты
    # -------------------------------------------------------------------------

    def inorder(self) -> list[int]:
        """Симметричный обход дерева (возвращает отсортированный список ключей)."""
        result: list[int] = []

        def _dfs(node: SplayNode | None) -> None:
            if node is None:
                return
            _dfs(node.left)
            result.append(node.key)
            _dfs(node.right)

        _dfs(self.root)
        return result

    def __iter__(self) -> Iterator[int]:
        """Позволяет итерироваться по дереву в отсортированном порядке."""
        return iter(self.inorder())

    def __len__(self) -> int:
        """Возвращает количество элементов в дереве."""
        return len(self.inorder())

    def __repr__(self) -> str:
        return f"SplayTree({self.inorder()})"


# ============================================================================
# Тесты
# ============================================================================


def run_tests() -> None:
    print("=" * 70)
    print("ТЕСТИРОВАНИЕ SPLAY TREE (полная версия)")
    print("=" * 70)

    passed = 0
    total = 0

    # -------------------------------------------------------------------------
    # 1. Базовые операции: insert, search, delete
    # -------------------------------------------------------------------------
    print("\n📌 1. Базовые операции:")
    tree = SplayTree()
    for key in [10, 20, 30, 40, 50, 25]:
        tree.insert(key)

    total += 1
    if tree.inorder() == [10, 20, 25, 30, 40, 50]:
        print(f"   ✅ inorder: {tree.inorder()}")
        passed += 1
    else:
        print(
            f"   ❌ inorder: ожидалось [10, 20, 25, 30, 40, 50], получено {tree.inorder()}"
        )

    total += 1
    if tree.search(25) and not tree.search(100):
        print(f"   ✅ search: 25 найден, 100 не найден")
        passed += 1
    else:
        print(f"   ❌ search")

    total += 1
    tree.delete(25)
    if not tree.search(25) and tree.inorder() == [10, 20, 30, 40, 50]:
        print(f"   ✅ delete(25): {tree.inorder()}")
        passed += 1
    else:
        print(f"   ❌ delete(25): {tree.inorder()}")

    # -------------------------------------------------------------------------
    # 2. Splay-эффект: после поиска узел становится корнем
    # -------------------------------------------------------------------------
    print("\n📌 2. Splay-эффект:")
    tree2 = SplayTree()
    for i in range(1, 11):
        tree2.insert(i)

    total += 1
    tree2.search(3)
    if tree2.root is not None and tree2.root.key == 3:
        print(f"   ✅ после search(3) корень = {tree2.root.key}")
        passed += 1
    else:
        print(f"   ❌ после search(3) корень = {tree2.root}")

    # -------------------------------------------------------------------------
    # 3. Split
    # -------------------------------------------------------------------------
    print("\n📌 3. Split:")
    tree3 = SplayTree()
    for key in [1, 3, 5, 7, 9, 11, 13]:
        tree3.insert(key)

    left, right = tree3.split(7)

    total += 1
    if left.inorder() == [1, 3, 5] and right.inorder() == [7, 9, 11, 13]:
        print(f"   ✅ split(7): left={left.inorder()}, right={right.inorder()}")
        passed += 1
    else:
        print(f"   ❌ split(7): left={left.inorder()}, right={right.inorder()}")

    total += 1
    if tree3.root is None:
        print(f"   ✅ исходное дерево пусто после split")
        passed += 1
    else:
        print(f"   ❌ исходное дерево не пусто")

    # -------------------------------------------------------------------------
    # 4. Merge
    # -------------------------------------------------------------------------
    print("\n📌 4. Merge:")
    t_left = SplayTree()
    for key in [2, 4, 6]:
        t_left.insert(key)

    t_right = SplayTree()
    for key in [8, 10, 12]:
        t_right.insert(key)

    merged = SplayTree.merge(t_left, t_right)

    total += 1
    if merged.inorder() == [2, 4, 6, 8, 10, 12]:
        print(f"   ✅ merge: {merged.inorder()}")
        passed += 1
    else:
        print(f"   ❌ merge: {merged.inorder()}")

    total += 1
    if t_left.root is None and t_right.root is None:
        print(f"   ✅ исходные деревья пусты после merge")
        passed += 1
    else:
        print(f"   ❌ исходные деревья не пусты")

    # -------------------------------------------------------------------------
    # 5. Split + Merge = тождественная операция
    # -------------------------------------------------------------------------
    print("\n📌 5. Split + Merge ( round-trip ):")
    tree4 = SplayTree()
    for key in [5, 2, 8, 1, 3, 7, 9]:
        tree4.insert(key)

    original = tree4.inorder()
    l, r = tree4.split(5)
    restored = SplayTree.merge(l, r)

    total += 1
    if restored.inorder() == original:
        print(f"   ✅ round-trip: {restored.inorder()} == {original}")
        passed += 1
    else:
        print(f"   ❌ round-trip: {restored.inorder()} != {original}")

    # -------------------------------------------------------------------------
    # 6. Краевые случаи split/merge
    # -------------------------------------------------------------------------
    print("\n📌 6. Краевые случаи:")

    # Split пустого дерева
    empty = SplayTree()
    l, r = empty.split(5)
    total += 1
    if l.root is None and r.root is None:
        print(f"   ✅ split пустого дерева")
        passed += 1
    else:
        print(f"   ❌ split пустого дерева")

    # Merge с пустым деревом
    t = SplayTree()
    t.insert(42)
    empty2 = SplayTree()
    m1 = SplayTree.merge(empty2, t)
    total += 1
    if m1.inorder() == [42] and t.root is None:
        print(f"   ✅ merge(пустое, непустое): {m1.inorder()}")
        passed += 1
    else:
        print(f"   ❌ merge(пустое, непустое)")

    m2 = SplayTree.merge(m1, empty2)
    total += 1
    if m2.inorder() == [42]:
        print(f"   ✅ merge(непустое, пустое): {m2.inorder()}")
        passed += 1
    else:
        print(f"   ❌ merge(непустое, пустое)")

    # -------------------------------------------------------------------------
    # 7. Стресс-тест split/merge
    # -------------------------------------------------------------------------
    print("\n📌 7. Стресс-тест split/merge:")
    import random

    random.seed(42)

    stress_ok = True
    for trial in range(100):
        n = random.randint(5, 50)
        keys = random.sample(range(1, 1000), n)
        keys.sort()

        tree_s = SplayTree()
        for k in keys:
            tree_s.insert(k)

        # Разрезаем в случайной точке
        split_key = keys[random.randint(0, n - 1)]
        l, r = tree_s.split(split_key)

        expected_left = [k for k in keys if k < split_key]
        expected_right = [k for k in keys if k >= split_key]

        if l.inorder() != expected_left or r.inorder() != expected_right:
            stress_ok = False
            print(f"   ❌ trial {trial}: split некорректен")
            break

        # Сливаем обратно
        merged = SplayTree.merge(l, r)
        if merged.inorder() != keys:
            stress_ok = False
            print(f"   ❌ trial {trial}: merge некорректен")
            break

    total += 1
    if stress_ok:
        print(f"   ✅ стресс-тест пройден (100 trials)")
        passed += 1
    else:
        print(f"   ❌ стресс-тест провален")

    # -------------------------------------------------------------------------
    # Итог
    # -------------------------------------------------------------------------
    print("\n" + "=" * 70)
    print(f"🏁 ИТОГ: {passed} / {total} тестов пройдено")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()
