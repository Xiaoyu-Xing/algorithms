# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Iterative BFS
# Change the deque to stack will give DFS
from collections import deque


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        count = 0
        queue = deque()
        queue.append((root, 1))
        while queue:
            curr, i = queue.popleft()
            if curr:
                count = max(count, i)
                queue.append((curr.left, i + 1))
                queue.append((curr.right, i + 1))

        return count


# Recurrsive
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
