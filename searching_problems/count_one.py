arr = [1, 1, 1, 1, 1, 0, 0]
length = len(arr)


def find_last_index(array, i, j):
    mid = int((i + j) / 2)
    if mid == 0 and arr[mid] == 0:
        return -1
    if (mid == length - 1 and arr[mid] == 1) or (arr[mid] == 1 and arr[mid + 1] == 0):
        return mid
    if arr[mid] == 0:
        return find_last_index(array, i, mid - 1)
    else:
        return find_last_index(array, mid + 1, j)


print(str(find_last_index(arr, 0, length - 1) + 1))
