from typing import Optional, List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Space and time complexity is O(n).
        if not root:
            return root
        q = deque()
        q.append(root)
        res = []
        while q:
            rightSide = None
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res
        
        # Space will be O(h) and time O(n)
        def reversePreorder(node, currLevel):
            if not node:
                return 
            if len(rightSideView) == currLevel:
                rightSideView.append(node.val)
            
            if node.right: 
                reversePreorder(node.right, currLevel + 1)
            if node.left: 
                reversePreorder(node.left, currLevel + 1)
        rightSideView = []
        reversePreorder(root, 0)
        return rightSideView
                


            