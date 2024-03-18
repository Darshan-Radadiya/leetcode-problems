# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root):
        # Both the approaches are same as the traversal of the tree in DFS manner. 
        # Recursive solution
        #  
        if not root:
            return None
        
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
    
    # Iterative Solution 
    # 
        if not root:
            return root
        s = [root]
        while s:
            currNode = s.pop()
            temp = currNode.left
            currNode.left = currNode.right
            currNode.right = temp
            if currNode.left:   s.append(currNode.left)
            if currNode.right:   s.append(currNode.right)
        return root