class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        """
        Проверяет, является ли массив "горным".
        Использует два указателя, идущих с краёв к центру.
        """
        n = len(arr)

        # Горный массив должен иметь минимум 3 элемента
        if n < 3:
            return False

        # left — указатель, идущий слева направо (подъём с левой стороны)
        # right — указатель, идущий справа налево (подъём с правой стороны)
        left = 0
        right = n - 1

        # Двигаем left вправо, пока элементы строго возрастают
        # Условие arr[left] < arr[left + 1] гарантирует строгое возрастание
        while left + 1 < n and arr[left] < arr[left + 1]:
            left += 1

        # Двигаем right влево, пока элементы строго возрастают (справа налево)
        # Условие arr[right] < arr[right - 1] гарантирует строгое возрастание
        # при движении справа налево (то есть убывание слева направо)
        while right - 1 >= 0 and arr[right] < arr[right - 1]:
            right -= 1

        # Теперь проверяем три условия:
        # 1. left == right — указатели встретились в одной точке (это пик)
        # 2. left != 0 — пик не в самом начале (был подъём слева)
        # 3. right != n - 1 — пик не в самом конце (был подъём справа)
        return left == right and left != 0 and right != n - 1


def main():
    """Тест-кейсы для задачи Valid Mountain Array."""
    solution = Solution()

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ЗАДАЧИ VALID MOUNTAIN ARRAY (два указателя)")
    print("=" * 60)

    # Тест 1: Слишком короткий массив
    arr = [2, 1]
    result = solution.validMountainArray(arr)
    expected = False
    print(f"\nТест 1: arr = {arr} (длина < 3)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 1 провален!"
    print("✓ Пройден")

    # Тест 2: Плато на пике
    arr = [3, 5, 5]
    result = solution.validMountainArray(arr)
    expected = False
    print(f"\nТест 2: arr = {arr} (плато на пике)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 2 провален!"
    print("✓ Пройден")

    # Тест 3: Классический горный массив
    arr = [0, 3, 2, 1]
    result = solution.validMountainArray(arr)
    expected = True
    print(f"\nТест 3: arr = {arr} (классическая гора)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 3 провален!"
    print("✓ Пройден")

    # Тест 4: Только возрастание
    arr = [1, 2, 3, 4, 5]
    result = solution.validMountainArray(arr)
    expected = False
    print(f"\nТест 4: arr = {arr} (только возрастание)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 4 провален!"
    print("✓ Пройден")

    # Тест 5: Только убывание
    arr = [5, 4, 3, 2, 1]
    result = solution.validMountainArray(arr)
    expected = False
    print(f"\nТест 5: arr = {arr} (только убывание)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 5 провален!"
    print("✓ Пройден")

    # Тест 6: Два горба
    arr = [1, 3, 2, 4, 1]
    result = solution.validMountainArray(arr)
    expected = False
    print(f"\nТест 6: arr = {arr} (два горба)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 6 провален!"
    print("✓ Пройден")

    # Тест 7: Минимальная валидная гора
    arr = [1, 3, 2]
    result = solution.validMountainArray(arr)
    expected = True
    print(f"\nТест 7: arr = {arr} (минимальная гора)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 7 провален!"
    print("✓ Пройден")

    # Тест 8: Длинная симметричная гора
    arr = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    result = solution.validMountainArray(arr)
    expected = True
    print(f"\nТест 8: arr = {arr} (длинная симметричная гора)")
    print(f"Результат: {result}")
    assert result == expected, f"Тест 8 провален!"
    print("✓ Пройден")

    print("\n" + "=" * 60)
    print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО! ✓")
    print("=" * 60)


if __name__ == "__main__":
    main()
