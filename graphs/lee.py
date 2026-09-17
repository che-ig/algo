import collections

def create_matrix(base_task):
    matrix = []
    for line in base_task:
        row = []
        for s in line:
            if s == " ":
                row.append(-1)
            elif s == "█":
                row.append(-7)
            else:
                row.append(-1)
        matrix.append(row)
    return matrix

def get_value(matrix, rows, cols):
    if rows >= 0 and rows < len(matrix) and cols >=0 and cols < len(matrix[0]):
        return matrix[rows][cols]
    return None

def bfs(matrix, start_position):
    cell = get_value(matrix, start_position[0], start_position[1])
    if cell is None or cell == -7:
        return
    matrix[start_position[0]][start_position[1]] = 0
    cell_deque = collections.deque()
    cell_deque.append(start_position)
    while len(cell_deque) > 0:
        current_cell_position = cell_deque.popleft()
        row,column = current_cell_position
        if get_value(matrix, row - 1, column) == -1:#UP
            matrix[row - 1][column] = matrix[row][column] + 1
            cell_deque.append((row - 1, column))
        if get_value(matrix, row + 1, column) == -1: #DOWN
            matrix[row + 1][column] = matrix[row][column] + 1
            cell_deque.append((row + 1, column))
        if get_value(matrix, row, column - 1 ) == -1: #LEFT
            matrix[row][column - 1] = matrix[row][column] + 1
            cell_deque.append((row, column - 1))
        if get_value(matrix, row, column + 1 ) == -1: #RIGHT
            matrix[row][column + 1] = matrix[row][column] + 1
            cell_deque.append((row, column + 1))

def get_path(matrix, start_position, end_position):
    bfs(matrix,start_position)
    row, column = end_position
    if matrix[row][column] < 0:
        return []
    path = [end_position]
    while (row,column)!= start_position:
        if get_value(matrix, row - 1, column) == matrix[row][column] - 1:#UP
            path.append((row - 1, column))
            row,column = row - 1, column
        elif get_value(matrix, row + 1, column) == matrix[row][column] - 1: #DOWN
            path.append((row + 1, column))
            row,column = row + 1, column
        elif get_value(matrix, row, column - 1 ) == matrix[row][column] - 1: #LEFT
            path.append((row, column - 1))
            row,column = row, column - 1
        elif get_value(matrix, row, column + 1 ) == matrix[row][column] - 1: #RIGHT
            path.append((row, column + 1))
            row,column = row, column + 1
    path.reverse()
    return path

def print_task(base_task):
    for row in base_task:
        print(row)

def find_and_print_path(base_task, start_position, end_position):
    matrix = create_matrix(base_task)
    path = get_path(matrix, start_position, end_position)
    if len(path) > 0:
        for row in range(len(base_task)):
            for column in range(len(base_task[row])):
                if (row,column) == start_position:
                    print("☺",end="")
                elif (row,column) == end_position:
                    print("◊",end="")
                elif (row, column) in path:
                    print("·",end="")
                else:
                    print(base_task[row][column], end="")
            print()




base_task = [" █ █      ",
             " █ █  █   ",
             " █ █  █   ",
             " █ ████   ",
             " █        ",
             " █   █ ███",
             " █   █    ",
             " ███ ██   ",
             "      ███ ",
             "        █ "]

print_task(base_task)

print()

find_and_print_path(base_task,(0,0),(9,9))