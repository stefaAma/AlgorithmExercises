# Find a triplet that sum to a given value
# Pigeonhole sort is used for sorting

arr = [1, 2, 4, 10]
sum_searched = 15


def find_min_max(array):
    min_val = array[0]
    max_val = array[0]
    i = 0
    while i < len(array):
        if array[i] > max_val:
            max_val = array[i]
        if array[i] < min_val:
            min_val = array[i]
        i += 1
    return min_val, max_val


def pigeonhole_sort(array, min_val, max_val):
    counting = []
    i = 0
    while i <= max_val - min_val:
        counting.append(0)
        i += 1
    i = 0
    while i < len(array):
        counting[array[i] - min_val] += 1
        i += 1
    i = 0
    array_index = 0
    while i <= max_val - min_val:
        while counting[i] > 0:
            array[array_index] = i + min_val
            array_index += 1
            counting[i] -= 1
        i += 1


def find_couple_sum_by_val(array, k, val):
    i = 0
    j = k - 1
    found_sum = False
    while found_sum is False and i < j:
        sum_values = array[i] + array[j] + array[k]
        if sum_values == val:
            found_sum = True
        else:
            if sum_values > val:
                j -= 1
            else:
                i += 1
    return found_sum, i, j


def find_triple_sum(array, val):
    min_val, max_val = find_min_max(array)
    pigeonhole_sort(array, min_val, max_val)
    result = False
    i = 0
    k = len(array) - 1
    j = k - 1
    while result is False and j > 0:
        result, i, j = find_couple_sum_by_val(array, k, val)
        if result is False:
            k -= 1
            j = k - 1
            i = 0
    if result:
        print("the three values are: " + str(array[i]) + " " + str(array[j]) + " " + str(array[k]))
    return result


print(str(find_triple_sum(arr, sum_searched)))
