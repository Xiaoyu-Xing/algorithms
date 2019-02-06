import bisect


def find_max_combination(list1, list2, maximum_capacity):
    list1.sort()
    list2.sort()
    ans_index = []
    curr_max = float('-inf')
    for i, first in enumerate(list1):
        left = maximum_capacity - first
        position = bisect.bisect(list2, left)
        if position and first + list2[position - 1] >= curr_max:
            second = list2(position - 1)
            if first + second > curr_max:
                curr_max = first + second
                ans_index.clear()  # ans_index = [] for python2
            for j in range(position - 1, -1, -1):
                if list1[i] + list2[j] == curr_max:
                    # or ans_index.append([first, second])
                    ans_index.append([i, j])
                else:
                    break
    return ans_index

# Or n2 solution


def find_max_combination(list1, list2, maximum_capacity):
    ans_index = []
    curr_max = float('-inf')
    for i, first in enumerate(list1):
        for j, second in enumerate(list2):
            if curr_max <= first + second <= maximum_capacity:
                if first + second > curr_max:
                    curr_max = first + second
                    ans_index.clear()  # ans_index = [] for python2
                # or ans_index.append([first, second])
                ans_index.append([i, j])
    return ans_index
