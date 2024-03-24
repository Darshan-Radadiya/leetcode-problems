from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root) -> bool:
       

        def valid(node,left,right):
            if not node:
                return True

            if not (node.val > right and node.val < left):
                return False
            
            return (valid(node.left,left,node.val) and valid(node.right,node.val,right))
        return valid(root, float("-inf"), float("inf"))
        
# Iterative:
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # we will set boundary on left and right.
        # left will be never less than (-infinity) 
        # right will be never greater than the (+infinity). 
        stack = [(root, float("-inf"), float("inf"))]
        while stack:
            node, leftBoundary, rightBoundary = stack.pop()
            if node.val <= leftBoundary or node.val >= rightBoundary:
                return False
            # if we go left side then we need to update the right boundary.
            # we will set rightBoundary as current node value AKA parent node.
            # vice versa for the right side.
            if node.left: stack.append((node.left,leftBoundary, node.val))
            if node.right: stack.append((node.right,node.val, rightBoundary))
        return True