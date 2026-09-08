from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            # Считаем частоты каждого символа (26 букв английского алфавита)
            count = [0] * 26
            for char in s:
                count[ord(char) - ord("a")] += 1

            # Преобразуем список в кортеж — его можно использовать как ключ словаря
            # (списки в Python неизменяемыми не являются, а кортежи — являются)
            key = tuple(count)
            anagrams[key].append(s)

        return list(anagrams.values())


class Solution_2:
    def groupAnagrams(self, strs):
        anagrams = {}

        for s in strs:
            # Считаем частоты каждого символа
            count = [0] * 26
            for char in s:
                count[ord(char) - ord("a")] += 1

            # Преобразуем список в кортеж для использования как ключ
            key = tuple(count)

            if key not in anagrams:
                anagrams[key] = []

            anagrams[key].append(s)

        return list(anagrams.values())
