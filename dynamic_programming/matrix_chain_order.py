import csv


def read_matrix():
    with open("matrix_dir/matrix_input.csv") as input_file:
        csv_input = csv.reader(input_file)
        mx_list = []
        current_matrix = -1
        for line in csv_input:
            if len(line) == 0:
                mx_list.append([])
                current_matrix += 1
            else:
                new_list = [int(str_num) for str_num in line]
                mx_list[current_matrix].append(new_list)
    return mx_list


def initialize_optimal_values(opt_values, mx_list, n):
    i = 0
    while i < n:
        opt_values[i][i]["rows"] = len(mx_list[i])
        opt_values[i][i]["columns"] = len(mx_list[i][0])
        i += 1


def matrix_chain_order(opt_values, mx_list, n):
    initialize_optimal_values(opt_values, mx_list, n)
    a = 2
    while a <= n:
        i = 0
        j = i + a - 1
        while j < n:
            k = i
            min_val = -1
            while k < j:
                current_val = opt_values[i][k]["optimal_val"] + opt_values[k + 1][j]["optimal_val"] + \
                              (opt_values[i][k]["rows"] * opt_values[i][k]["columns"] *
                               opt_values[k + 1][j]["columns"])
                if min_val == -1 or current_val < min_val:
                    min_val = current_val
                    opt_values[i][j]["optimal_val"] = min_val
                    opt_values[i][j]["rows"] = opt_values[i][k]["rows"]
                    opt_values[i][j]["columns"] = opt_values[k + 1][j]["columns"]
                    opt_values[i][j]["k"] = k
                k += 1
            i += 1
            j += 1
        a += 1


def print_brackets(opt_values, i, j, mx_list, ordered_mx):
    if i == j:
        ordered_mx.append(mx_list[i])
    else:
        k = opt_values[i][j]["k"]
        ordered_mx.append("(")
        print_brackets(opt_values, i, k, mx_list, ordered_mx)
        print_brackets(opt_values, k + 1, j, mx_list, ordered_mx)
        ordered_mx.append(")")


def find_multiplication_order(opt_values, mx_list, ordered_mx, n):
    matrix_chain_order(opt_values, mx_list, n)
    print_brackets(opt_values, 0, n - 1, mx_list, ordered_mx)


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


def ordered_matrix_refactoring(i, j, result_matrix, ordered_mx):
    del ordered_mx[i: j + 1]
    ordered_mx.append(0)
    k = len(ordered_mx) - 1
    while k > i:
        ordered_mx[k] = ordered_mx[k - 1]
        k -= 1
    ordered_mx[i] = result_matrix


def find_result_matrix(ordered_mx):
    left_bracket = False
    first_matrix = False
    i = 0
    while len(ordered_mx) > 1:
        if left_bracket is False:
            left_bracket = True
            i += 1
        elif first_matrix is False:
            if ordered_mx[i] != "(":
                first_matrix = True
                i += 1
            else:
                left_bracket = False
        else:
            if ordered_mx[i] != "(":
                result_matrix = multiply_matrix(ordered_mx[i - 1], ordered_mx[i])
                ordered_matrix_refactoring(i - 2, i + 1, result_matrix, ordered_mx)
                i -= 2
                if i > 0:
                    if ordered_mx[i - 1] == "(":
                        i -= 1
                    else:
                        i -= 2
            left_bracket = False
            first_matrix = False


def write_matrix(ordered_mx):
    with open("matrix_dir/matrix_output.csv", "w", newline="") as output_file:
        csv_output = csv.writer(output_file)
        for line in ordered_mx[0]:
            first_elem = [str(line[0])]
            del line[0]
            output_line = [" " + str(str_num) for str_num in line]
            csv_output.writerow(first_elem + output_line)


if __name__ == "__main__":
    matrix_list = read_matrix()
    n = len(matrix_list)
    optimal_values = [[{"optimal_val": 0, "rows": -1, "columns": -1, "k": -1} for x in range(n)] for y in range(n)]
    ordered_matrix = []

    find_multiplication_order(optimal_values, matrix_list, ordered_matrix, n)
    print("Order in which to multiply the matrices")
    print(ordered_matrix)

    find_result_matrix(ordered_matrix)
    write_matrix(ordered_matrix)
