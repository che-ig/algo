"""
Ключевая идея
Чтобы последовательность скобок была валидной (правильной), должны выполняться два правила:

    В любой момент времени количество закрывающих скобок ) не может превышать количество открывающих (.
    В финальной строке количество открывающих и закрывающих скобок должно быть равно n.

Используя эти правила, мы можем строить строку рекурсивно:

    Мы можем добавить (, если их количество пока меньше n.
    Мы можем добавить ), только если их количество строго меньше количества (.
"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """
        Генерирует все возможные валидные комбинации из n пар скобок.
        """
        result = []

        def backtrack(current: list[str], open_count: int, close_count: int) -> None:
            """
            Рекурсивно строит строку скобок.
            current - текущая собираемая строка (список символов для эффективности).
            open_count - количество добавленных открывающих скобок '('.
            close_count - количество добавленных закрывающих скобок ')'.
            """
            # Базовый случай: длина строки достигла 2 * n
            # Это значит, что мы добавили ровно n открывающих и n закрывающих скобок
            if len(current) == 2 * n:
                result.append("".join(current))
                return

            # Вариант 1: Добавляем открывающую скобку '('
            # Мы можем это сделать, если ещё не использовали все n скобок
            if open_count < n:
                current.append("(")
                backtrack(current, open_count + 1, close_count)
                current.pop()  # Отменяем выбор (Backtrack)

            # Вариант 2: Добавляем закрывающую скобку ')'
            # Мы можем это сделать только если закрывающих скобок меньше, чем открывающих
            if close_count < open_count:
                current.append(")")
                backtrack(current, open_count, close_count + 1)
                current.pop()  # Отменяем выбор (Backtrack)

        # Запускаем бэктрекинг с пустой строкой и нулевыми счётчиками
        backtrack([], 0, 0)

        return result


def main():
    """Тест-кейсы для задачи Generate Parentheses."""
    solution = Solution()
    #
    # print("=" * 60)
    # print("ТЕСТИРОВАНИЕ ЗАДАЧИ GENERATE PARENTHESES")
    # print("=" * 60)
    #
    # # Тест 1: Базовый случай n = 1
    # n = 1
    # result = solution.generateParenthesis(n)
    # expected = ["()"]
    # print(f"\nТест 1: n = {n}")
    # print(f"Результат: {result}")
    # assert result == expected, "Тест 1 провален!"
    # print("✓ Пройден")
    #
    # # Тест 2: Классический случай n = 2
    # n = 2
    # result = solution.generateParenthesis(n)
    # expected = ["(())", "()()"]
    # print(f"\nТест 2: n = {n}")
    # print(f"Результат: {result}")
    # assert sorted(result) == sorted(expected), "Тест 2 провален!"
    # print("✓ Пройден")
    #
    # Тест 3: Стандартный случай из примера LeetCode n = 3
    n = 3
    result = solution.generateParenthesis(n)
    expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    print(f"\nТест 3: n = {n}")
    print(f"Результат: {result}")
    assert sorted(result) == sorted(expected), "Тест 3 провален!"
    print("✓ Пройден")

    # Тест 4: Проверка количества для n = 4
    # Количество валидных скобочных последовательностей описывается
    # Каталонскими числами. Для n = 4 это C_4 = 14.
    n = 4
    result = solution.generateParenthesis(n)
    print(f"\nТест 4: n = {n}")
    print(f"Количество комбинаций: {len(result)}")
    assert len(result) == 14, f"Тест 4 провален! Ожидалось 14, получено {len(result)}"
    print("✓ Пройден")

    # Тест 5: Максимальное ограничение LeetCode n = 8
    # Каталонское число C_8 = 1430.
    n = 8
    result = solution.generateParenthesis(n)
    print(f"\nТест 5: n = {n} (максимальное ограничение)")
    print(f"Количество комбинаций: {len(result)}")
    assert len(result) == 1430, (
        f"Тест 5 провален! Ожидалось 1430, получено {len(result)}"
    )
    print("✓ Пройден")

    print("\n" + "=" * 60)
    print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО! ✓")
    print("=" * 60)


if __name__ == "__main__":
    main()
