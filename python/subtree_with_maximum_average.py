# Post order traversal and divide and conquer, O(n) time, O(logn) space for recursion

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    max_avg = float('-inf')
    node = None

    def max_avg_subtree(self, root):
        if root is None:
            return None
        self.recurse_find(root)
        return self.node

    def recurse_find(self, node):
        if node is None:
            return 0, 0
        left_sum, left_node_count = self.recurse_find(node.left)
        right_sum, right_node_count = self.recurse_find(node.right)
        curr_sum = left_sum + right_sum + node.val
        curr_node_count = left_node_count + right_node_count + 1
        curr_avg = curr_sum * 1.0 / curr_node_count
        if self.node is None or curr_avg > self.max_avg:
            self.node = node
            self.max_avg = curr_avg
        return curr_sum, curr_node_count
