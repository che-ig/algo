"""
Алгоритм кодирования Хаффмана с двумя очередями (Two-Queue Approach)

Оптимизированная версия, работающая за O(K log K) в общем случае
или O(K) при малом алфавите (через counting sort).
"""

from collections import Counter, deque
from dataclasses import dataclass


@dataclass
class HuffmanNode:
    """Узел бинарного дерева Хаффмана."""

    char: str | None
    freq: int
    left: "HuffmanNode | None" = None
    right: "HuffmanNode | None" = None


def count_frequencies(text: str) -> dict[str, int]:
    """Подсчитывает частоту каждого символа."""
    return dict(Counter(text))


def build_huffman_tree_two_queues(freq_map: dict[str, int]) -> HuffmanNode | None:
    """
    Строит дерево Хаффмана используя две очереди.

    Алгоритм:
    1. Сортируем листья по частоте → Q1 (отсортированная очередь листьев)
    2. Q2 — пустая очередь для внутренних узлов
    3. На каждом шаге:
       - Смотрим на головы Q1 и Q2
       - Берём два узла с минимальной частотой
       - Создаём родителя и кладём в Q2
    4. Последний узел — корень дерева

    Ключевой инвариант: Q2 всегда отсортирована, потому что
    мы всегда объединяем минимальные элементы, и суммы неубывают.

    Args:
        freq_map: Словарь частот символов

    Returns:
        Корень дерева Хаффмана или None

    Time Complexity:
        - O(K log K) — из-за сортировки листьев
        - O(K) — если алфавит мал (можно использовать counting sort)
        - Основной цикл: O(K) — K-1 итераций по O(1)
    """
    if not freq_map:
        return None

    # ШАГ 1: Создаём отсортированную очередь листьев (Q1)
    # Сортируем по частоте — это единственная "дорогая" операция
    sorted_leaves = sorted(
        (HuffmanNode(char=char, freq=freq) for char, freq in freq_map.items()),
        key=lambda node: node.freq,
    )
    q1: deque[HuffmanNode] = deque(sorted_leaves)

    # ШАГ 2: Пустая очередь для внутренних узлов (Q2)
    q2: deque[HuffmanNode] = deque()

    # Особый случай: один уникальный символ
    if len(q1) == 1:
        single_node = q1.popleft()
        root = HuffmanNode(char=None, freq=single_node.freq)
        root.left = single_node
        return root

    # ШАГ 3: Вспомогательная функция для получения минимума из двух очередей
    def get_min() -> HuffmanNode:
        """
        Извлекает узел с минимальной частотой из голов Q1 и Q2.

        Сравниваем только головы двух очередей — O(1).
        """
        if not q1:
            return q2.popleft()
        if not q2:
            return q1.popleft()

        # Берём минимум из голов обеих очередей
        if q1[0].freq <= q2[0].freq:
            return q1.popleft()
        else:
            return q2.popleft()

    # ШАГ 4: Основной цикл — K-1 итераций
    # На каждой итерации объединяем два узла с минимальной частотой
    while len(q1) + len(q2) > 1:
        # Берём два минимума — каждый за O(1)
        left_child = get_min()
        right_child = get_min()

        # Создаём внутренний узел
        parent = HuffmanNode(
            char=None,
            freq=left_child.freq + right_child.freq,
            left=left_child,
            right=right_child,
        )

        # Кладём в Q2 — она остаётся отсортированной!
        q2.append(parent)

    return q2.popleft()


def generate_codes(root: HuffmanNode | None) -> dict[str, str]:
    """Генерирует коды Хаффмана путём DFS-обхода дерева."""
    if root is None:
        return {}

    codes: dict[str, str] = {}

    def traverse(node: HuffmanNode | None, current_code: str) -> None:
        if node is None:
            return
        if node.char is not None:
            codes[node.char] = current_code
            return
        traverse(node.left, current_code + "0")
        traverse(node.right, current_code + "1")

    traverse(root, "")
    return codes


def encode(text: str, codes: dict[str, str]) -> str:
    """Кодирует текст в бинарную строку."""
    return "".join(codes[char] for char in text)


def decode(encoded_text: str, root: HuffmanNode | None) -> str:
    """Декодирует бинарную строку обратно в текст."""
    if root is None:
        return ""

    decoded_chars: list[str] = []
    current_node: HuffmanNode = root

    for bit in encoded_text:
        current_node = current_node.left if bit == "0" else current_node.right
        if current_node is None:
            raise ValueError("Некорректная закодированная строка")
        if current_node.char is not None:
            decoded_chars.append(current_node.char)
            current_node = root

    return "".join(decoded_chars)


def huffman_compress_two_queues(
    text: str,
) -> tuple[str, dict[str, str], HuffmanNode | None]:
    """Полная функция сжатия с использованием двух очередей."""
    freq_map = count_frequencies(text)
    tree_root = build_huffman_tree_two_queues(freq_map)
    codes = generate_codes(tree_root)
    encoded_text = encode(text, codes)
    return encoded_text, codes, tree_root


def main() -> None:
    """Демонстрация работы алгоритма."""
    text = "hello world"
    print(f"Исходный текст: '{text}'")

    encoded, codes, tree = huffman_compress_two_queues(text)

    print(f"\nТаблица кодов:")
    for char, code in sorted(codes.items(), key=lambda x: len(x[1])):
        print(f"  '{char}' -> {code}")

    print(f"\nЗакодированная строка: {encoded}")
    print(f"Длина: {len(encoded)} бит (оригинал: {len(text) * 8} бит)")

    decoded = decode(encoded, tree)
    print(f"\nДекодированный текст: '{decoded}'")
    print(f"Успех: {decoded == text}")


if __name__ == "__main__":
    main()
