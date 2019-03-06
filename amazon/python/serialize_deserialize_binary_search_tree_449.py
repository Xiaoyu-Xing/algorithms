# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Similar to 297
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def encode(root):
            val = []
            if not root:
                val.append('None')
            else:
                val.append(str(root.val))
                val.extend(encode(root.left))
                val.extend(encode(root.right))
            return val
        
        return ' '.join(encode(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def decode():
            node = data.popleft()
            if node == 'None':
                return None
            root = TreeNode(int(node))
            root.left = decode()
            root.right = decode()
            return root
        data = collections.deque(data.split())
        return decode()
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))



# Or if not using None as the indicator of end of left or right subtree, 
# use min and max by the property of BST
# https://leetcode.com/problems/serialize-and-deserialize-bst/discuss/93171/Python-O(-N-)-solution.-easy-to-understand
class Codec:

    def serialize(self, root):
        vals = []

        def preOrder(node):
            if node:
                vals.append(node.val)
                preOrder(node.left)
                preOrder(node.right)

        preOrder(root)

        return ' '.join(map(str, vals))

    # O( N ) since each val run build once
    def deserialize(self, data):
        vals = collections.deque(int(val) for val in data.split())
        # min max value here to constraint the tree growth, if not follows the 
        # pattern of BST, it means it reaches the bottom, so return
        def build(minVal, maxVal):
            if vals and minVal < vals[0] < maxVal:
                val = vals.popleft()
                node = TreeNode(val)
                node.left = build(minVal, val)
                node.right = build(val, maxVal)
                return node

        return build(float('-infinity'), float('infinity'))