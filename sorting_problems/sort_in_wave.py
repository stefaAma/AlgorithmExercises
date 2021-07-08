arr = [3, 6, 5, 10, 7, 20]
length = len(arr) - 2


def swap(array, i, j):
    x = array[i]
    array[i] = array[j]
    array[j] = x


def sort_in_wave_form(array):
    i = 0
    while i <= length:
        if i % 2 == 0:
            if array[i] < array[i + 1]:
                swap(array, i, i + 1)
        else:
            if array[i] > array[i + 1]:
                swap(array, i, i + 1)
        i += 1


sort_in_wave_form(arr)
print("Array in wave form: " + str(arr))
