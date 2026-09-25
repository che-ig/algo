class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        """
        Возвращает все возможные комбинации букв для заданной строки цифр.
        Использует бэктрекинг (рекурсивный подход).
        """
        # Если строка пустая, комбинаций нет
        if not digits:
            return []

        # Словарь соответствия цифр и букв (как на кнопочном телефоне)
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []

        def backtrack(index: int, current_path: list[str]) -> None:
            """
            Рекурсивная функция для генерации комбинаций.
            index - индекс текущей обрабатываемой цифры в строке digits.
            current_path - список букв, выбранных на данный момент.
            """
            # Базовый случай: мы выбрали букву для каждой цифры
            if index == len(digits):
                result.append("".join(current_path))
                return

            # Получаем строку букв, соответствующую текущей цифре
            current_digit = digits[index]
            possible_letters = phone_map[current_digit]

            # Перебираем все возможные буквы для текущей цифры
            for letter in possible_letters:
                # 1. Выбираем букву (добавляем в путь)
                current_path.append(letter)

                # 2. Рекурсивно переходим к следующей цифре
                backtrack(index + 1, current_path)

                # 3. Отменяем выбор (backtrack), чтобы попробовать следующую букву
                current_path.pop()

        # Запускаем бэктрекинг с первой цифры (индекс 0) и пустым путём
        backtrack(0, [])

        return result

    def letterCombinationsIterative(self, digits: str) -> list[str]:
        """
        Возвращает все возможные комбинации букв для заданной строки цифр.
        Использует итеративный подход (BFS-стиль).
        """
        # Если строка пустая, комбинаций нет
        if not digits:
            return []

        # Словарь соответствия цифр и букв
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        # Начинаем с пустой строки
        combinations = [""]

        # Обрабатываем каждую цифру
        for digit in digits:
            next_combinations = []
            # Для каждой существующей комбинации добавляем все возможные буквы
            for combo in combinations:
                for letter in phone_map[digit]:
                    next_combinations.append(combo + letter)
            # Обновляем список комбинаций
            combinations = next_combinations

        return combinations


