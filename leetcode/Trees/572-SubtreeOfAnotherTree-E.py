from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isSubtree(self, s, t):

        if not s:
            return False
        if not t:
            return True
        if self.sameTree(s,t):
            return True
        return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)

    def sameTree(self, s,t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return self.sameTree(s.left,t.left) and self.sameTree(s.right,t.right)
        return False
    
    # Same approach different version

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        isSubTree = False
        if not subRoot:
            return True
        if not root:
            return False
        if root.val == subRoot.val:
            if self.sameTree(root, subRoot): return True

        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
         

    def sameTree(self, tree1, tree2):
        if not tree1 and not tree2:
            return True
        if not tree1 or not tree2:
            return False
        return (tree1.val == tree2.val) and self.sameTree(tree1.left,tree2.left) and self.sameTree(tree1.right,tree2.right)
        
        