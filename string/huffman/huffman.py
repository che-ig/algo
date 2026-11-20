"""
Алгоритм кодирования Хаффмана (Huffman Coding)

Это статистический алгоритм сжатия без потерь, который назначает более короткие
бинарные коды частым символам и более длинные - редким символам.
"""

from collections import Counter
from dataclasses import dataclass
from heapq import heappop, heappush


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

    Алгоритм:
    1. Создаем листовой узел для каждого символа с его частотой
    2. Помещаем все узлы в очередь с приоритетом (min-heap)
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

    Time Complexity: O(K log K), где K - количество уникальных символов
    """
    if not freq_map:
        return None

    # Создаем очередь с приоритетом и заполняем её листовыми узлами
    priority_queue: list[HuffmanNode] = []

    for char, freq in freq_map.items():
        node = HuffmanNode(char=char, freq=freq)
        heappush(priority_queue, node)

    # Особый случай: если в тексте только один уникальный символ
    if len(priority_queue) == 1:
        # Создаем фиктивный узел, чтобы дерево не выродилось
        single_node = heappop(priority_queue)
        root = HuffmanNode(char=None, freq=single_node.freq)
        root.left = single_node
        return root

    # Строим дерево, объединяя узлы с наименьшей частотой
    while len(priority_queue) > 1:
        # Извлекаем два узла с минимальной частотой
        left_child: HuffmanNode = heappop(priority_queue)
        right_child: HuffmanNode = heappop(priority_queue)

        # Создаем новый внутренний узел
        # Сумма частот = общая частота обоих поддеревьев
        parent_freq: int = left_child.freq + right_child.freq
        parent_node = HuffmanNode(
            char=None,  # Внутренние узлы не содержат символов
            freq=parent_freq,
            left=left_child,
            right=right_child,
        )

        # Помещаем новый узел обратно в очередь
        heappush(priority_queue, parent_node)

    # Последний оставшийся узел - корень дерева
    return heappop(priority_queue)


def generate_codes(root: HuffmanNode | None) -> dict[str, str]:
    """
    Генерирует коды Хаффмана для каждого символа путем обхода дерева.

    Алгоритм:
    - Обходим дерево от корня к листьям (DFS)
    - При движении влево добавляем '0' к текущему коду
    - При движении вправо добавляем '1' к текущему коду
    - Когда достигаем листа, сохраняем накопленный код для этого символа

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

        # Если это листовой узел (содержит символ)
        if node.char is not None:
            # Особый случай: если код пустой (единственный символ в тексте)
            # Присваиваем ему код '0'
            codes[node.char] = current_code if current_code else "0"
            return

        # Рекурсивно обходим левое и правое поддеревья
        # Добавляем '0' для левого пути и '1' для правого
        traverse(node.left, current_code + "0")
        traverse(node.right, current_code + "1")

    traverse(root, "")
    return codes


def encode(text: str, codes: dict[str, str]) -> str:
    """
    Кодирует текст в бинарную строку используя коды Хаффмана.

    Args:
        text: Исходный текст для кодирования
        codes: Словарь кодов Хаффмана (символ -> бинарный код)

    Returns:
        Бинарная строка (последовательность '0' и '1')

    Example:
        >>> encode("abc", {"a": "0", "b": "10", "c": "11"})
        '01011'

    Time Complexity: O(N), где N - длина текста
    """
    encoded_bits: list[str] = []

    for char in text:
        if char not in codes:
            raise ValueError(f"Символ '{char}' не найден в таблице кодов")
        encoded_bits.append(codes[char])

    return "".join(encoded_bits)


def decode(encoded_text: str, root: HuffmanNode | None) -> str:
    """
    Декодирует бинарную строку обратно в текст, используя дерево Хаффмана.

    Алгоритм:
    - Начинаем с корня дерева
    - Читаем биты закодированной строки по одному
    - Если бит '0' - идем влево, если '1' - вправо
    - Когда достигаем листа, добавляем символ к результату
    - Возвращаемся к корню и продолжаем со следующего бита

    Args:
        encoded_text: Бинарная строка для декодирования
        root: Корень дерева Хаффмана

    Returns:
        Декодированный текст

    Time Complexity: O(N), где N - длина закодированной строки
    """
    if root is None:
        return ""

    decoded_chars: list[str] = []
    current_node: HuffmanNode = root

    for bit in encoded_text:
        # Двигаемся по дереву в зависимости от бита
        if bit == "0":
            current_node = current_node.left
        else:  # bit == '1'
            current_node = current_node.right

        if current_node is None:
            raise ValueError("Некорректная закодированная строка")

        # Если достигли листа, добавляем символ к результату
        if current_node.char is not None:
            decoded_chars.append(current_node.char)
            # Возвращаемся к корню для следующего символа
            current_node = root

    return "".join(decoded_chars)


