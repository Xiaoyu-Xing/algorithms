from collections import deque
from collections import defaultdict

# check the questions here: https://www.geeksforgeeks.org/bottom-view-binary-tree/
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bottom_view(root):
    MIN, MAX = 0, 0
    if not root:
        return []
    ans = {}
    queue = deque()
    queue.append((root, 0))
    while queue:
        curr, i = queue.popleft()
        if curr:
            MIN = min(MIN, i)
            MAX = max(MAX, i)
            ans[i] = curr.val
            queue.append((curr.left, i - 1))
            queue.append((curr.right, i + 1))
    ret = []
    for i in range(MIN, MAX + 1):
        ret.append(ans[i])

    return ret


root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(5)
root.left.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(25)
root.left.right.right = Node(14)
root.right.left.left = Node(10)

print(bottom_view(root))

new_root = None
print(bottom_view(new_root))


# if need to print the left element when collsion happens
# or use above method, switch the append sequence, right first, then left
# at the end, because we use MIN and MAX to denote the output sequence from left to right
# so the output sequence didn't change
def bottom_view_with_height(root):
    if not root:
        return []
    ans = defaultdict(list)
    MIN, MAX = 0, 0
    queue = deque()
    # (node, vertical_distance, height)
    queue.append((root, 0, 1))
    while queue:
        curr, v, h = queue.popleft()
        if curr:
            MIN = min(MIN, v)
            MAX = max(MAX, v)
            ans[v].append((h, curr.val))
            queue.append((curr.left, v - 1, h + 1))
            queue.append((curr.right, v + 1, h + 1))
    ret = []
    for i in range(MIN, MAX + 1):
        # Last element in the list of that vertical, first number is the height
        last_level = ans[i][-1][0]
        for each in ans[i]:
            if last_level == each[0]:
                ret.append(each[1])
                break
    return ret


print(bottom_view_with_height(root))
