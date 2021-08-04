import csv


class ListItem(object):
    def __init__(self, value):
        self._value = value
        self._next_item = None

    @property
    def value(self):
        return self._value

    @property
    def next_item(self):
        return self._next_item

    @next_item.setter
    def next_item(self, item):
        self._next_item = item


def create_linked_list(numbers_list):
    head = None
    current = None
    for number in numbers_list:
        item = ListItem(int(number))
        if head is None:
            head = item
            current = item
        else:
            current.next_item = item
            current = item
    # current.next_item = None
    return head


with open("input_files/list_numbers.csv") as input_file:
    csv_input = csv.reader(input_file)
    numbers = [num_list for index, num_list in enumerate(csv_input) if index == 0]

linked_list = create_linked_list(numbers[0])


def reverse_list(previous_item, current_item):
    if current_item.next_item is None:
        current_item.next_item = previous_item
        return current_item
    else:
        new_head = reverse_list(current_item, current_item.next_item)
        current_item.next_item = previous_item
        return new_head


def print_linked_list(head):
    index = 0
    while head is not None:
        print(f"Item({index + 1}) = {head.value}")
        head = head.next_item
        index += 1


new_list = reverse_list(None, linked_list)
print_linked_list(new_list)
