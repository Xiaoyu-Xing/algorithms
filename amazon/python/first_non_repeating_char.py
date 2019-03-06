# Either use a OrderedDict or array to record the order of sequence in the string
# So no furture check is needed, which will be required used normal dictionary


from collections import OrderedDict


def non_repeating(s):
    counter = OrderedDict()
    for char in s:
        counter[char] = counter.get(char, 0) + 1

    while counter:
        curr, count = counter.popitem(last=False)
        if count == 1:
            return curr

    return None


print(non_repeating('abcdeabc'))


# or use array
def non_repeating_2(s):
    counter = [0] * 26 * 2
    for char in s:
        counter[ord(char) - 65] += 1

    for i, count in enumerate(counter):
        if count == 1:
            return chr(i + 65)

    return None


print(non_repeating_2('abcdABCDeabceABCD'))
