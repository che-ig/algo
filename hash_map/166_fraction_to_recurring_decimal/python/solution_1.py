class Solution:
    def fractionToDecimal(self, numerator, denominator):
        # Обработка нуля
        if numerator == 0:
            return "0"

        result = []

        # 1. Определяем знак результата
        # XOR знаков: если ровно один из них отрицательный — результат отрицательный
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")

        # 2. Работаем с абсолютными значениями
        # В Python нет проблемы переполнения, но логически правильно
        num = abs(numerator)
        den = abs(denominator)

        # 3. Целая часть
        result.append(str(num // den))
        remainder = num % den

        # Если остаток 0 — дробь конечная, возвращаем результат
        if remainder == 0:
            return "".join(result)

        # 4. Дробная часть
        result.append(".")

        # Словарь: остаток → позиция в result, где будет записана цифра
        # Это нужно, чтобы знать, куда вставить открывающую скобку '('
        remainder_map = {}

        while remainder != 0:
            # Если такой остаток уже встречался — нашли период!
            if remainder in remainder_map:
                # Вставляем '(' на позицию, где началась периодическая часть
                result.insert(remainder_map[remainder], "(")
                result.append(")")
                break

            # Запоминаем позицию текущего остатка
            remainder_map[remainder] = len(result)

            # Деление в столбик: умножаем остаток на 10
            remainder *= 10

            # Добавляем очередную цифру дробной части
            result.append(str(remainder // den))

            # Обновляем остаток
            remainder %= den

        return "".join(result)
