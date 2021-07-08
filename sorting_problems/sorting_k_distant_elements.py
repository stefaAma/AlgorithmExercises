
arr = [10, 9, 8, 7, 4, 70, 60, 7, 50]
k = 5
heap_size = k + 1


def left(index):
    return ((index + 1) * 2) - 1


def right(index):
    return (index + 1) * 2


def swap(array, x, y):
    z = array[x]
    array[x] = array[y]
    array[y] = z


def parent(index):
    if index % 2 == 0:
        return int(index / 2) - 1
    return int(index / 2)


def min_heapify(heap, i):
    if len(heap) > 0:
        left_child_index = left(i)
        right_child_index = right(i)
        min_val = heap[i]
        min_index = i
        if left_child_index < len(heap) and heap[left_child_index] < min_val:
            min_val = heap[left_child_index]
            min_index = left_child_index
        if right_child_index < len(heap) and heap[right_child_index] < min_val:
            min_val = heap[right_child_index]
            min_index = right_child_index
        if min_val != heap[i]:
            swap(heap, i, min_index)
            min_heapify(heap, min_index)


def build_min_heap(array):
    i = int(len(array) / 2) - 1
    while i >= 0:
        min_heapify(array, i)
        i -= 1


def push_heap(heap, i):
    if parent(i) >= 0 and heap[i] < heap[parent(i)]:
        swap(heap, i, parent(i))
        push_heap(heap, parent(i))


def push(heap, val):
    heap.append(val)
    push_heap(heap, len(heap) - 1)


def pop(heap):
    if len(heap) > 0:
        val = heap[0]
        swap(heap, 0, len(heap) - 1)
        heap.pop(len(heap) - 1)
        min_heapify(heap, 0)
        return val


def create_subarray(array):
    i = 0
    copy = []
    while i <= k and i < len(array):
        copy.append(array[i])
        i += 1
    return copy


def sorting(array):
    heap = create_subarray(array)
    build_min_heap(heap)
    i = 0
    j = k + 1
    while j < len(array):
        array[i] = pop(heap)
        push(heap, array[j])
        i += 1
        j += 1
    while len(heap) > 0:
        array[i] = pop(heap)
        i += 1


sorting(arr)
print(str(arr))
