from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return False
        total = 0
        stack = [(root, root.val)]
        while stack:
            node, currSum = stack.pop()

            if not node.left and not node.right:
                total = total + currSum
            
            if node.left:
                stack.append((node.left, (currSum) * 10 + node.left.val))
            if node.right:
                stack.append((node.right, (currSum) * 10 + node.right.val))

        return total

# Time O(n)