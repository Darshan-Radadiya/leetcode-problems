from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        idx = 0
        q.append((root, idx))
        maxWidth = 0
        while q:
            n = len(q)
            minimumIdxOnCurrentLevel = q[0][1] 
            for i in range(n):
                node, idx = q.popleft()
                idx = idx - minimumIdxOnCurrentLevel  # subtracted to prevent integer overflow
                if i == 0:
                    leftIdx = idx
                if i == n - 1:
                    rightIdx = idx
                if node.left: q.append((node.left,(2*idx + 1)))
                if node.right: q.append((node.right,(2*idx + 2)))
                maxWidth = max(maxWidth, rightIdx - leftIdx + 1)
        return maxWidth
