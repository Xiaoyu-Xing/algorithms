# DFS

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def convert(root):
            to_convert = []
            if root == None:
                to_convert.append('None')
            else:
                to_convert.append(str(root.val))
                to_convert.extend(convert(root.left))
                to_convert.extend(convert(root.right))
            return to_convert
        return ' '.join(convert(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def convert_back():
            next_node = to_convert.popleft()
            if next_node == 'None':
                return None
            new_node = TreeNode(int(next_node))
            new_node.left = convert_back()
            new_node.right = convert_back()
            return new_node

        to_convert = deque(data.split())
        return convert_back()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
