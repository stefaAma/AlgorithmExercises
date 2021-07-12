prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
k = 15
pieces = []
solution = []


def initialize_arrays():
    i = 0
    while i < k:
        pieces.append({"optimal_val": 0, "first_half": -1, "second_half": -1})
        solution.append(0)
        i += 1


def cut_rod(i):
    if pieces[i]["optimal_val"] != 0:
        return pieces[i]["optimal_val"]
    if i == 0:
        return prices[0]
    j = 0
    max_val = 0
    while j < i:
        val = cut_rod(j) + cut_rod(i - j - 1)
        if val > max_val:
            max_val = val
            pieces[i]["optimal_val"] = max_val
            pieces[i]["first_half"] = j
            pieces[i]["second_half"] = i - j - 1
        j += 1
    if i <= len(prices) - 1 and prices[i] > pieces[i]["optimal_val"]:
        pieces[i]["optimal_val"] = prices[i]
        pieces[i]["first_half"] = i
        pieces[i]["second_half"] = -1
    return pieces[i]["optimal_val"]


def find_solution(i):
    if i == 0 or pieces[i]["first_half"] == i:
        solution[i] += 1
    else:
        find_solution(pieces[i]["first_half"])
        find_solution(pieces[i]["second_half"])


def print_solution():
    if k >= 1:
        initialize_arrays()
        optimized_val = cut_rod(k - 1)
        find_solution(k - 1)
        print("The optimized value is (" + str(optimized_val) + ")\n")
        i = 0
        while i < k:
            if solution[i] != 0:
                print("There are " + str(solution[i]) + " piece/s of length (" + str(i + 1) + ")")
            i += 1
    else:
        print("The rod length MUST BE >= 1")


print_solution()
