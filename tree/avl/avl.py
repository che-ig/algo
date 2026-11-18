from typing import Any, Generic, Iterator, Protocol, TypeVar


# Протокол для типизации ключей, которые можно сравнивать
class Comparable(Protocol):
    """Протокол для типизации ключей, которые можно сравнивать между собой.

    Любой тип, реализующий этот протокол (например, int, str, float),
    может использоваться в качестве ключа в AVL-дереве.
    """

    def __lt__(self, other: Any) -> bool:
        """Метод 'меньше' (<). Используется для определения направления спуска по дереву.

        Args:
            other: Объект, с которым производится сравнение.

        Returns:
            True, если self строго меньше other, иначе False.
        """
        ...

    def __gt__(self, other: Any) -> bool:
        """Метод 'больше' (>). Обеспечивает полную поддержку операторов сравнения.

        Args:
            other: Объект, с которым производится сравнение.

        Returns:
            True, если self строго больше other, иначе False.
        """
        ...

    def __eq__(self, other: Any) -> bool:
        """Метод 'равно' (==). Используется для проверки совпадения ключей при поиске и обновлении.

        Args:
            other: Объект, с которым производится сравнение.

        Returns:
            True, если self равен other, иначе False.
        """
        ...


# Обобщенные типы для ключа (K) и значения (V)
K = TypeVar("K", bound=Comparable)
V = TypeVar("V")


class AVLNode(Generic[K, V]):
    """Узел AVL-дерева.

    Хранит ключ, значение, ссылки на левое и правое поддерево,
    а также высоту узла для поддержания баланса.

    Attributes:
        key: Ключ узла, должен поддерживать сравнение (протокол Comparable).
        value: Значение, ассоциированное с ключом.
        left: Ссылка на левый дочерний узел или None.
        right: Ссылка на правый дочерний узел или None.
        height: Высота поддерева, корнем которого является данный узел.
    """

    # Использование __slots__ для экономии памяти при большом количестве узлов
    __slots__ = ("key", "value", "left", "right", "height")

    def __init__(self, key: K, value: V) -> None:
        """Инициализирует новый узел AVL-дерева.

        Args:
            key: Ключ узла. Должен поддерживать операторы сравнения.
            value: Значение, ассоциированное с ключом.
        """
        self.key: K = key
        self.value: V = value
        self.left: AVLNode[K, V] | None = None
        self.right: AVLNode[K, V] | None = None
        self.height: int = 1  # Новый узел всегда имеет высоту 1


