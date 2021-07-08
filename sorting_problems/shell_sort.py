
arr = [10, 9, 8, 7, 4, 70, 60, 7, 50, 10, 8]


def shell_sort(array):
    n = int(len(array) / 2)
    while n > 0:
        i = n
        while i < len(array):
            val = array[i]
            j = i
            while j >= n and array[j - n] > val:
                array[j] = array[j - n]
                j -= n
            array[j] = val
            i += 1
        n = int(n / 2)


shell_sort(arr)
print(str(arr))
