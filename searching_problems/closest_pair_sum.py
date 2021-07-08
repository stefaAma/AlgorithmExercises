arr1 = [1, 4, 5, 7]
arr2 = [10, 20, 30, 40]
find = 50

print(str(arr1))
print(str(arr2))

m = len(arr1)
n = len(arr2)

if n < m:
    arr3 = arr1
    arr1 = arr2
    arr2 = arr3
    x = m
    m = n
    n = x

MAX_VAL = 100000
diff = MAX_VAL
i = 0
index1 = -1
index2 = -1


def binary_search(arr1_i, lower_bound, upper_bound):
    if lower_bound > upper_bound:
        return
    global diff
    global find
    a = int((lower_bound + upper_bound)/2)
    new_val = abs(arr2[a] + arr1[arr1_i] - find)
    if new_val < diff:
        diff = new_val
        global index1
        global index2
        index1 = arr1_i
        index2 = a
        if diff == 0:
            return
    if arr2[a] + arr1[arr1_i] - find > 0:
        binary_search(arr1_i, lower_bound, a-1)
    else:
        binary_search(arr1_i, a + 1, upper_bound)


while diff != 0 and i < m:
    binary_search(i, 0, n-1)
    i = i + 1

print("The closest values to: " + str(find) + " are: " + str(arr1[index1]) + " and: " + str(arr2[index2]))
