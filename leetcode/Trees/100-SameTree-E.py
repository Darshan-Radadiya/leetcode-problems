# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p,q):
    ##### Recursive #####
        if not p and not q: 
            return True
        if not p or not q: 
            return False

        return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    ##### Iterative #####
        stack = [(p, q)]
        while stack:
            pNode, qNode = stack.pop()
            if not pNode and not qNode:
                continue
            if not qNode or not pNode or pNode.val != qNode.val:
                return False
            stack.append((pNode.left,qNode.left)) 
            stack.append((pNode.right,qNode.right)) 
        return True