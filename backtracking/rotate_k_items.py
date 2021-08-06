from backtracking import reverse_linked_list as lk_list


def read_k_value():
    with open("input_files/list_numbers.csv") as input_file:
        csv_input = lk_list.csv.reader(input_file)
        val = [num for index, num in enumerate(csv_input) if index == 1]
        return int(val[0][0])


def linked_list_length(current):
    if current.next_item is None:
        return 1
    return 1 + linked_list_length(current.next_item)


def detach_last_item(current):
    if current.next_item is None:
        return current
    last_item = detach_last_item(current.next_item)
    if current.next_item == last_item:
        current.next_item = None
    return last_item


def rotate_items(head, rotations):
    for i in range(rotations):
        last_item = detach_last_item(head)
        last_item.next_item = head
        head = last_item
    return head


if __name__ == "__main__":
    k = read_k_value()
    numbers = lk_list.read_number_list()
    linked_list = lk_list.create_linked_list(numbers)

    rotated_list = rotate_items(linked_list, k)
    lk_list.print_linked_list(rotated_list)
