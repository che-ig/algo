class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        Разворачивает только гласные буквы в строке.
        Использует технику двух указателей.
        """
        # Используем set для проверки за O(1).
        # Включаем как строчные, так и заглавные гласные.
        vowels = set("aeiouAEIOU")

        # Преобразуем строку в список, так как строки в Python неизменяемы
        chars = list(s)

        # Инициализируем два указателя: один в начале, другой в конце
        left = 0
        right = len(s) - 1

        # Двигаем указатели навстречу друг другу
        while left < right:
            # Двигаем левый указатель вправо, пока не встретим гласную
            while left < right and chars[left] not in vowels:
                left += 1

            # Двигаем правый указатель влево, пока не встретим гласную
            while left < right and chars[right] not in vowels:
                right -= 1

            # Если указатели не пересеклись, меняем гласные местами
            if left < right:
                chars[left], chars[right] = chars[right], chars[left]

                # Двигаем оба указателя внутрь для поиска следующей пары
                left += 1
                right -= 1

        # Собираем список символов обратно в строку
        return "".join(chars)
