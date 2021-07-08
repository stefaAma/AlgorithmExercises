arr = [10, 3, 40, 20, 50, 80, 70]
key = 40
temp = None


def almost_bin_search(array, first, last):
    if first > last:
        return -1
    mid = int((first + last) / 2)
    global temp
    if mid + 1 < len(array) and array[mid] > array[mid + 1]:
        temp = array[mid + 1]
        if temp == key:
            return mid + 1
    elif mid - 1 >= 0 and array[mid] < array[mid - 1]:
        temp = array[mid - 1]
        if temp == key:
            return mid - 1
    else:
        if key == array[mid]:
            return mid
        temp = array[mid]
    if key > temp:
        return almost_bin_search(array, mid + 1, last)
    else:
        return almost_bin_search(array, first, mid - 1)


print(str(almost_bin_search(arr, 0, (len(arr) - 1))))
