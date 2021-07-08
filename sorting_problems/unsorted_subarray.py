arr = [0, 1, 15, 25, 6, 7, 30, 40, 50]

first = -1
last = -1

min_val = 1000000
max_val = arr[0]

i = 0

while i < len(arr):
    if (i + 1) < len(arr) and arr[i] > arr[i + 1]:
        if arr[i + 1] < min_val:
            min_val = arr[i + 1]
        last = i + 1
    if arr[i] > max_val:
        max_val = arr[i]
    if arr[i] < max_val and ((i == len(arr) - 1) or (arr[i] <= arr[i + 1])):
        last = i
    i += 1

if last != -1:
    i = 0
    while first == -1:
        if min_val < arr[i]:
            first = i
        i += 1

    i = 0
    while i < len(arr):
        if first <= i <= last:
            print(str(arr[i]) + " ")
        i += 1
