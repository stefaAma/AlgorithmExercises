x = 35
k = 4
arr = [12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56]
closest = -1
best_val = 10000000
if k > 0:
    print("Output:")


def binary_search(first, last):
    global closest
    if first > last:
        global k
        k = k - 1
        print(" " + str(arr[closest]))
        return
    mid = int((first + last) / 2)
    if arr[mid] == x:
        closest = mid
        return
    val = arr[mid] - x
    global best_val
    if abs(val) < best_val:
        best_val = abs(val)
        closest = mid
    if val > 0:
        return binary_search(first, mid - 1)
    else:
        return binary_search(mid + 1, last)


binary_search(0, len(arr))
lower_bound = closest - 1
upper_bound = closest + 1

while k > 0:
    val_low = abs(arr[lower_bound] - x)
    val_up = abs(arr[upper_bound] - x)
    if val_low < val_up:
        print(" " + str(arr[lower_bound]))
        lower_bound = lower_bound - 1
    elif val_up < val_low:
        print(" " + str(arr[upper_bound]))
        upper_bound = upper_bound + 1
    else:
        print(" " + str(arr[lower_bound]))
        print(" " + str(arr[upper_bound]))
        lower_bound = lower_bound - 1
        upper_bound = upper_bound + 1
    k = k - 1
