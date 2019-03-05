# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def LCA(root, p, q):
    if p.val < root.val and q.val < root.val:
        return LCA(root.left, p, q)
    elif p.val > root.val and q.val > root.val:
        return LCA(root.right, p, q)
    else:
        return root


def LCA_ite(root, p, q):
    curr = root
    while curr:
        if p.val < curr.val and q.val < curr.val:
            curr = curr.left
        elif p.val > curr.val and q.val > curr.val:
            curr = curr.right
        else:
            return curr
