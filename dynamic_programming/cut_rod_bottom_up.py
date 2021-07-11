prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
k = 15
pieces = []
solution = []


def initialize_arrays():
    global pieces
    global solution
    i = 0
    while i < k:
        pieces.append({"optimal_val": 0, "first_half": -1, "second_half": -1})
        solution.append(0)
        i += 1


def cut_rod(i, n):
    max_val = 0
    j = 0
    while j < i - 1:
        j_complementary = i - j - 2
        current_val = pieces[j]["optimal_val"] + pieces[j_complementary]["optimal_val"]
        if current_val > max_val:
            max_val = current_val
            pieces[i - 1]["optimal_val"] = max_val
            pieces[i - 1]["first_half"] = j
            pieces[i - 1]["second_half"] = j_complementary
        j += 1
    if i <= len(prices) and prices[i - 1] > max_val:
        pieces[i - 1]["optimal_val"] = prices[i - 1]
        pieces[i - 1]["first_half"] = i - 1
        pieces[i - 1]["second_half"] = -1
    if i == n:
        return pieces[n - 1]["optimal_val"]
    else:
        return cut_rod(i + 1, n)


def find_solution(i):
    if pieces[i - 1]["second_half"] == -1:
        solution[i - 1] += 1
    else:
        find_solution(pieces[i - 1]["first_half"] + 1)
        find_solution(pieces[i - 1]["second_half"] + 1)


def print_solution():
    initialize_arrays()
    optimized_val = cut_rod(1, k)
    find_solution(k)
    i = 0
    print("The optimized value is (" + str(optimized_val) + ")\n")
    while i < k:
        if solution[i] != 0:
            print("There are " + str(solution[i]) + " piece/s of length (" + str(i + 1) + ")")
        i += 1


print_solution()