def main():
    """Тест-кейсы для задачи Letter Combinations of a Phone Number."""
    solution = Solution()

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ РЕШЕНИЯ С БЭКТРЕКИНГОМ")
    print("=" * 60)

    # Тест 1: Стандартный случай из примера LeetCode
    digits = "23"
    result = solution.letterCombinations(digits)
    expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    print(f"\nТест 1: digits = '{digits}'")
    print(f"Ожидаемый результат: {sorted(expected)}")
    print(f"Получено: {sorted(result)}")
    assert sorted(result) == sorted(expected), f"Тест 1 провален!"
    print("✓ Пройден")

    # Тест 2: Одиночная цифра
    digits = "2"
    result = solution.letterCombinations(digits)
    expected = ["a", "b", "c"]
    print(f"\nТест 2: digits = '{digits}'")
    print(f"Ожидаемый результат: {sorted(expected)}")
    print(f"Получено: {sorted(result)}")
    assert sorted(result) == sorted(expected), f"Тест 2 провален!"
    print("✓ Пройден")

    # Тест 3: Цифра с 4 буквами (7 или 9)
    digits = "7"
    result = solution.letterCombinations(digits)
    expected = ["p", "q", "r", "s"]
    print(f"\nТест 3: digits = '{digits}' (4 буквы)")
    print(f"Ожидаемый результат: {sorted(expected)}")
    print(f"Получено: {sorted(result)}")
    assert sorted(result) == sorted(expected), f"Тест 3 провален!"
    print("✓ Пройден")

    # Тест 4: Три цифры
    digits = "234"
    result = solution.letterCombinations(digits)
    print(f"\nТест 4: digits = '{digits}' (3 цифры)")
    print(f"Количество комбинаций: {len(result)}")
    print(f"Первые 5 комбинаций: {sorted(result)[:5]}")
    # Для "234" должно быть 3 * 3 * 3 = 27 комбинаций
    assert len(result) == 27, f"Тест 4 провален! Ожидалось 27, получено {len(result)}"
    print("✓ Пройден")

    # Тест 5: Максимальная длина (4 цифры) с максимальным количеством букв
    digits = "9999"
    result = solution.letterCombinations(digits)
    print(f"\nТест 5: digits = '{digits}' (максимальная длина, 4 буквы на цифру)")
    print(f"Количество комбинаций: {len(result)}")
    # Для "9999" должно быть 4^4 = 256 комбинаций
    assert len(result) == 256, f"Тест 5 провален! Ожидалось 256, получено {len(result)}"
    print("✓ Пройден")

    # Тест 6: Пустая строка (edge case)
    digits = ""
    result = solution.letterCombinations(digits)
    expected = []
    print(f"\nТест 6: digits = '{digits}' (пустая строка)")
    print(f"Ожидаемый результат: {expected}")
    print(f"Получено: {result}")
    assert result == expected, f"Тест 6 провален!"
    print("✓ Пройден")

    # Тест 7: Смешанные цифры (с разным количеством букв)
    digits = "27"
    result = solution.letterCombinations(digits)
    print(f"\nТест 7: digits = '{digits}' (3 буквы + 4 буквы)")
    print(f"Количество комбинаций: {len(result)}")
    # Для "27" должно быть 3 * 4 = 12 комбинаций
    assert len(result) == 12, f"Тест 7 провален! Ожидалось 12, получено {len(result)}"
    print("✓ Пройден")

    print("\n" + "=" * 60)
    print("ТЕСТИРОВАНИЕ ИТЕРАТИВНОГО РЕШЕНИЯ")
    print("=" * 60)

    # Тест 8: Стандартный случай для итеративного решения
    digits = "23"
    result = solution.letterCombinationsIterative(digits)
    expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    print(f"\nТест 8: digits = '{digits}' (итеративное)")
    print(f"Ожидаемый результат: {sorted(expected)}")
    print(f"Получено: {sorted(result)}")
    assert sorted(result) == sorted(expected), f"Тест 8 провален!"
    print("✓ Пройден")

    # Тест 9: Одиночная цифра для итеративного решения
    digits = "5"
    result = solution.letterCombinationsIterative(digits)
    expected = ["j", "k", "l"]
    print(f"\nТест 9: digits = '{digits}' (итеративное)")
    print(f"Ожидаемый результат: {sorted(expected)}")
    print(f"Получено: {sorted(result)}")
    assert sorted(result) == sorted(expected), f"Тест 9 провален!"
    print("✓ Пройден")

    # Тест 10: Три цифры для итеративного решения
    digits = "234"
    result = solution.letterCombinationsIterative(digits)
    print(f"\nТест 10: digits = '{digits}' (итеративное, 3 цифры)")
    print(f"Количество комбинаций: {len(result)}")
    assert len(result) == 27, f"Тест 10 провален! Ожидалось 27, получено {len(result)}"
    print("✓ Пройден")

    # Тест 11: Пустая строка для итеративного решения
    digits = ""
    result = solution.letterCombinationsIterative(digits)
    expected = []
    print(f"\nТест 11: digits = '{digits}' (итеративное, пустая строка)")
    print(f"Ожидаемый результат: {expected}")
    print(f"Получено: {result}")
    assert result == expected, f"Тест 11 провален!"
    print("✓ Пройден")

    # Тест 12: Сравнение обоих решений на одинаковых входных данных
    print("\n" + "=" * 60)
    print("СРАВНЕНИЕ ОБОИХ РЕШЕНИЙ")
    print("=" * 60)

    test_cases = ["2", "23", "234", "9999", "27", "568"]
    for digits in test_cases:
        result_recursive = solution.letterCombinations(digits)
        result_iterative = solution.letterCombinationsIterative(digits)
        print(f"\ndigits = '{digits}':")
        print(f"  Рекурсивное: {len(result_recursive)} комбинаций")
        print(f"  Итеративное: {len(result_iterative)} комбинаций")
        assert sorted(result_recursive) == sorted(result_iterative), (
            f"Результаты не совпадают для '{digits}'!"
        )
        print("  ✓ Совпадают")

    print("\n" + "=" * 60)
    print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО! ✓")
    print("=" * 60)


if __name__ == "__main__":
    main()
