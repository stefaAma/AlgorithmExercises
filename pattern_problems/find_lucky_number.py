n = 27


def is_lucky(position, counter):
    # an alternative condition could be (position == counter - 1)
    if position < counter:
        return True
    if position % counter == 0:
        return False
    position = position - int(position / counter)
    return is_lucky(position, counter + 1)


if is_lucky(n, 2) is True:
    print("Number " + str(n) + " is LUCKY")
else:
    print("Number " + str(n) + " is NOT LUCKY")
