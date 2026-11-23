"""
Алгоритм кодирования Хаффмана (Huffman Coding)

Оптимизированная версия с использованием метода Флойда (heapify)
для построения кучи за O(K) вместо O(K log K).
"""

from collections import Counter
from dataclasses import dataclass
from heapq import heapify, heappop, heappush


@dataclass
class HuffmanNode:
    """
    Узел бинарного дерева Хаффмана.

    Attributes:
        char: Символ (None для внутренних узлов)
        freq: Частота символа или сумма частот поддеревьев
        left: Левый дочерний узел
        right: Правый дочерний узел
    """

    char: str | None
    freq: int
    left: "HuffmanNode | None" = None
    right: "HuffmanNode | None" = None

    def __lt__(self, other: "HuffmanNode") -> bool:
        """
        Метод сравнения для работы с heapq (очередь с приоритетом).
        Узлы сравниваются по частоте.
        """
        return self.freq < other.freq


def count_frequencies(text: str) -> dict[str, int]:
    """
    Подсчитывает частоту каждого символа в тексте.

    Args:
        text: Входная строка для анализа

    Returns:
        Словарь, где ключ - символ, значение - его частота

    Example:
        >>> count_frequencies("aabbc")
        {'a': 2, 'b': 2, 'c': 1}
    """
    return dict(Counter(text))


def build_huffman_tree(freq_map: dict[str, int]) -> HuffmanNode | None:
    """
    Строит дерево Хаффмана на основе частот символов.

    Алгоритм (ОПТИМИЗИРОВАННАЯ ВЕРСИЯ):
    1. Создаем листовой узел для каждого символа с его частотой
    2. Строим кучу методом Флойда (heapify) за O(K)
       вместо последовательной вставки за O(K log K)
    3. Пока в очереди больше одного узла:
       - Извлекаем два узла с наименьшей частотой
       - Создаем новый внутренний узел с суммой их частот
       - Назначаем извлеченные узлы как дочерние
       - Помещаем новый узел обратно в очередь
    4. Оставшийся узел - корень дерева Хаффмана

    Args:
        freq_map: Словарь частот символов

    Returns:
        Корень дерева Хаффмана или None, если вход пустой

    Time Complexity:
        - Построение кучи: O(K) [метод Флойда]
        - Основной цикл: O(K log K) [K-1 итерация, каждая O(log K)]
        - Итого: O(K log K) — но с меньшей константой, чем раньше
    """
    if not freq_map:
        return None

    # ШАГ 1: Создаем список листовых узлов
    # Это обычный Python list, а не куча
    nodes: list[HuffmanNode] = [
        HuffmanNode(char=char, freq=freq) for char, freq in freq_map.items()
    ]

    # ШАГ 2: Применяем метод Флойда (heapify)
    # Преобразуем список в min-heap за O(K) операций
    # Это эффективнее, чем K раз вызывать heappush (O(K log K))
    heapify(nodes)

    # Особый случай: если в тексте только один уникальный символ
    if len(nodes) == 1:
        # Создаем фиктивный узел, чтобы дерево не выродилось
        single_node = heappop(nodes)
        root = HuffmanNode(char=None, freq=single_node.freq)
        root.left = single_node
        return root

    # ШАГ 3: Строим дерево, объединяя узлы с наименьшей частотой
    while len(nodes) > 1:
        # Извлекаем два узла с минимальной частотой
        # Каждая операция heappop занимает O(log K)
        left_child: HuffmanNode = heappop(nodes)
        right_child: HuffmanNode = heappop(nodes)

        # Создаем новый внутренний узел
        parent_freq: int = left_child.freq + right_child.freq
        parent_node = HuffmanNode(
            char=None,  # Внутренние узлы не содержат символов
            freq=parent_freq,
            left=left_child,
            right=right_child,
        )

        # Помещаем новый узел обратно в кучу
        # heappush поддерживает свойство кучи за O(log K)
        heappush(nodes, parent_node)

    # Последний оставшийся узел - корень дерева
    return heappop(nodes)


def generate_codes(root: HuffmanNode | None) -> dict[str, str]:
    """
    Генерирует коды Хаффмана для каждого символа путем обхода дерева.

    Args:
        root: Корень дерева Хаффмана

    Returns:
        Словарь, где ключ - символ, значение - его бинарный код

    Time Complexity: O(K), где K - количество уникальных символов
    """
    if root is None:
        return {}

    codes: dict[str, str] = {}

    def traverse(node: HuffmanNode | None, current_code: str) -> None:
        """Рекурсивный обход дерева для генерации кодов."""
        if node is None:
            return

        if node.char is not None:
            codes[node.char] = current_code if current_code else "0"
            return

        traverse(node.left, current_code + "0")
        traverse(node.right, current_code + "1")

    traverse(root, "")
    return codes


def encode(text: str, codes: dict[str, str]) -> str:
    """Кодирует текст в бинарную строку используя коды Хаффмана."""
    encoded_bits: list[str] = []
    for char in text:
        if char not in codes:
            raise ValueError(f"Символ '{char}' не найден в таблице кодов")
        encoded_bits.append(codes[char])
    return "".join(encoded_bits)


def decode(encoded_text: str, root: HuffmanNode | None) -> str:
    """Декодирует бинарную строку обратно в текст."""
    if root is None:
        return ""

    decoded_chars: list[str] = []
    current_node: HuffmanNode = root

    for bit in encoded_text:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node is None:
            raise ValueError("Некорректная закодированная строка")

        if current_node.char is not None:
            decoded_chars.append(current_node.char)
            current_node = root

    return "".join(decoded_chars)


def huffman_compress(text: str) -> tuple[str, dict[str, str], HuffmanNode | None]:
    """Полная функция сжатия текста алгоритмом Хаффмана."""
    freq_map: dict[str, int] = count_frequencies(text)
    tree_root: HuffmanNode | None = build_huffman_tree(freq_map)
    codes: dict[str, str] = generate_codes(tree_root)
    encoded_text: str = encode(text, codes)
    return encoded_text, codes, tree_root


def main() -> None:
    """Демонстрация работы алгоритма Хаффмана."""
    text = "hello world"
    print(f"Исходный текст: '{text}'")
    print(f"Длина оригинала: {len(text) * 8} бит")

    encoded, codes, tree = huffman_compress(text)

    print(f"\nТаблица кодов Хаффмана:")
    for char, code in sorted(codes.items(), key=lambda x: len(x[1])):
        print(f"  '{char}' -> {code}")

    print(f"\nЗакодированная строка: {encoded}")
    print(f"Длина сжатых данных: {len(encoded)} бит")

    compression_ratio = (1 - len(encoded) / (len(text) * 8)) * 100
    print(f"Степень сжатия: {compression_ratio:.1f}%")

    decoded = decode(encoded, tree)
    print(f"\nДекодированный текст: '{decoded}'")
    print(f"Успех: {decoded == text}")


if __name__ == "__main__":
    main()
