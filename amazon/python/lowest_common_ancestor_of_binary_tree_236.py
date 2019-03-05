# Method 1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(node):
            if not node:
                return False
            left = find(node.left)
            right = find(node.right)
            found = node == q or node == p
            if left + right + found >= 2:
                self.ans = node
            return found or left or right
        find(root)
        return self.ans


# Method 2:
class Solution:

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Stack for tree traversal
        stack = [root]
        # Dictionary for parent pointers
        parent = {root: None}
        # Iterate until we find both the nodes p and q
        while p not in parent or q not in parent:
            node = stack.pop()
            # While traversing the tree, keep saving the parent pointers.
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        # Ancestors set() for node p.
        ancestors = set()
        # Process all ancestors for node p using parent pointers.
        while p:
            ancestors.add(p)
            p = parent[p]
        # The first ancestor of q which appears in
        # p's ancestor set() is their lowest common ancestor.
        while q not in ancestors:
            q = parent[q]
        return q
