
string_text = "AABAACAADAABAABA"
string_pattern = "AABA"


def check_occurrence(text, pattern, first, last):
    equals = True
    i = 0
    while equals is True and first <= last:
        if text[first] != pattern[i]:
            equals = False
        first += 1
        i += 1
    return equals


def print_patterns():
    text = []
    pattern = []
    for x in string_text:
        text.append(x)
    for x in string_pattern:
        pattern.append(x)
    i = 0
    while i <= len(text) - len(pattern):
        result = check_occurrence(text, pattern, i, (i + len(pattern)) - 1)
        if result:
            print("Pattern found at index " + str(i))
        i += 1


print_patterns()
