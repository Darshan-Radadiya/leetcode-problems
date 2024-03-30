from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # Iterative
        # 
        if not root:
            return
        curr = root
        stack = []
        res = []
        while stack or curr:
            if curr:
                res.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()
        return res
        # Recursive
        #
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []