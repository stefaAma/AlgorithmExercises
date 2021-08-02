import csv

with open("matrix_dir/matrix_input.csv") as input_file:
    csv_input = csv.reader(input_file)
    matrix_list = []
    current_matrix = -1
    for line in csv_input:
        if len(line) == 0:
            matrix_list.append([])
            current_matrix += 1
        else:
            new_list = [int(str_num) for str_num in line]
            matrix_list[current_matrix].append(new_list)


print(matrix_list)
n = len(matrix_list)
optimal_values = [[{"optimal_val": 0, "rows": -1, "columns": -1, "k": -1} for x in range(n)] for y in range(n)]

ordered_matrix = []


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
        # print("Matrix n°: " + str(i + 1))
        ordered_matrix.append(matrix_list[i])
    else:
        k = optimal_values[i][j]["k"]
        # print("(")
        ordered_matrix.append("(")
        print_brackets(i, k)
        print_brackets(k + 1, j)
        # print(")")
        ordered_matrix.append(")")


def execute_algorithm():
    matrix_chain_order()
    print_brackets(0, n - 1)


execute_algorithm()
# print(optimal_values)
# print(ordered_matrix)


def multiply_matrix(matrix_one, matrix_two):
    rows_one = len(matrix_one)
    columns_one = len(matrix_one[0])
    columns_two = len(matrix_two[0])
    result_matrix = []
    for i in range(rows_one):
        result_matrix.append([])
        for j in range(columns_two):
            val = 0
            for k in range(columns_one):
                val = val + (matrix_one[i][k] * matrix_two[k][j])
            result_matrix[i].append(val)
    return result_matrix


# print(multiply_matrix(matrix_list[0], matrix_list[1]))


def ordered_matrix_refactoring(i, j, result_matrix):
    del ordered_matrix[i:j]
    ordered_matrix.append(0)
    k = len(ordered_matrix) - 1
    while k > i:
        ordered_matrix[k] = ordered_matrix[k - 1]
        k -= 1
    ordered_matrix[i] = result_matrix


def find_result_matrix():
    left_bracket = False
    first_matrix = False
    # second_matrix = False
    i = 0
    while len(ordered_matrix) > 1:
        if left_bracket is False:
            left_bracket = True
            i += 1
        elif first_matrix is False:
            if ordered_matrix[i] != "(":
                first_matrix = True
                i += 1
            else:
                left_bracket = False
        if ordered_matrix[i] != "(":
            result_matrix = multiply_matrix(ordered_matrix[i - 1], ordered_matrix[i])
            ordered_matrix_refactoring(i - 2, i + 1, result_matrix)
            i -= 2
            if i > 0:
                if ordered_matrix[i - 1] == "(":
                    i -= 1
                else:
                    i -= 2
        left_bracket = False
        first_matrix = False



