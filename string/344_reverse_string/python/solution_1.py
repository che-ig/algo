class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Разворачивает массив символов in-place с O(1) дополнительной памяти.
        Не возвращает ничего (void), модифицирует входной массив напрямую.

        Использует два указателя, сходящихся к центру:
        - left движется слева направо
        - right движется справа налево
        На каждом шаге меняем s[left] и s[right] местами.
        """
        # left — указатель на начало текущей ещё не развёрнутой части
        left = 0

        # right — указатель на конец текущей ещё не развёрнутой части.
        # len(s) - 1 — индекс последнего элемента массива.
        right = len(s) - 1

        # Пока указатели не встретились и не пересеклись
        while left < right:
            # Меняем местами символы под указателями.
            # В Python это делается одной строкой через кортежное присваивание:
            # (s[left], s[right]) = (s[right], s[left])
            # Сначала вычисляется правая часть (создаётся кортеж),
            # потом происходит распаковка и присваивание.
            # Это не требует временной переменной!
            s[left], s[right] = s[right], s[left]

            # Двигаем указатели навстречу друг другу
            left += 1
            right -= 1


def main():
    """Тест-кейсы для задачи Reverse String."""
    solution = Solution()

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ЗАДАЧИ REVERSE STRING")
    print("=" * 60)

    # Тест 1: Стандартный случай из примера LeetCode
    s = ["h", "e", "l", "l", "o"]
    solution.reverseString(s)
    expected = ["o", "l", "l", "e", "h"]
    print(f"\nТест 1: s = {s}")
    print(f"Результат: {s}")
    assert s == expected, f"Тест 1 провален! Ожидалось {expected}, получено {s}"
    print("✓ Пройден")

    # Тест 2: Палиндром (после разворота выглядит так же, но регистр меняется)
    s = ["H", "a", "n", "n", "a", "h"]
    solution.reverseString(s)
    expected = ["h", "a", "n", "n", "a", "H"]
    print(f"\nТест 2: s = {s} (палиндром с разным регистром)")
    print(f"Результат: {s}")
    assert s == expected, f"Тест 2 провален!"
    print("✓ Пройден")

    # Тест 3: Один символ
    s = ["a"]
    solution.reverseString(s)
    expected = ["a"]
    print(f"\nТест 3: s = {s} (один символ)")
    print(f"Результат: {s}")
    assert s == expected, f"Тест 3 провален!"
    print("✓ Пройден")

    # Тест 4: Два символа
    s = ["a", "b"]
    solution.reverseString(s)
    expected = ["b", "a"]
    print(f"\nТест 4: s = {s} (два символа)")
    print(f"Результат: {s}")
    assert s == expected, f"Тест 4 провален!"
    print("✓ Пройден")

    # Тест 5: Пустая строка (по условию не бывает, но проверим)
    s = []
    solution.reverseString(s)
    expected = []
    print(f"\nТест 5: s = {s} (пустой массив)")
    print(f"Результат: {s}")
    assert s == expected, f"Тест 5 провален!"
    print("✓ Пройден")

    # Тест 6: Чётное количество символов
    s = ["a", "b", "c", "d"]
    solution.reverseString(s)
    expected = ["d", "c", "b", "a"]
    print(f"\nТест 6: s = {s} (чётное количество)")
    print(f"Результат: {s}")
    assert s == expected, f"Тест 6 провален!"
    print("✓ Пройден")

    # Тест 7: Нечётное количество символов
    s = ["a", "b", "c", "d", "e"]
    solution.reverseString(s)
    expected = ["e", "d", "c", "b", "a"]
    print(f"\nТест 7: s = {s} (нечётное количество)")
    print(f"Результат: {s}")
    assert s == expected, f"Тест 7 провален!"
    print("✓ Пройден")

    print("\n" + "=" * 60)
    print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО! ✓")
    print("=" * 60)


if __name__ == "__main__":
    main()
