from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        res = []
        def dfs(node):
            if not node:
                res.append("N")
                return 
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        self.i = 0
        def dfs():
            if data[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(data[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# ITERATIVE TRAVERSAL
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
        encodedStr = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node: 
                encodedStr.append(str(node.val))
                q.append(node.left)
                q.append(node.right) 
            else:
                encodedStr.append("N")
        return ",".join(encodedStr)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        data = data.split(",")
        tree = deque(data)
        root = TreeNode(int(tree.popleft()))
        q = deque([root])
        
        while q:
            node = q.popleft()
            leftChild = tree.popleft()
            if leftChild != "N":
                node.left = TreeNode(int(leftChild))
                q.append(node.left)
            rightChild = tree.popleft()
            if rightChild != "N":
                node.right = TreeNode(int(rightChild))
                q.append(node.right)
            
        return root

        

#        8
#      /   \
#     3     10
#    / \    / \
#   1   6   N 14
#  / \ / \    / \
# N  N 4  7  13  N

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans