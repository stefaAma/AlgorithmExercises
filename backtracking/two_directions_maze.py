maze = [[1, 1, 1, 1],
        [0, 1, 1, 1],
        [1, 1, 0, 0],
        [1, 1, 1, 1]]

row_length = 4
column_length = 4


def print_matrix(matrix):
    i = 0
    lines = len(matrix)
    while i < lines:
        j = 0
        columns = len(matrix[i])
        while j < columns:
            if matrix[i][j] == 2:
                print(" " + str(i) + " " + str(j))
            j += 1
        i += 1


def is_safe(matrix, i, j):
    if matrix[i][j] == 0:
        return False
    return True


def find_path(matrix, i, j):
    matrix[i][j] = 2
    if i == row_length - 1 and j == column_length - 1:
        return True
    if j + 1 < column_length and is_safe(matrix, i, j + 1):
        if find_path(matrix, i, j + 1) is True:
            return True
    if i + 1 < row_length and is_safe(matrix, i + 1, j):
        if find_path(matrix, i + 1, j) is True:
            return True
    matrix[i][j] = 1
    return False


if find_path(maze, 0, 0) is True:
    print_matrix(maze)
else:
    print("The solution doesn't exist")
