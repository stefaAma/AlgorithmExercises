
arr = [5, 4, 1, 5, 0, 7, 2, 1, 0, 8, 2, 1, 8, 8]
length = len(arr)


def find_min_element(array):
    i = 1
    min_index = 0
    min_val = array[0]
    while i < length:
        if array[i] <= min_val:
            min_val = array[i]
            min_index = i
        i += 1
    return min_index


def find_max_element(array):
    i = 1
    max_val = array[0]
    max_index = 0
    while i < length:
        if array[i] > max_val:
            max_val = array[i]
            max_index = i
        i += 1
    return max_index


def min_element_swapping(array, index):
    swap = 0
    while index < length - 1:
        array[index], array[index + 1] = array[index + 1], array[index]
        swap += 1
        index += 1
    return swap


def max_element_swapping(array, index):
    swap = 0
    while index > 0:
        array[index], array[index - 1] = array[index - 1], array[index]
        index -= 1
        swap += 1
    return swap


def number_of_swaps(array):
    swaps = 0
    index = find_min_element(array)
    swaps += min_element_swapping(array, index)
    index = find_max_element(array)
    swaps += max_element_swapping(array, index)
    return swaps


print(str(number_of_swaps(arr)))
