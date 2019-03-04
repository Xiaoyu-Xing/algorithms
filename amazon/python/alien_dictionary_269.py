from collections import defaultdict
from collections import deque

# reference: https://leetcode.com/problems/alien-dictionary/discuss/156130/Python-Solution-with-Detailed-Explanation-(91)
# improvement: applicable to language more than 26 letters (arbitrary lenght of alphabet)
def alienOrder(words):
    # children dict is to store the topological order descendents
    # degree is to store ascendent of a vertex in topological order
    children = defaultdict(set)
    degree = defaultdict(set)
    # Must have, need to populate every letter in above two dicts,
    # because some letter may miss due to not able to enter below if condition
    for each_word in words:
        for each_letter in each_word:
            children[each_letter]
            degree[each_letter]

    # In each pair of consecutive words, we can only learn 1 piece of information
    # Because one letter diff will sort two words
    for i in range(len(words) - 1):
        for first, second in zip(words[i], words[i + 1]):
            if first != second:
                children[first].add(second)
                degree[second].add(first)
                break

    # print(children, degree)
    # Queue is for BFS from degree 0 to larger degree
    # Populate queue with degree 0 element first
    queue = deque()
    for key in children.keys():
        if len(degree[key]) == 0:
            queue.append(key)
    # Ans list
    ans = []
    while queue:
        parent = queue.popleft()
        ans.append(parent)
        for child in children[parent]:
            degree[child].remove(parent)
            # Whenever degree to 0, there is no dependency/parents for this element
            if len(degree[child]) == 0:
                queue.append(child)
    # print(children, degree)
    for each, parents in degree.items():
        if len(parents) != 0:
            return ''
    return ''.join(ans)


print(alienOrder([
    "wrt",
    "wrf",
    "er",
    "ett",
    "rftt"
]))

print(alienOrder([
    'z', 'z'
]))

print(alienOrder([
    'ab', 'adc'
]))

print(alienOrder(["za", "zb", "ca", "cb"]))
