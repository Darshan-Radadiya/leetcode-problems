from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if not node:
                # If we found a null node, all subsequent nodes should also be null.
                while q:
                    nullNode = q.popleft()
                    if nullNode:
                        return False
                return True
            
            q.append(node.left)
            q.append(node.right)
        return True