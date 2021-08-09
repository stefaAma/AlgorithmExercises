from backtracking import reverse_linked_list as lk_list
from backtracking import rotate_k_items as k_read


def remove_nth_item_from_end(n, previous, current):
    if current.next_item is None:
        current_val = 1
        if n == current_val:
            if previous is not None:
                previous.next_item = None
            current = None
        if previous is not None:
            return current_val
        else:
            return current
    else:
        current_val = 1 + remove_nth_item_from_end(n, current, current.next_item)
        head = current
        if current_val == n:
            if previous is not None:
                previous.next_item = current.next_item
            else:
                head = current.next_item
            del current
        if previous is not None:
            return current_val
        else:
            return head


if __name__ == "__main__":
    numbers = lk_list.read_number_list()
    nth_item = k_read.read_k_value()
    linked_list = lk_list.create_linked_list(numbers)
    lk_list.print_linked_list(remove_nth_item_from_end(nth_item, None, linked_list))
