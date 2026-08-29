def replace_spaces_2(s: str) -> str:
    """
    Заменяет все пробелы в строке на '@40'.

    В Python есть встроенный метод str.replace(),
    который делает ровно это.
    """
    return s.replace(" ", "@40")


def replace_spaces(s: str) -> str:
    result = []
    for ch in s:
        if ch == " ":
            result.append("@40")
        else:
            result.append(ch)
    return "".join(result)


# --- Чтение ввода в формате Coding Ninjas ---
if __name__ == "__main__":
    t = int(input())  # количество тестовых случаев

    for _ in range(t):
        s = input()
        print(replace_spaces(s))
