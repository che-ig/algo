from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Словарь: ключ — отсортированная строка, значение — список анаграмм
        # defaultdict(list) автоматически создаёт пустой список для нового ключа
        anagrams = defaultdict(list)

        for s in strs:
            # Сортируем символы строки — это будет ключом группы
            # "eat", "tea", "ate" → все превращаются в "aet"
            key = "".join(sorted(s))
            anagrams[key].append(s)

        # Возвращаем все значения словаря (списки анаграмм)
        return list(anagrams.values())


class Solution_2:
    def groupAnagrams(self, strs):
        anagrams = {}

        for s in strs:
            # Сортируем символы строки — это будет ключом группы
            key = "".join(sorted(s))

            # Проверяем, есть ли уже такой ключ в словаре
            if key not in anagrams:
                anagrams[key] = []  # создаём пустой список

            anagrams[key].append(s)

        # Возвращаем все значения словаря
        return list(anagrams.values())


class Solution_3:
    def groupAnagrams(self, strs):
        anagrams = {}

        for s in strs:
            key = "".join(sorted(s))
            # setdefault создаёт пустой список, если ключа нет
            anagrams.setdefault(key, []).append(s)

        return list(anagrams.values())
