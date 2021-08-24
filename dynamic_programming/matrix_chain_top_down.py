from dynamic_programming import matrix_chain_order as mx_chain


def matrix_chain_order(opt_values, i, j):
    if i == j:
        return 0
    min_val = -1
    for k in range(i, j):
        current_val = matrix_chain_order(opt_values, i, k) + matrix_chain_order(opt_values, k + 1, j) + \
                      (opt_values[i][k]["rows"] * opt_values[i][k]["columns"] * opt_values[k + 1][j]["columns"])
        if min_val == -1 or current_val < min_val:
            min_val = current_val
            opt_values[i][j]["optimal_val"] = min_val
            opt_values[i][j]["rows"] = opt_values[i][k]["rows"]
            opt_values[i][j]["columns"] = opt_values[k + 1][j]["columns"]
            opt_values[i][j]["k"] = k
    return opt_values[i][j]["optimal_val"]


def find_multiplication_order(opt_values, mx_list, i, j):
    mx_chain.initialize_optimal_values(opt_values, mx_list, j + 1)
    return matrix_chain_order(opt_values, i, j)


if __name__ == "__main__":
    matrix_list = mx_chain.read_matrix()
    n = len(matrix_list)
    optimal_values = [[{"optimal_val": 0, "rows": -1, "columns": -1, "k": -1} for x in range(n)] for y in range(n)]
    ordered_matrix = []

    optimal_value = find_multiplication_order(optimal_values, matrix_list, 0, n - 1)
    mx_chain.print_brackets(optimal_values, 0, n - 1, matrix_list, ordered_matrix)
    print(f"Minimum number of scalar products required: {optimal_value}\nOrder in which to multiply the matrices")
    print(ordered_matrix)

    mx_chain.find_result_matrix(ordered_matrix)
    mx_chain.write_matrix(ordered_matrix)
