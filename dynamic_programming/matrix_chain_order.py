matrix_one = [[0 for x in range(7)] for y in range(20)]
matrix_two = [[0 for x in range(25)] for y in range(7)]
matrix_three = [[0 for x in range(15)] for y in range(25)]
matrix_four = [[0 for x in range(25)] for y in range(15)]

matrix_list = [matrix_one, matrix_two, matrix_three, matrix_four]
n = len(matrix_list)
optimal_values = [[{"optimal_val": 0, "rows": -1, "columns": -1, "k": -1} for x in range(n)] for y in range(n)]


def initialize_optimal_values():
    i = 0
    while i < n:
        optimal_values[i][i]["rows"] = len(matrix_list[i])
        optimal_values[i][i]["columns"] = len(matrix_list[i][0])
        i += 1


def matrix_chain_order():
    initialize_optimal_values()
    a = 2
    while a <= n:
        i = 0
        j = i + a - 1
        while j < n:
            k = i
            min_val = -1
            while k < j:
                current_val = optimal_values[i][k]["optimal_val"] + optimal_values[k + 1][j]["optimal_val"] + \
                              (optimal_values[i][k]["rows"] * optimal_values[i][k]["columns"] *
                               optimal_values[k + 1][j]["columns"])
                if min_val == -1 or current_val < min_val:
                    min_val = current_val
                    optimal_values[i][j]["optimal_val"] = min_val
                    optimal_values[i][j]["rows"] = optimal_values[i][k]["rows"]
                    optimal_values[i][j]["columns"] = optimal_values[k + 1][j]["columns"]
                    optimal_values[i][j]["k"] = k
                k += 1
            i += 1
            j += 1
        a += 1


def print_brackets(i, j):
    if i == j:
        print("Matrix n°: " + str(i + 1))
    else:
        k = optimal_values[i][j]["k"]
        print("(")
        print_brackets(i, k)
        print_brackets(k + 1, j)
        print(")")


def execute_algorithm():
    matrix_chain_order()
    print_brackets(0, n - 1)


execute_algorithm()
print(optimal_values)
