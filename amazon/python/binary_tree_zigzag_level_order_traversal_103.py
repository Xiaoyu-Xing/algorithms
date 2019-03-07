# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# My method: by flag to indicate append left child first or not
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        q1, q2 = [root], []
        flag = 1
        while q1 or q2:
            ans.append([])
            while q1:
                curr = q1.pop()
                ans[-1].append(curr.val)
                if flag < 0:
                    if curr.right:
                        q2.append(curr.right)
                    if curr.left:
                        q2.append(curr.left)
                else:
                    if curr.left:
                        q2.append(curr.left)
                    if curr.right:
                        q2.append(curr.right)
            q1, q2 = q2, q1
            flag *= -1
        return ans


# Reference: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/discuss/33834/Python-simple-BFS
# Normal BFS, just flip the output based on the flag
def zigzagLevelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
        return []
    res, temp, stack, flag = [], [], [root], 1
    while stack:
        for i in range(len(stack)):
            node = stack.pop(0)
            temp += [node.val]
            if node.left:
                stack += [node.left]
            if node.right:
                stack += [node.right]
        res += [temp[::flag]]
        temp = []
        flag *= -1
    return res
