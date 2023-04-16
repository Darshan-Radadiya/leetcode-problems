# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root):
        # recursive DFS approach

        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
        
    # Iterative DFS approach:

    def maxDepth(self, root):

        if not root:
            return 0
        res = 0
        stack = [[root,1]]

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(depth,res)
                stack.append([node.left,depth + 1])
                stack.append([node.right,depth + 1])
        return res

#BFS
    def maxDepth(self, root: TreeNode) -> int:
        q = deque()
        if root:
            q.append(root)

        level = 0

        while q:

            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level