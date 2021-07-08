arr1 = [1, 5, 10, 20, 40, 80, 90, 120, 130]
arr2 = [6, 7, 20, 80, 100, 120]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

x = len(arr1)
y = len(arr2)
z = len(arr3)

i = 0
j = 0
k = 0

while i < x and j < y and k < z:
    if arr1[i] > arr2[j]:
        j = j + 1
    if arr2[j] > arr1[i]:
        i = i + 1
    if arr1[i] > arr3[k]:
        k = k + 1
    if arr3[k] > arr1[i]:
        i = i + 1
    if arr2[j] > arr3[k]:
        k = k + 1
    if arr3[k] > arr2[j]:
        j = j + 1
    if arr1[i] == arr2[j] == arr3[k]:
        print("val: " + str(arr1[i]))
        i = i + 1
        j = j + 1
        k = k + 1
