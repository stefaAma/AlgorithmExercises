arr = [7, 10, 4, 3, 20, 15]
k = 6


def swap(x, y):
    z = arr[x]
    arr[x] = arr[y]
    arr[y] = z


def partition(first, last):
    i = first - 1
    while first < last:
        if arr[first] <= arr[last]:
            i += 1
            swap(i, first)
        first += 1
    swap((i + 1), last)
    return i + 1


def quick_select(first, last):
    q = partition(first, last)
    if q == (k - 1):
        return arr[q]
    if q > (k - 1):
        return quick_select(first, (q - 1))
    else:
        return quick_select((q + 1), last)


print(quick_select(0, (len(arr) - 1)))
