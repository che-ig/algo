class Solution:
    # time: (n * n)
    # mem:  (n * n)
    # Note: Оптимально O(n) по памяти, но доска имеет размер 9x9 поэтому нет
    # смысла в оптимизации т к сложность по факту будет O(1)
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # тут храним пару (номер строки, значение)
        rows = set()
        # тут храним пару (номер колонки, значение)
        cols = set()
        # тут храним пару (номер блока, значение)
        blocks = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]
                if val == ".":
                    continue
                blockIdx = i // 3 * 3 + j // 3
                # если у нас уже есть такой элемент в строке/столбце/блоке
                # значит невалидное судоку
                if (i, val) in rows or (j, val) in cols or (blockIdx, val) in blocks:
                    return False
                rows.add((i, val))
                cols.add((j, val))
                blocks.add((blockIdx, val))
        return True
