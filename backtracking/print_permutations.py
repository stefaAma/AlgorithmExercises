
string_text = "ciao"


def recursive_print(array, permutation):
    i = 0
    length = len(array)
    if i == length:
        print(str(permutation))
    while i < length:
        copy = array.copy()
        copy.pop(i)
        permutation.append(array[i])
        recursive_print(copy, permutation)
        permutation.pop()
        i += 1


def print_all_permutations(text):
    array = []
    for x in text:
        array.append(x)
    recursive_print(array, [])


print_all_permutations(string_text)
