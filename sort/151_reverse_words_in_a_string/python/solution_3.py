"""
Алгоритм O(1)O(1)O(1) памяти (Классический follow-up)
В языках с изменяемыми строками (C++, Java, Rust) от вас могут потребовать решить задачу in-place, то есть без создания новых строк или массивов слов.
Поскольку в Python строки неизменяемы (immutable), для демонстрации этого алгоритма мы сначала конвертируем строку в список символов (массив).
Алгоритм состоит из 3 шагов:

    Развернуть весь массив символов целиком.
    Развернуть каждое слово внутри массива по отдельности.
    «Сжать» массив, удалив лишние пробелы (сдвинуть символы влево).
"""

"""
Почему подход O(1) так важен?
Если вы придете на собеседование в FAANG и сразу напишете s.split()[::-1], вас могут спросить: "Отлично, а как бы вы сделали это на C++ без выделения дополнительной памяти?". Знание трехшагового алгоритма (Reverse All -> Reverse Words -> Clean Spaces) показывает, что вы понимаете, как алгоритмы работают под капотом, а не просто знаете синтаксис Python.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        # Конвертируем в список символов, чтобы менять на месте
        chars = list(s)
        n = len(chars)

        # Шаг 1: Разворачиваем всю строку целиком
        self._reverse(chars, 0, n - 1)

        # Шаг 2: Разворачиваем каждое слово и попутно удаляем лишние пробелы
        self._clean_and_reverse_words(chars, n)

        return "".join(chars)

    def _reverse(self, chars: list, left: int, right: int) -> None:
        """Разворачивает подмассив символов от left до right."""
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

    def _clean_and_reverse_words(self, chars: list, n: int) -> None:
        """Разворачивает слова и сдвигает их влево, убирая лишние пробелы."""
        write_idx = 0  # Указатель для записи "чистого" результата

        i = 0
        while i < n:
            # Пропускаем пробелы
            while i < n and chars[i] == " ":
                i += 1
            if i >= n:
                break

            # Нашли начало слова
            start = i
            while i < n and chars[i] != " ":
                i += 1
            end = i - 1

            # Разворачиваем текущее слово
            self._reverse(chars, start, end)

            # Копируем слово на позицию write_idx
            # (если это не первое слово, добавляем один пробел перед ним)
            if write_idx > 0:
                chars[write_idx] = " "
                write_idx += 1

            # Копируем символы слова
            for k in range(start, end + 1):
                chars[write_idx] = chars[k]
                write_idx += 1

        # Обрезаем хвост массива (лишние символы в конце)
        del chars[write_idx:]


if __name__ == "__main__":
    solution = Solution()

    # Пример 1
    s1 = "the sky is blue"
    print(f"Input:  '{s1}'")
    print(f"Output: '{solution.reverseWords(s1)}'")
    print(f"Ожидание: 'blue is sky the'\n")

    # Пример 2
    s2 = "  hello world  "
    print(f"Input:  '{s2}'")
    print(f"Output: '{solution.reverseWords(s2)}'")
    print(f"Ожидание: 'world hello'\n")

    # Пример 3
    s3 = "a good   example"
    print(f"Input:  '{s3}'")
    print(f"Output: '{solution.reverseWords(s3)}'")
    print(f"Ожидание: 'example good a'\n")
