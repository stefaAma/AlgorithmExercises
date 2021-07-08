arr = [7, 10, 4, 3, 20, 15]
k = 3


def parent(index):
    return int(index / 2)


def left(index):
    return ((index + 1) * 2) - 1


def right(index):
    return (index + 1) * 2


def swap(array, x, y):
    z = array[x]
    array[x] = array[y]
    array[y] = z


def max_heapify(heap, index):
    if index < k:
        right_index = right(index)
        max_index = index
        if right_index < k and arr[right_index] > arr[index]:
            max_index = right_index
        left_index = left(index)
        if left_index < k and arr[left_index] > arr[max_index]:
            max_index = left_index
        if index != max_index:
            swap(arr, index, max_index)
            max_heapify(heap, max_index)


def build_max_heap(heap):
    i = int((k - 1) / 2) - 1
    while i >= 0:
        max_heapify(heap, i)
        i -= 1


def extract_k(heap):
    build_max_heap(heap)
    i = k
    while i < len(arr):
        if heap[i] < heap[0]:
            heap[0] = heap[i]
            max_heapify(heap, 0)
        i += 1
    return heap[0]


build_max_heap(arr)
print(arr)
print(extract_k(arr))
