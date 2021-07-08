arr = [10, 9, 8, 7, 4, 70, 60, 7, 50, 2, 1, -2, 0, 0]


def cycle_sort(array):
    i = 0
    while i < len(arr) - 1:
        pos = i
        item = array[i]
        j = i + 1
        while j < len(arr):
            if array[j] < item:
                pos += 1
            j += 1
        if pos != i:
            while array[pos] == item:
                pos += 1
            array[pos], item = item, array[pos]
            while pos != i:
                j = i + 1
                pos = i
                while j < len(arr):
                    if array[j] < item:
                        pos += 1
                    j += 1
                while array[pos] == item:
                    pos += 1
                array[pos], item = item, array[pos]
        i += 1


cycle_sort(arr)
print(str(arr))
