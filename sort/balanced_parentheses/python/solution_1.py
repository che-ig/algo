class Solution:
    # @param A : string
    # @return an integer

    # time: O(n)
    # mem: O(1)
    def solve(self, A):
        # balance - делаем +1 если открывающаяся и -1 если закрывающаяся
        balance = 0
        for char in A:
            balance = balance + 1 if char == "(" else balance - 1
            # если balance < 0 значит недостаточно открывающих скобок и закрывающих больше
            if balance < 0:
                return 0
        return int(balance == 0)
