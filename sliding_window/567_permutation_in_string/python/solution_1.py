from collections import Counter


class SolutionCounter:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Проверяет, содержит ли s2 перестановку s1 как подстроку.
        Использует Counter для сравнения частот символов.

        Это более простое, но менее оптимальное решение по сравнению
        с подходом через скользящее окно с счётчиком matches.
        """
        # Если s1 длиннее s2, перестановка невозможна по определению
        if len(s1) > len(s2):
            return False

        # Считаем частоты символов в s1 один раз
        # Counter создаёт словарь вида {'a': 1, 'b': 1} для строки "ab"
        s1_count = Counter(s1)

        # Длина окна равна длине s1, так как перестановка имеет ту же длину
        window_size = len(s1)

        # Скользим окном фиксированного размера по строке s2
        # range(len(s2) - window_size + 1) гарантирует, что окно не выйдет за границы
        for i in range(len(s2) - window_size + 1):
            # Вырезаем подстроку длины window_size, начиная с позиции i
            window = s2[i : i + window_size]

            # Считаем частоты символов в текущем окне
            # и сравниваем с частотами в s1
            if Counter(window) == s1_count:
                # Если частоты совпали — нашли перестановку
                return True

        # Если прошли по всем окнам и не нашли совпадение — перестановки нет
        return False


def main_counter():
    """Тест-кейсы для альтернативного решения с Counter."""
    solution = SolutionCounter()

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ АЛЬТЕРНАТИВНОГО РЕШЕНИЯ (Counter)")
    print("=" * 60)

    # Тест 1: Стандартный случай из примера LeetCode
    s1 = "ab"
    s2 = "eidbaooo"
    result = solution.checkInclusion(s1, s2)
    expected = True
    print(f"\nТест 1: s1 = '{s1}', s2 = '{s2}'")
    print(f"Результат: {result} (подстрока 'ba' — перестановка 'ab')")
    assert result == expected, f"Тест 1 провален!"
    print("✓ Пройден")

    # Тест 2: Перестановки нет
    s1 = "ab"
    s2 = "eidboaoo"
    result = solution.checkInclusion(s1, s2)
    expected = False
    print(f"\nТест 2: s1 = '{s1}', s2 = '{s2}'")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 2 провален!"
    print("✓ Пройден")

    # Тест 3: s1 длиннее s2
    s1 = "abc"
    s2 = "ab"
    result = solution.checkInclusion(s1, s2)
    expected = False
    print(f"\nТест 3: s1 = '{s1}', s2 = '{s2}' (s1 длиннее)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 3 провален!"
    print("✓ Пройден")

    # Тест 4: s1 и s2 одинаковые
    s1 = "abc"
    s2 = "abc"
    result = solution.checkInclusion(s1, s2)
    expected = True
    print(f"\nТест 4: s1 = '{s1}', s2 = '{s2}' (одинаковые)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 4 провален!"
    print("✓ Пройден")

    # Тест 5: Перестановка в самом начале
    s1 = "ab"
    s2 = "abx"
    result = solution.checkInclusion(s1, s2)
    expected = True
    print(f"\nТест 5: s1 = '{s1}', s2 = '{s2}' (перестановка в начале)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 5 провален!"
    print("✓ Пройден")

    # Тест 6: Перестановка в самом конце
    s1 = "ab"
    s2 = "xba"
    result = solution.checkInclusion(s1, s2)
    expected = True
    print(f"\nТест 6: s1 = '{s1}', s2 = '{s2}' (перестановка в конце)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 6 провален!"
    print("✓ Пройден")

    # Тест 7: Одиночные символы
    s1 = "a"
    s2 = "a"
    result = solution.checkInclusion(s1, s2)
    expected = True
    print(f"\nТест 7: s1 = '{s1}', s2 = '{s2}' (одиночные)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 7 провален!"
    print("✓ Пройден")

    # Тест 8: Длинная строка с перестановкой в середине
    s1 = "abc"
    s2 = "xyz" + "bca" + "www"
    result = solution.checkInclusion(s1, s2)
    expected = True
    print(f"\nТест 8: s1 = '{s1}', s2 = '{s2}' (перестановка 'bca' в середине)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 8 провален!"
    print("✓ Пройден")

    # Тест 9: Все символы одинаковые
    s1 = "aa"
    s2 = "baab"
    result = solution.checkInclusion(s1, s2)
    expected = True
    print(f"\nТест 9: s1 = '{s1}', s2 = '{s2}' (одинаковые символы)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 9 провален!"
    print("✓ Пройден")

    print("\n" + "=" * 60)
    print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО! ✓")
    print("=" * 60)


if __name__ == "__main__":
    main_counter()
