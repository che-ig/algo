class Solution:
    def interpret(self, command: str) -> str:
        """
        Интерпретирует команду Goal Parser через парсинг.
        Проходим по строке и интерпретируем каждый токен.
        """
        result = []
        i = 0
        n = len(command)

        # Проходим по всем символам команды
        while i < n:
            if command[i] == "G":
                # Токен "G" → интерпретируем как "G"
                result.append("G")
                i += 1  # Переходим к следующему символу

            elif command[i] == "(" and command[i + 1] == ")":
                # Токен "()" → интерпретируем как "o"
                result.append("o")
                i += 2  # Пропускаем оба символа "()"

            elif command[i] == "(" and command[i + 1] == "a":
                # Токен "(al)" → интерпретируем как "al"
                result.append("al")
                i += 4  # Пропускаем все 4 символа "(al)"

        # Соединяем список символов в строку
        return "".join(result)
