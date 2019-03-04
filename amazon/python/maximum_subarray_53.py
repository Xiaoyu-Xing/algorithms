# Best analysis: https://leetcode.com/problems/maximum-subarray/discuss/20193/DP-solution-and-some-thoughts
# Look at this youtube anaysis about Kadane's alg:
# https://www.youtube.com/watch?v=86CQq3pKSUw
# Also check Leetcode 121, sell stock for another version

# With variable memorize the max value:
def max_subarray(array):
    if not array:
        return None
    global_max = float('-inf')
    prev_max = float('-inf')
    for element in array:
        prev_max = max(element, prev_max + element)
        global_max = max(global_max, prev_max)
    return global_max


# With list as memory to memorize every thing, then pick maximum one
def max_subarray(array):
    if not array:
        return None
    mem = []
    mem.append(array[0])
    for element in array[1:]:
        mem.append(max(element, element + mem[-1]))
    return max(mem)
