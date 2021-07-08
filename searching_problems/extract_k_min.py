arr = [7, 10, 4, 3, 20, 15]
k_val = 4
num_heap = 6


def parent(index):
    return int(index / 2)


def left(index):
    return index * 2


def right(index):
    return (index * 2) + 1


def swap(heap, x, y):
    z = heap[x]
    heap[x] = heap[y]
    heap[y] = z


# O(logN) time complexity
def min_heapify(heap, index):
    if index < num_heap:
        min_index = index
        left_index = left(index)
        if left_index < num_heap and heap[left_index] < heap[index]:
            min_index = left_index
        right_index = right(index)
        if right_index < num_heap and heap[right_index] < heap[min_index]:
            min_index = right_index
        if index != min_index:
            swap(heap, index, min_index)
            min_heapify(heap, min_index)


# O(n) time complexity
def build_min_heap(heap):
    mid = int((num_heap - 1) / 2)
    i = mid
    while i >= 0:
        min_heapify(heap, i)
        i -= 1


# O(logN) because use the min_heapify algorithm
def extract_min(heap):
    global num_heap
    min_val = heap[0]
    heap[0] = heap[num_heap - 1]
    num_heap -= 1
    min_heapify(heap, 0)
    return min_val


# O(k*logN) because invoke the extract_min algorithm which has time complexity of O(logN) for k times
def extract_min_k(heap):
    build_min_heap(heap)
    i = 0
    res_val = None
    while i < k_val:
        res_val = extract_min(heap)
        i += 1
    return res_val


print(extract_min_k(arr))
