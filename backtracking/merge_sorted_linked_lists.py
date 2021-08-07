from backtracking import reverse_linked_list as lk_list


def read_numbers_lists(first_row_idx = 3, last_row_idx = 6):
    with open("input_files/list_numbers.csv") as input_file:
        csv_input = lk_list.csv.reader(input_file)
        numbers_lists = [nums_list for index, nums_list in enumerate(csv_input) if
                         first_row_idx <= index <= last_row_idx]
        return numbers_lists


def merge_linked_lists(first_list, second_list):
    head = None
    current = None
    while first_list is not None or second_list is not None:
        new_item = None
        if first_list is None or second_list is not None and first_list.value > second_list.value:
            new_item = lk_list.ListItem(second_list.value)
            second_list = second_list.next_item
        else:
            new_item = lk_list.ListItem(first_list.value)
            first_list = first_list.next_item
        if head is None:
            head = new_item
            current = new_item
        else:
            current.next_item = new_item
            current = new_item
    return head


def merge_k_lists(linked_lists):
    while len(linked_lists) > 1:
        merged_linked_list = merge_linked_lists(linked_lists[0], linked_lists[1])
        linked_lists[0] = merged_linked_list
        del linked_lists[1]
    return linked_lists[0]


if __name__ == "__main__":
    nums_lists = read_numbers_lists()
    lk_lists = []
    for num_list in nums_lists:
        lk_lists.append(lk_list.create_linked_list(num_list))
    final_linked_list = merge_k_lists(lk_lists)
    lk_list.print_linked_list(final_linked_list)
