from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        # read - указатель для чтения исходных символов
        # write - указатель для записи сжатых символов
        read = 0
        write = 0

        # Проходим по массиву, пока не прочитаем все символы
        while read < len(chars):
            # Запоминаем текущий символ для подсчета группы
            current_char = chars[read]
            count = 0

            # Считаем длину текущей группы одинаковых символов
            while read < len(chars) and chars[read] == current_char:
                read += 1
                count += 1

            # 1. Записываем сам символ
            chars[write] = current_char
            write += 1

            # 2. Если в группе больше одного символа, записываем её длину
            if count > 1:
                # Если длина >= 10, str(count) вернет строку из нескольких цифр.
                # Мы посимвольно записываем каждую цифру в массив.
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        # По условию нужно вернуть новую длину массива
        return write


# --- Проверка на примерах ---
if __name__ == "__main__":
    sol = Solution()

    chars1 = ["a", "a", "b", "b", "c", "c", "c"]
    print(sol.compress(chars1), chars1)
    # Ожидается: 6, ['a', '2', 'b', '2', 'c', '3']

    chars2 = ["a"]
    print(sol.compress(chars2), chars2)
    # Ожидается: 1, ['a']

    chars3 = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    print(sol.compress(chars3), chars3)
    # Ожидается: 4, ['a', 'b', '1', '2']
