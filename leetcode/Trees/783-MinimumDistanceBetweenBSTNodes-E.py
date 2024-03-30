from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int: 
    #    Iterative
        prev = None
        res = float("inf")
        curr = root
        s = []
        while s or curr:
            while curr:
                s.append(curr)
                curr = curr.left
            curr = s.pop()
            if prev:
                res = min(res, curr.val - prev.val)
            prev = curr
            curr = curr.right
        return res
    
    # Recursive
        res, prev = float("inf"), None
        def inorder(root):
            nonlocal prev, res
            if not root:
                return root
            inorder(root.left)
            if prev:
                res = min(res, root.val- prev.val)
            prev = root
            inorder(root.right)
        inorder(root)
        return res