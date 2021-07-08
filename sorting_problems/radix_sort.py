arr = [0, 23, 14, 12, 9, 28, 1, 14]
n = len(arr)


def counting_sort(input_arr, exp):
    k = 10
    count_array = [0] * k
    output_array = [0] * len(input_arr)
    i = 0
    while i < k:
        count_array[i] = 0
        i += 1
    i = 0
    while i < len(input_arr):
        order_magnitude = int(input_arr[i] / exp)
        count_array[order_magnitude % 10] += 1
        i += 1
    i = 1
    while i < k:
        count_array[i] += count_array[i - 1]
        i += 1
    i = len(input_arr) - 1
    while i >= 0:
        order_magnitude = int(input_arr[i] / exp)
        output_array[count_array[order_magnitude % 10] - 1] = input_arr[i]
        count_array[order_magnitude % 10] -= 1
        i -= 1
    i = 0
    while i < len(input_arr):
        input_arr[i] = output_array[i]
        i += 1


def radix_sort(input_arr):
    max_val = max(input_arr)
    if max_val != 0:
        exp = 10
        x = 0
        while max_val != 0:
            max_val = int(max_val/exp)
            x += 1
        i = 0
        exp = 1
        while i < x:
            counting_sort(input_arr, exp)
            exp *= 10
            i += 1


radix_sort(arr)
print(str(arr))