def huffman_compress(text: str) -> tuple[str, dict[str, str], HuffmanNode | None]:
    """
    Полная функция сжатия текста алгоритмом Хаффмана.

    Args:
        text: Исходный текст для сжатия

    Returns:
        Кортеж из:
        - Закодированная бинарная строка
        - Таблица кодов (для передачи декодеру)
        - Корень дерева (для декодирования)

    Example:
        >>> encoded, codes, tree = huffman_compress("hello")
        >>> print(f"Оригинал: {len('hello') * 8} бит")
        >>> print(f"Сжато: {len(encoded)} бит")
    """
    # Шаг 1: Подсчитываем частоты символов
    freq_map: dict[str, int] = count_frequencies(text)

    # Шаг 2: Строим дерево Хаффмана
    tree_root: HuffmanNode | None = build_huffman_tree(freq_map)

    # Шаг 3: Генерируем коды для каждого символа
    codes: dict[str, str] = generate_codes(tree_root)

    # Шаг 4: Кодируем текст
    encoded_text: str = encode(text, codes)

    return encoded_text, codes, tree_root


def main() -> None:
    """Демонстрация работы алгоритма Хаффмана."""

    # Пример 1: Простая строка
    text = "hello world"
    print("=" * 60)
    print("Пример 1: Простая строка")
    print("=" * 60)
    print(f"Исходный текст: '{text}'")
    print(f"Длина оригинала: {len(text) * 8} бит (8 бит на символ)")

    # Сжимаем
    encoded, codes, tree = huffman_compress(text)

    print(f"\nТаблица кодов Хаффмана:")
    for char, code in sorted(codes.items(), key=lambda x: len(x[1])):
        print(f"  '{char}' -> {code}")

    print(f"\nЗакодированная строка: {encoded}")
    print(f"Длина сжатых данных: {len(encoded)} бит")

    # Вычисляем степень сжатия
    compression_ratio = (1 - len(encoded) / (len(text) * 8)) * 100
    print(f"Степень сжатия: {compression_ratio:.1f}%")

    # Декодируем обратно
    decoded = decode(encoded, tree)
    print(f"\nДекодированный текст: '{decoded}'")
    print(f"Успех: {decoded == text}")

    # Пример 2: Текст с повторяющимися символами
    print("\n" + "=" * 60)
    print("Пример 2: Текст с повторениями")
    print("=" * 60)
    text2 = "aaaaabbbbbccccddddeee"
    print(f"Исходный текст: '{text2}'")
    print(f"Длина оригинала: {len(text2) * 8} бит")

    encoded2, codes2, tree2 = huffman_compress(text2)

    print(f"\nТаблица кодов:")
    for char, code in sorted(codes2.items(), key=lambda x: len(x[1])):
        print(f"  '{char}' -> {code}")

    print(f"\nЗакодированная строка: {encoded2}")
    print(f"Длина сжатых данных: {len(encoded2)} бит")

    compression_ratio2 = (1 - len(encoded2) / (len(text2) * 8)) * 100
    print(f"Степень сжатия: {compression_ratio2:.1f}%")

    decoded2 = decode(encoded2, tree2)
    print(f"\nДекодированный текст: '{decoded2}'")
    print(f"Успех: {decoded2 == text2}")

    # Пример 3: Анализ частот
    print("\n" + "=" * 60)
    print("Пример 3: Анализ частот символов")
    print("=" * 60)
    text3 = "abracadabra"
    freq = count_frequencies(text3)
    print(f"Текст: '{text3}'")
    print(f"Частоты символов:")
    for char, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
        print(f"  '{char}': {count} ({count / len(text3) * 100:.1f}%)")


if __name__ == "__main__":
    main()
