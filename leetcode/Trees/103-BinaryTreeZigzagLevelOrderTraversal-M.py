from typing import Optional, List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        res = []
        q = deque()
        q.append(root)
        while q:
            level = []
            n = len(q)
            for i in range(n):
                if len(res) % 2 != 0:
                    node = q.pop()
                    if node.right:
                        q.appendleft(node.right) 
                    if node.left:
                        q.appendleft(node.left)
                else:
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                level.append(node.val)
            res.append(level)
        return res
        
        # Or else we can simply append left in level array if current level is odd.
        if not root:
            return root
        res = []
        q = deque()
        q.append(root)
        while q:
            level = deque()
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if len(res) % 2 != 0:
                    level.appendleft(node.val)
                else:
                    level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res
            