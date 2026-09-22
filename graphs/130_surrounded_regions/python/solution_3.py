from collections import deque


class Solution:
    # проверяем не выходят ли индексы за границу массива, True - если не выходим
    def good_idx(self, i: int, j: int, board: list[list[str]]) -> bool:
        return 0 <= i < len(board) and 0 <= j < len(board[0])

    # делаем обход и помечаем вершины пройденными
    # если flip -> true, то помечаем все пройденные вершины как X
    def bfs(
        self,
        startX: int,
        startY: int,
        visited: list[list[bool]],
        board: list[list[str]],
        flip: bool,
    ):
        # bfs запускаем только для не посещенных вершин - можно проверку делать и не внутри функции
        if visited[startX][startY] or board[startX][startY] == "X":
            return

        q = deque([(startX, startY)])
        visited[startX][startY] = True
        # перебераем шаги которые могут быть из текущий вершины
        steps = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        while len(q) > 0:
            x, y = q.popleft()
            if flip:
                board[x][y] = "X"
            for step in steps:
                # вычисляем координаты куда можем пойти
                newX, newY = x + step[0], y + step[1]
                if not self.good_idx(newX, newY, board):
                    continue
                if board[newX][newY] == "X" or visited[newX][newY]:
                    continue
                q.append([newX, newY])
                visited[newX][newY] = True

    def solve(self, board: list[list[str]]) -> None:
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        # перебираем крайние столбцы
        for i in range(len(board)):
            self.bfs(i, 0, visited, board, False)
            self.bfs(i, len(board[0]) - 1, visited, board, False)

        # перебираем крайние строки
        for i in range(len(board[0])):
            self.bfs(0, i, visited, board, False)
            self.bfs(len(board) - 1, i, visited, board, False)

        # обходим все индексы кроме крайних - т к их уже обходили
        for i in range(1, len(board) - 1):
            for j in range(1, len(board[i]) - 1):
                # bfs запускаем только для не посещенных вершин - проверка внутри
                self.bfs(i, j, visited, board, True)
