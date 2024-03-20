from typing import Optional, List
# Definition for a binary tree node.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative solution
        if not root:
            return
        stack = []
        res = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res

        
        # Two different way for recursive.    
        def inorder(root,res):
            if not root:
                return
            inorder(root.left,res)
            res.append(root.val)
            inorder(root.right,res)
            
        res = []
        inorder(root,res)
        return res
        
        # if not root:
        #     return None
        # return [root.val, self.inorderTraversal(root.left), self.inorderTraversal(root.right)]
        