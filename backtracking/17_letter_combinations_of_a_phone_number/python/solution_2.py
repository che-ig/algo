"""
Сложность алгоритма

    Время: O(4^N * N), где N — длина строки digits.
        В худшем случае (цифры 7 и 9) у каждой цифры 4 варианта. Всего комбинаций 4^N.
        Сборка строки через "".join() занимает O(N) времени.
    Память: O(4^N * N) для глубины стека рекурсии и списка current_path (не считая памяти для хранения самого ответа).
"""


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) <= 0:
            return []

        phoneSymbols = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        combinationsCount = 1
        for digit in digits:
            combinationsCount *= len(phoneSymbols[digit])

        result = ["" for _ in range(combinationsCount)]
        # сколько раз будем повторять одну и ту же букву - ее период
        symbolPeriod = combinationsCount

        for digit in digits:
            # сколько раз будем повторять одну и ту же букву
            symbolPeriod = symbolPeriod // len(phoneSymbols[digit])

            # сколько раз повторяем все буквы, чтобы добавить символ к каждому ответу
            allLattersPeriod = (
                combinationsCount // symbolPeriod // len(phoneSymbols[digit])
            )

            i = 0
            for _ in range(allLattersPeriod):
                for symbol in phoneSymbols[digit]:
                    for _ in range(symbolPeriod):
                        result[i] += symbol
                        i += 1
        return result


class Solution_2:
    def bruteforce(self, idx: int, digits: str, currCombination: str, allCombinations):
        if idx == len(digits):
            # список превращаем в строку
            allCombinations.append("".join(currCombination))
            return
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        digit = digits[idx]
        for letter in phone[digit]:
            # добавили новую букву
            currCombination.append(letter)
            # перебрали все варианты для текущей буквы
            self.bruteforce(idx + 1, digits, currCombination, allCombinations)
            # убрали букву
            currCombination.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        # без if-a на входные данные "" вернем [""], а должно быть []
        if len(digits) == 0:
            return []
        ans = []
        self.bruteforce(0, digits, [], ans)
        return ans
