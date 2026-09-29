class Solution:
    def generate(self, n, balance, currParentheses, allParentheses):
        # balance < 0 - закрывающих больше, чем открывающих
        # balance > n - len(currParentheses) - не хватит закрывающих скобок
        if balance < 0 or balance > n - len(currParentheses):
            return

        if balance == 0 and len(currParentheses) == n:
            allParentheses.append("".join(currParentheses))
            return

        # Перебираем оба варианта
        for brace, newBalance in [["(", balance + 1], [")", balance - 1]]:
            currParentheses.append(brace)
            self.generate(n, newBalance, currParentheses, allParentheses)
            currParentheses.pop()

    def generateParenthesis(self, n: int) -> list[str]:
        allParentheses = []
        self.generate(n * 2, 0, [], allParentheses)
        return allParentheses
