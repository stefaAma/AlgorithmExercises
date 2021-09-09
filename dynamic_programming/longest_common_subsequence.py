from collections import deque


def lcs_length(string_one, string_two):
    m = len(string_one)
    n = len(string_two)
    lcs_matrix_length = [[0 for x in range(n + 1)] for x in range(m + 1)]
    for i in range(m):
        for j in range(n):
            if string_one[i] == string_two[j]:
                lcs_matrix_length[i + 1][j + 1] = lcs_matrix_length[i][j] + 1
            elif lcs_matrix_length[i + 1][j] >= lcs_matrix_length[i][j + 1]:
                lcs_matrix_length[i + 1][j + 1] = lcs_matrix_length[i + 1][j]
            else:
                lcs_matrix_length[i + 1][j + 1] = lcs_matrix_length[i][j + 1]
    return lcs_matrix_length


def print_lcs(lcs_matrix_length, string_one, string_two):
    m = len(string_one)
    n = len(string_two)
    stack = deque()
    while m >= 1 and n >= 1:
        if string_one[m - 1] == string_two[n - 1]:
            stack.append(string_one[m - 1])
            m -= 1
            n -= 1
        elif lcs_matrix_length[m - 1][n] >= lcs_matrix_length[m][n - 1]:
            m -= 1
        else:
            n -= 1
    lcs_string = ""
    stack_len = len(stack)
    for i in range(stack_len):
        lcs_string = lcs_string + stack.pop()
    print(f"The LCS between -- {string_one} -- and -- {string_two} -- is -- {lcs_string} ")


if __name__ == "__main__":
    s1 = input("Please insert string_one:  ")
    s2 = input("Please insert string_two:  ")
    print_lcs(lcs_length(s1, s2), s1, s2)
