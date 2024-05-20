from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # Iterative 
        # Time and Space is O(n) 
        # root = TreeNode(preorder[0])
        # s = [root]
        # for i in range(1,len(preorder)):
        #     node, child = s[-1],TreeNode(preorder[i])
        #     while s and s[-1].val < child.val:
        #         node = s.pop()
        #     if node.val < child.val:
        #         node.right = child
        #     else:
        #         node.left = child
        #     s.append(childO
        # return root

        # recursive
        # Time and Space is O(n)
        def builder(lowerBound, upperBound):
            nonlocal i
            if i == len(preorder):
                return None
            val = preorder[i]
            if val < lowerBound or val > upperBound:
                return None
            i += 1
            root = TreeNode(val)
            root.left = builder(lowerBound,val)
            root.right = builder(val,upperBound)
            return root

        i = 0
        return builder(float('-inf'),float('inf'))
