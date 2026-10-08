class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        """
        Возвращает количество строк в words, состоящих только из символов allowed.
        Классическое решение с явными циклами и флагом.
        """
        # Превращаем allowed в множество для поиска за O(1)
        allowed_set = set(allowed)

        # Счётчик согласованных строк
        count = 0

        # Проходим по каждому слову в массиве
        for word in words:
            # Флаг: предполагаем, что слово согласовано
            is_consistent = True

            # Проверяем каждый символ слова
            for char in word:
                # Если символ не найден в allowed_set, слово не согласовано
                if char not in allowed_set:
                    is_consistent = False
                    break  # Прерываем проверку — дальше нет смысла

            # Если после проверки всех символов флаг остался True,
            # значит слово согласовано
            if is_consistent:
                count += 1

        return count
