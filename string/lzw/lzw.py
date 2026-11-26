"""
Алгоритм сжатия LZW (Lempel-Ziv-Welch)

Реализация работает с байтовыми последовательностями (bytes),
что является стандартом для реальных систем сжатия.
"""


def lzw_compress(data: bytes) -> list[int]:
    """
    Сжимает байтовую последовательность с помощью алгоритма LZW.

    Args:
        data: Исходные данные в виде байтов.

    Returns:
        Список целых чисел (кодов), представляющих сжатые данные.
    """
    # Инициализация словаря всеми возможными одиночными байтами (0-255)
    dict_size = 256
    dictionary: dict[bytes, int] = {bytes([i]): i for i in range(dict_size)}

    current_string = b""
    compressed_data: list[int] = []

    for byte in data:
        # Преобразуем одиночный байт в bytes-объект для конкатенации
        next_byte = bytes([byte])
        combined = current_string + next_byte

        if combined in dictionary:
            # Если комбинация уже есть, просто расширяем текущую строку
            current_string = combined
        else:
            # Выдаем код для известной части строки
            compressed_data.append(dictionary[current_string])
            # Добавляем новую комбинацию в словарь
            dictionary[combined] = dict_size
            dict_size += 1
            # Начинаем новую строку с текущего байта
            current_string = next_byte

    # Не забываем выдать код для последней накопленной строки
    if current_string:
        compressed_data.append(dictionary[current_string])

    return compressed_data


def lzw_decompress(compressed_data: list[int]) -> bytes:
    """
    Восстанавливает исходную байтовую последовательность из LZW-кодов.

    Args:
        compressed_data: Список целых чисел (кодов), полученных при сжатии.

    Returns:
        Исходные данные в виде байтов.
    """
    if not compressed_data:
        return b""

    # Инициализация словаря (должна точно совпадать с кодировщиком)
    dict_size = 256
    dictionary: dict[int, bytes] = {i: bytes([i]) for i in range(dict_size)}

    # Первый код всегда корректен и находится в базовом словаре
    first_code = compressed_data[0]
    previous_output = dictionary[first_code]
    result: list[bytes] = [previous_output]

    for code in compressed_data[1:]:
        if code in dictionary:
            # Стандартный случай: код уже есть в словаре
            entry = dictionary[code]
        else:
            # EDGE CASE: код еще не добавлен в словарь декодера.
            # Это возможно только если код равен строке, которую мы
            # собираемся добавить прямо сейчас:
            # previous_output + first_char(previous_output)
            entry = previous_output + bytes([previous_output[0]])

        result.append(entry)

        # Добавляем новую запись в словарь:
        # предыдущий вывод + первый символ текущего вывода
        dictionary[dict_size] = previous_output + bytes([entry[0]])
        dict_size += 1

        # Текущий вывод становится предыдущим для следующей итерации
        previous_output = entry

    return b"".join(result)


def main() -> None:
    """Демонстрация работы алгоритма LZW."""

    # Пример 1: Классическая строка с Edge Case
    original_text = "ABABABAB"
    data = original_text.encode("utf-8")

    print(f"Исходные данные: {original_text}")
    print(f"Размер оригинала: {len(data)} байт")

    # Сжатие
    compressed = lzw_compress(data)
    print(f"\nСжатые коды: {compressed}")
    print(f"Количество кодов: {len(compressed)} (вместо {len(data)} байт)")

    # Распаковка
    decompressed = lzw_decompress(compressed)
    print(f"Восстановленные данные: {decompressed.decode('utf-8')}")
    print(f"Успех: {data == decompressed}")

    # Пример 2: Данные, где LZW показывает максимальную эффективность
    print("\n" + "=" * 50)
    pattern = b"TOBEORNOTTOBEORTOBEORNOT"
    compressed_pattern = lzw_compress(pattern)
    decompressed_pattern = lzw_decompress(compressed_pattern)

    print(f"Оригинал: {len(pattern)} байт")
    print(f"Сжатое: {len(compressed_pattern)} кодов")
    print(f"Степень сжатия: {(1 - len(compressed_pattern) / len(pattern)) * 100:.1f}%")
    print(f"Целостность данных: {pattern == decompressed_pattern}")


if __name__ == "__main__":
    main()
