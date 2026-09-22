from collections import defaultdict, deque


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: list[str]
    ) -> list[list[str]]:
        """
        Находит все кратчайшие пути преобразования от beginWord до endWord.
        Возвращает список списков слов, или пустой список если пути нет.
        """
        # Если endWord нет в словаре — преобразование невозможно
        if endWord not in wordList:
            return []

        # Добавляем beginWord в словарь для построения графа
        wordList.append(beginWord)

        # Шаг 1: Строим граф через паттерны
        # pattern_to_words["*ot"] = ["hot", "dot", "lot"]
        pattern_to_words = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1 :]
                pattern_to_words[pattern].append(word)

        # Шаг 2: BFS для вычисления кратчайших расстояний от beginWord
        # distance[word] = минимальное количество шагов от beginWord до word
        distance = {beginWord: 0}
        queue = deque([beginWord])

        while queue:
            current_word = queue.popleft()

            # Если дошли до endWord — можно остановить BFS
            # (все слова на этом уровне уже обработаны)
            if current_word == endWord:
                break

            # Проходим по всем соседям текущего слова
            for i in range(len(current_word)):
                pattern = current_word[:i] + "*" + current_word[i + 1 :]

                for neighbor in pattern_to_words[pattern]:
                    # Если сосед ещё не посещён — добавляем в очередь
                    if neighbor not in distance:
                        distance[neighbor] = distance[current_word] + 1
                        queue.append(neighbor)

        # Если endWord не достижим — возвращаем пустой список
        if endWord not in distance:
            return []

        # Шаг 3: DFS для восстановления всех кратчайших путей
        # Идём от endWord к beginWord, используя информацию о расстояниях
        all_paths = []
        current_path = [endWord]

        def dfs(current_word: str) -> None:
            """
            Рекурсивно восстанавливает все кратчайшие пути от current_word до beginWord.
            """
            # Базовый случай: достигли beginWord
            if current_word == beginWord:
                # Разворачиваем путь (так как шли от endWord к beginWord)
                all_paths.append(current_path[::-1])
                return

            # Проходим по всем соседям текущего слова
            for i in range(len(current_word)):
                pattern = current_word[:i] + "*" + current_word[i + 1 :]

                for neighbor in pattern_to_words[pattern]:
                    # Идём только к словам с расстоянием на 1 меньше
                    # Это гарантирует, что мы движемся по кратчайшему пути
                    if (
                        neighbor in distance
                        and distance[neighbor] == distance[current_word] - 1
                    ):
                        current_path.append(neighbor)
                        dfs(neighbor)
                        current_path.pop()  # Backtracking: убираем слово из пути

        # Запускаем DFS от endWord
        dfs(endWord)

        return all_paths


def main():
    solution = Solution()

    # Тест 1: Стандартный случай с двумя путями
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    result = solution.findLadders(beginWord, endWord, wordList)
    print(f"Тест 1: {beginWord} -> {endWord}")
    print(f"Результат: {result}")
    expected = [
        ["hit", "hot", "dot", "dog", "cog"],
        ["hit", "hot", "lot", "log", "cog"],
    ]
    assert sorted(result) == sorted(expected), (
        f"Ожидалось {expected}, получено {result}"
    )
    print("✓ Пройден\n")

    # Тест 2: endWord отсутствует в словаре
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log"]
    result = solution.findLadders(beginWord, endWord, wordList)
    print(f"Тест 2: {beginWord} -> {endWord} (endWord отсутствует)")
    print(f"Результат: {result}")
    assert result == [], f"Ожидалось [], получено {result}"
    print("✓ Пройден\n")

    # Тест 3: Прямое преобразование
    beginWord = "a"
    endWord = "c"
    wordList = ["a", "b", "c"]
    result = solution.findLadders(beginWord, endWord, wordList)
    print(f"Тест 3: {beginWord} -> {endWord} (прямое преобразование)")
    print(f"Результат: {result}")
    expected = [["a", "c"]]
    assert result == expected, f"Ожидалось {expected}, получено {result}"
    print("✓ Пройден\n")

    # Тест 4: Нет пути
    beginWord = "red"
    endWord = "tax"
    wordList = ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]
    result = solution.findLadders(beginWord, endWord, wordList)
    print(f"Тест 4: {beginWord} -> {endWord} (нет пути)")
    print(f"Результат: {result}")
    # Здесь путь есть: red -> ted -> tex -> tax
    expected = [["red", "ted", "tex", "tax"]]
    assert result == expected, f"Ожидалось {expected}, получено {result}"
    print("✓ Пройден\n")

    print("=" * 50)
    print("Все тесты пройдены успешно! ✓")


if __name__ == "__main__":
    main()
