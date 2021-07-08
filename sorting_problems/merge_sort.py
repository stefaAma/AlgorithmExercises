arr = [7, 10, 4, 3, 20, 15, 30]
key = 7


def merge(array, first, mid, last):
    arr1 = [0] * ((mid - first) + 1)
    i = 0
    k = first
    while i < len(arr1):
        arr1[i] = array[k]
        i += 1
        k += 1
    arr2 = [0] * (last - mid)
    k = mid + 1
    j = 0
    while j < len(arr2):
        arr2[j] = array[k]
        j += 1
        k += 1
    i = 0
    j = 0
    k = first
    while i < len(arr1) or j < len(arr2):
        if j < len(arr2) and (i == len(arr1) or arr2[j] <= arr1[i]):
            array[k] = arr2[j]
            j += 1
        else:
            array[k] = arr1[i]
            i += 1
        k += 1


def merge_sort(array, first, last):
    if first < last:
        mid = int((first + last) / 2)
        merge_sort(array, first, mid)
        merge_sort(array, mid + 1, last)
        merge(array, first, mid, last)


merge_sort(arr, 0, len(arr) - 1)
print(arr)