class AVLTree(Generic[K, V]):
    """Самобалансирующееся AVL-дерево.

    Гарантирует, что разница высот левого и правого поддеревьев любого узла
    не превышает 1, что обеспечивает сложность O(log n) для основных операций.
    """

    def __init__(self) -> None:
        """Инициализирует пустое AVL-дерево."""
        self._root: AVLNode[K, V] | None = None

    # ==================== ВСПОМОГАТЕЛЬНЫЕ МЕТОДЫ ====================

    def _height(self, node: AVLNode[K, V] | None) -> int:
        """Возвращает высоту узла или 0, если узел отсутствует.

        Args:
            node: Узел дерева или None (для пустого поддерева).

        Returns:
            Высота узла (целое число >= 0). Для None возвращает 0.
        """
        return node.height if node else 0

    def _balance_factor(self, node: AVLNode[K, V]) -> int:
        """Вычисляет коэффициент балансировки узла.

        Коэффициент балансировки = высота левого поддерева - высота правого.
        Допустимые значения: -1, 0, 1. Значения вне этого диапазона
        сигнализируют о необходимости поворота.

        Args:
            node: Узел, для которого вычисляется коэффициент балансировки.

        Returns:
            Разность высот левого и правого поддеревьев.
        """
        return self._height(node.left) - self._height(node.right)

    def _update_height(self, node: AVLNode[K, V]) -> None:
        """Обновляет высоту узла на основе высот его детей.

        Формула: height = 1 + max(height(left), height(right)).

        Args:
            node: Узел, высоту которого необходимо пересчитать.
        """
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    # ==================== ПОВОРОТЫ (БАЛАНСИРОВКА) ====================

    def _right_rotate(self, y: AVLNode[K, V]) -> AVLNode[K, V]:
        """Выполняет правый малый поворот (устраняет дисбаланс типа LL).

        Структура до и после поворота:
              y                               x
             / \                             / \
            x   T3     Right Rotate        T1   y
           / \       - - - - - - - >           / \
         T1   T2                             T2   T3

        Args:
            y: Узел, находящийся в состоянии дисбаланса (корень поддерева).

        Returns:
            Новый корень поддерева после выполнения поворота (бывший левый ребёнок y).
        """
        x = y.left
        t2 = x.right

        # Выполняем поворот
        x.right = y
        y.left = t2

        # Обновляем высоты (сначала нижний узел y, потом верхний x)
        self._update_height(y)
        self._update_height(x)

        return x  # Новый корень поддерева

    def _left_rotate(self, y: AVLNode[K, V]) -> AVLNode[K, V]:
        """Выполняет левый малый поворот (устраняет дисбаланс типа RR).

        Структура до и после поворота:
            y                                x
           / \                              / \
          T1  x      Left Rotate           y   T3
             / \   - - - - - - - >        / \
            T2 T3                       T1  T2

        Args:
            y: Узел, находящийся в состоянии дисбаланса (корень поддерева).

        Returns:
            Новый корень поддерева после выполнения поворота (бывший правый ребёнок y).
        """
        x = y.right
        t2 = x.left

        # Выполняем поворот
        x.left = y
        y.right = t2

        # Обновляем высоты
        self._update_height(y)
        self._update_height(x)

        return x  # Новый корень поддерева

    def _balance(self, node: AVLNode[K, V]) -> AVLNode[K, V]:
        """Проверяет коэффициент балансировки и применяет необходимые повороты.

        Обрабатывает все 4 случая дисбаланса:
          - LL (balance > 1, left.balance >= 0)  -> правый поворот
          - LR (balance > 1, left.balance < 0)   -> левый + правый повороты
          - RR (balance < -1, right.balance <= 0)-> левый поворот
          - RL (balance < -1, right.balance > 0) -> правый + левый повороты

        Args:
            node: Узел, который необходимо сбалансировать.

        Returns:
            Новый корень сбалансированного поддерева. Если баланс уже в норме,
            возвращается сам узел без изменений.
        """
        self._update_height(node)
        balance = self._balance_factor(node)

        # Случай LL (Левый-Левый)
        # LL (Left-Left): balance > 1, left.balance >= 0
        # Ситуация: Узел y перевешен влево, его левый ребёнок x также перевешен влево (или сбалансирован).
        # Решение: Один правый поворот вокруг y.
        #
        #         y                                  x
        #        / \                                / \
        #       x   T3         Right Rotate(y)     T1  y
        #      / \          - - - - - - - - >         / \
        #    T1   T2                                 T2  T3
        #
        # Что происходит:
        # - x поднимается на место y
        # - y становится правым ребёнком x
        # - T2 (правое поддерево x) становится левым поддеревом y
        if balance > 1 and self._balance_factor(node.left) >= 0:
            return self._right_rotate(node)

        # Случай LR (Левый-Правый)
        # LR (Left-Right): balance > 1, left.balance < 0
        # Ситуация: Узел y перевешен влево, его левый ребёнок x перевешен вправо. Внук z — правый ребёнок x.
        # Решение: Сначала левый поворот вокруг x, затем правый поворот вокруг y.
        #
        #         y                               y                              z
        #        / \                             / \                           /   \
        #       x   T4     Left Rotate(x)       z   T4     Right Rotate(y)    y      x
        #      / \        - - - - - - - - >    / \      - - - - - - - - >    / \    / \
        #    T1   z                           x   T3                        T1  T2 T3  T4
        #        / \                         / \
        #      T2   T3                     T1   T2
        #
        # Что происходит:
        # - Шаг 1 (левый поворот вокруг x): z поднимается, x становится левым ребёнком z, T2 становится правым поддеревом x
        # - Шаг 2 (правый поворот вокруг y): z поднимается на место y, y становится левым ребёнком z, T3 становится левым поддеревом y
        if balance > 1 and self._balance_factor(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # Случай RR (Правый-Правый)
        # RR (Right-Right): balance < -1, right.balance <= 0
        # Ситуация: Узел y перевешен вправо, его правый ребёнок x также перевешен вправо (или сбалансирован).
        # Решение: Один левый поворот вокруг y.
        #
        #         y                                  x
        #        / \                                / \
        #      T1   x         Left Rotate(y)       y   T3
        #          / \       - - - - - - - - >    / \
        #        T2   T3                        T1   T2
        #
        # Что происходит:
        # - x поднимается на место y
        # - y становится левым ребёнком x
        # - T2 (левое поддерево x) становится правым поддеревом y
        if balance < -1 and self._balance_factor(node.right) <= 0:
            return self._left_rotate(node)

        # Случай RL (Правый-Левый)
        # RL (Right-Left): balance < -1, right.balance > 0
        # Ситуация: Узел y перевешен вправо, его правый ребёнок x перевешен влево. Внук z — левый ребёнок x.
        # Решение: Сначала правый поворот вокруг x, затем левый поворот вокруг y.
        #
        #         y                               y                               z
        #        / \                             / \                           /     \
        #      T1   x       Right Rotate(x)    T1   z       Left Rotate(y)    y       x
        #          / \     - - - - - - - - >       / \    - - - - - - - - >  / \     / \
        #         z   T4                         T2   x                     T1  T2  T3  T4
        #        / \                                 / \
        #      T2   T3                             T3   T4
        #
        # Что происходит:
        # - Шаг 1 (правый поворот вокруг x): z поднимается, x становится правым ребёнком z, T3 становится левым поддеревом x
        # - Шаг 2 (левый поворот вокруг y): z поднимается на место y, y становится левым ребёнком z, T2 становится правым поддеревом y
        if balance < -1 and self._balance_factor(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node  # Если баланс в норме, возвращаем узел без изменений

    # ==================== ОСНОВНЫЕ ОПЕРАЦИИ ====================

    def _insert(self, node: AVLNode[K, V] | None, key: K, value: V) -> AVLNode[K, V]:
        """Рекурсивная вставка узла с последующей балансировкой.

        Сначала выполняет стандартную вставку в BST, затем при возврате
        из рекурсии обновляет высоты и выполняет балансировку.

        Args:
            node: Текущий корень поддерева (или None для пустого).
            key: Ключ вставляемого элемента.
            value: Значение, ассоциированное с ключом.

        Returns:
            Новый корень поддерева после вставки и балансировки.
        """
        # 1. Стандартная вставка в BST
        if not node:
            return AVLNode(key, value)

        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            # Если ключ уже существует, просто обновляем значение
            node.value = value
            return node

        # 2. Балансировка при возврате из рекурсии
        return self._balance(node)

    def insert(self, key: K, value: V) -> None:
        """Публичный метод для добавления пары ключ-значение в дерево.

        Если ключ уже существует, его значение будет обновлено.
        После вставки дерево автоматически балансируется.

        Args:
            key: Ключ вставляемого элемента.
            value: Значение, ассоциированное с ключом.
        """
        self._root = self._insert(self._root, key, value)

    def _get_min_value_node(self, node: AVLNode[K, V]) -> AVLNode[K, V]:
        """Находит узел с минимальным ключом в поддереве (используется при удалении).

        Двигается по левым рёбрам до тех пор, пока не достигнет листа.

        Args:
            node: Корень поддерева, в котором ищется минимум. Не может быть None.

        Returns:
            Узел с минимальным ключом в заданном поддереве.
        """
        current = node
        while current.left:
            current = current.left
        return current

    def _delete(self, node: AVLNode[K, V] | None, key: K) -> AVLNode[K, V] | None:
        """Рекурсивное удаление узла по ключу с последующей балансировкой.

        Обрабатывает три случая:
          1. Узел без потомков — просто удаляется.
          2. Узел с одним потомком — заменяется своим потомком.
          3. Узел с двумя потомками — заменяется inorder-преемником
             (минимальным узлом правого поддерева), после чего преемник удаляется.

        Args:
            node: Текущий корень поддерева (или None).
            key: Ключ удаляемого элемента.

        Returns:
            Новый корень поддерева после удаления и балансировки,
            или None, если поддерево стало пустым.
        """
        if not node:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Узел найден. Удаляем его.

            # Узел с одним потомком или без них
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            # Узел с двумя потомками:
            # Находим inorder-преемника (минимальный узел в правом поддереве)
            temp = self._get_min_value_node(node.right)

            # Копируем данные преемника в текущий узел
            node.key = temp.key
            node.value = temp.value

            # Удаляем преемника из правого поддерева
            node.right = self._delete(node.right, temp.key)

        # Если после удаления дерево стало пустым
        if not node:
            return node

        # Балансировка при возврате из рекурсии
        return self._balance(node)

    def delete(self, key: K) -> None:
        """Публичный метод для удаления узла по ключу.

        Если ключ не найден, дерево остаётся неизменным.
        После удаления дерево автоматически балансируется.

        Args:
            key: Ключ удаляемого элемента.
        """
        self._root = self._delete(self._root, key)

    def search(self, key: K) -> V | None:
        """Ищет значение по ключу итеративным спуском по дереву.

        Сложность: O(log n) благодаря сбалансированности AVL-дерева.

        Args:
            key: Искомый ключ.

        Returns:
            Значение, ассоциированное с ключом, или None, если ключ не найден.
        """
        current = self._root
        while current:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current.value
        return None

    # ==================== ИТЕРАЦИЯ И УТИЛИТЫ ====================

    def _inorder_iter(self, node: AVLNode[K, V] | None) -> Iterator[tuple[K, V]]:
        """Рекурсивный генератор для симметричного (in-order) обхода дерева.

        Обход выполняется в порядке: левое поддерево -> корень -> правое поддерево,
        что гарантирует выдачу пар (ключ, значение) в отсортированном по ключу порядке.

        Args:
            node: Текущий корень поддерева (или None).

        Yields:
            Кортежи (key, value) в порядке возрастания ключей.
        """
        if node:
            yield from self._inorder_iter(node.left)
            yield (node.key, node.value)
            yield from self._inorder_iter(node.right)

    def items(self) -> Iterator[tuple[K, V]]:
        """Возвращает итератор по всем парам (ключ, значение) в отсортированном порядке.

        Returns:
            Генератор, выдающий пары (key, value), отсортированные по возрастанию ключа.
        """
        return self._inorder_iter(self._root)

    def __contains__(self, key: K) -> bool:
        """Позволяет использовать оператор `in` для проверки наличия ключа.

        Пример:
            if 42 in tree: ...

        Args:
            key: Проверяемый ключ.

        Returns:
            True, если ключ присутствует в дереве, иначе False.
        """
        return self.search(key) is not None

    def __len__(self) -> int:
        """Возвращает количество элементов в дереве.

        Внимание: метод выполняет полный обход дерева, поэтому имеет сложность O(n).
        Для частых проверок размера рекомендуется хранить счётчик отдельно.

        Returns:
            Целое число — количество пар (ключ, значение) в дереве.
        """
        return sum(1 for _ in self.items())


if __name__ == "__main__":
    # Создаем дерево, где ключи - int, значения - str
    tree: AVLTree[int, str] = AVLTree()

    # Вставка элементов (дерево будет балансироваться автоматически)
    data = [
        (10, "A"),
        (20, "B"),
        (30, "C"),
        (40, "D"),
        (50, "E"),
        (25, "F"),
        (5, "G"),
        (3, "H"),
    ]

    for key, value in data:
        tree.insert(key, value)

    print("Дерево в отсортированном порядке (In-order):")
    for k, v in tree.items():
        print(f"Key: {k}, Value: {v}")
    # Ожидаемый вывод: 3, 5, 10, 20, 25, 30, 40, 50

    print("\nПроверка баланса (высоты поддеревьев):")
    # В AVL дереве высота всегда будет близка к log2(N)
    # Для 8 элементов идеальная высота ~ 3 или 4.

    print("\nПоиск элемента:")
    print(f"Значение для ключа 25: {tree.search(25)}")  # Выведет: F
    print(f"Значение для ключа 99: {tree.search(99)}")  # Выведет: None

    print("\nИспользование оператора 'in':")
    print(f"Есть ли ключ 20? {20 in tree}")  # Выведет: True
    print(f"Есть ли ключ 99? {99 in tree}")  # Выведет: False

    print("\nУдаление элемента:")
    tree.delete(20)
    print(f"Значение для ключа 20 после удаления: {tree.search(20)}")  # Выведет: None

    print("\nОбновление значения существующего ключа:")
    tree.insert(10, "Updated_A")
    print(f"Новое значение для ключа 10: {tree.search(10)}")  # Выведет: Updated_A
