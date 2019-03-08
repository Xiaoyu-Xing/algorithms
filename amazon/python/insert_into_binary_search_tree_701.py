# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Recurrsive
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root


# Iterative

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        curr = root
        prev = None
        while curr:
            if val < curr.val:
                prev = curr
                curr = curr.left
            else:
                prev = curr
                curr = curr.right
        if prev.val < val:
            prev.right = TreeNode(val)
        else:
            prev.left = TreeNode(val)
        return root
