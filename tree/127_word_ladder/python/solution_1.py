from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordlist: list[str]) -> int:
        """
        Возвращает количество слов в кратчайшей цепочке преобразований
        от beginWord до endWord, или 0 если цепочки нет.
        """
        # Если endWord нет в словаре — преобразование невозможно
        if endWord not in wordlist:
            return 0

        # Строим словарь паттернов: "*ot" -> ["hot", "dot", "lot"]
        # Это позволяет за O(1) находить всех соседей слова
        patterns = defaultdict(list)
        wordlist.append(beginWord)  # добавляем beginWord для построения паттернов

        for word in wordlist:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1 :]
                patterns[pattern].append(word)

        # BFS: очередь хранит (текущее_слово, длина_цепочки)
        queue = deque([(beginWord, 1)])
        visited = {beginWord}  # множество посещённых слов

        while queue:
            word, length = queue.popleft()

            # Если дошли до цели — возвращаем длину
            if word == endWord:
                return length

            # Проходим по всем паттернам текущего слова
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1 :]

                # Все слова с таким же паттерном — соседи (отличаются на 1 букву)
                for neighbor in patterns[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, length + 1))

        # Цепочка не найдена
        return 0


def main():
    """Тест-кейсы для задачи Word Ladder."""
    solution = Solution()

    # Тест 1: Стандартный случай из примера LeetCode
    # hit -> hot -> dot -> dog -> cog (длина 5)
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    result = solution.ladderLength(beginWord, endWord, wordList)
    print(f"Тест 1: {beginWord} -> {endWord}")
    print(f"Ожидаемый результат: 5, Получено: {result}")
    assert result == 5, f"Ожидалось 5, получено {result}"
    print("✓ Пройден\n")

    # Тест 2: endWord отсутствует в словаре
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log"]
    result = solution.ladderLength(beginWord, endWord, wordList)
    print(f"Тест 2: {beginWord} -> {endWord} (endWord отсутствует)")
    print(f"Ожидаемый результат: 0, Получено: {result}")
    assert result == 0, f"Ожидалось 0, получено {result}"
    print("✓ Пройден\n")

    # Тест 3: Короткая цепочка
    # hot -> dot -> dog (длина 3)
    beginWord = "hot"
    endWord = "dog"
    wordList = ["hot", "dog", "dot"]
    result = solution.ladderLength(beginWord, endWord, wordList)
    print(f"Тест 3: {beginWord} -> {endWord}")
    print(f"Ожидаемый результат: 3, Получено: {result}")
    assert result == 3, f"Ожидалось 3, получено {result}"
    print("✓ Пройден\n")

    # Тест 4: Прямое преобразование (слова отличаются на 1 букву)
    # a -> c (длина 2)
    beginWord = "a"
    endWord = "c"
    wordList = ["a", "b", "c"]
    result = solution.ladderLength(beginWord, endWord, wordList)
    print(f"Тест 4: {beginWord} -> {endWord} (прямое преобразование)")
    print(f"Ожидаемый результат: 2, Получено: {result}")
    assert result == 2, f"Ожидалось 2, получено {result}"
    print("✓ Пройден\n")

    # Тест 5: Нет пути между словами
    # "talk" и "tail" могут быть связаны, но если в словаре нет промежуточных слов
    beginWord = "talk"
    endWord = "tail"
    wordList = ["talk", "tons", "tail"]
    result = solution.ladderLength(beginWord, endWord, wordList)
    print(f"Тест 5: {beginWord} -> {endWord} (нет пути)")
    print(f"Ожидаемый результат: 0, Получено: {result}")
    assert result == 0, f"Ожидалось 0, получено {result}"
    print("✓ Пройден\n")

    # Тест 6: beginWord уже равен endWord (хотя по условию задачи это редкость)
    beginWord = "cat"
    endWord = "cat"
    wordList = ["cat"]
    result = solution.ladderLength(beginWord, endWord, wordList)
    print(f"Тест 6: {beginWord} -> {endWord} (начальное слово = конечное)")
    print(f"Ожидаемый результат: 1, Получено: {result}")
    assert result == 1, f"Ожидалось 1, получено {result}"
    print("✓ Пройден\n")

    # Тест 7: Более длинная цепочка
    # "red" -> "ted" -> "tex" -> "tax" (длина 4)
    beginWord = "red"
    endWord = "tax"
    wordList = ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]
    result = solution.ladderLength(beginWord, endWord, wordList)
    print(f"Тест 7: {beginWord} -> {endWord} (длинная цепочка)")
    print(f"Ожидаемый результат: 4, Получено: {result}")
    assert result == 4, f"Ожидалось 4, получено {result}"
    print("✓ Пройден\n")

    print("=" * 50)
    print("Все тесты пройдены успешно! ✓")


if __name__ == "__main__":
    main()
