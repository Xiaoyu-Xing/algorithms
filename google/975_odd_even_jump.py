import bisect


def jump(A):
    length = len(A)
    A_sort = [(number, i) for i, number in enumerate(A)].sort()
    odd = [0] * length
    even = [0] * length
    odd[-1] = even[-1] = 1
    for i in range(length - 2, -1, -1):
        to_end = A[i + 1:]
        right = bisect.bisect(to_end.sort(), A[i])
        if right < len(to_end):
            next_move = to_end.index(to_end.sort()[right + 1]) + i + 1
            odd[i] = odd[next_move]
        else:
            odd[i] = 0
    for i in range(length - 2, -1, -1):
        to_end = A[i + 1:]
        left = bisect.bisect_left(to_end.sort(), A[i])
        if right > 0:
            next_move = to_end.index(to_end.sort()[left - 1]) + i + 1
            even[i] = even[next_move]
        else:
            even[i] = 0
    print(odd, even)
    new = [0] * length
    new[-1] = 1
    for i in range(length - 1):
        odd = True
        j
        while j
