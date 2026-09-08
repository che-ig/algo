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
