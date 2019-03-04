from collections import deque
from collections import defaultdict


def verticalOrder(root):
    if not root:
        return []
    ans = defaultdict(list)
    # Has to be BFS, because the output list for each needs to be from top to bottom
    queue = deque()
    queue.append((root, 0))
    MIN, MAX = 0, 0
    while queue:
        node, i = queue.popleft()
        if node:
                # MIN MAX to know the range of dictionary keys, so no sorting needed.
            MIN = min(MIN, i)
            MAX = max(MAX, i)
            ans[i].append(node.val)
            # Left first, then right, because the order need to be from left to right
            queue.append((node.left, i - 1))
            queue.append((node.right, i + 1))

    ret = []
    for i in range(MIN, MAX + 1):
        ret.append(ans[i])
    return ret
