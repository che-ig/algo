class Solution:
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)
        n = len(s)

        # Очередь хранит индексы, с которых мы начинаем искать следующее слово
        queue = [0]

        # Множество посещённых индексов, чтобы не обрабатывать один и тот же индекс дважды
        visited = set()
        visited.add(0)

        while queue:
            # Берём текущий индекс (начало нераспознанной части строки)
            start = queue.pop(0)

            # Если дошли до конца строки — всё разбито успешно
            if start == n:
                return True

            # Пробуем все возможные слова, начинающиеся с позиции start
            for end in range(start + 1, n + 1):
                if end not in visited and s[start:end] in word_set:
                    visited.add(end)
                    queue.append(end)

        return False
