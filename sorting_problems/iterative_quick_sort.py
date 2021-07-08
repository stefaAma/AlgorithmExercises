arr = [10, 9, 8, 7, 4, 70, 60, 7, 50, 2, 1, -2, 0, 0]


class Stack(object):
    def __init__(self):
        self.stack = []
        self.top = - 1

    def push(self, val):
        self.stack.append(val)
        self.top += 1

    def pop(self):
        val = None
        if self.top != -1:
            val = self.stack.pop(self.top)
            self.top -= 1
        return val

    def size(self):
        return self.top + 1


def partition(array, first, last):
    min_index = first - 1
    while first < last:
        if array[first] < array[last]:
            if min_index + 1 != first:
                array[min_index + 1], array[first] = array[first], array[min_index + 1]
            min_index += 1
        first += 1
    if min_index + 1 != last:
        array[last], array[min_index + 1] = array[min_index + 1], array[last]
    return min_index + 1


def iterative_quick_sort(array):
    stack = Stack()
    first = 0
    last = len(array) - 1
    base_case = False
    while base_case is False or stack.size() > 0:
        if base_case:
            q = stack.pop()
            first = q + 1
            if stack.size() == 0:
                last = len(array) - 1
            else:
                prev_q = stack.pop()
                last = prev_q - 1
                stack.push(prev_q)
            if last - first + 1 >= 2:
                base_case = False
        else:
            q = partition(array, first, last)
            stack.push(q)
            last = q - 1
            if last - first + 1 < 2:
                base_case = True


iterative_quick_sort(arr)
print(str(arr))
