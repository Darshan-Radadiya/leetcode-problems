from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # recursive recommended. 
        def dfs(root):
            if not root:
                return [(0,0)]
            leftPair = dfs(root.left)
            rightPair = dfs(root.right)
            withRoot = root.val + leftPair[0][1] + rightPair[0][1]
            withoutRoot = max(leftPair[0]) + max(rightPair[0])
            return [(withRoot, withoutRoot)]
        return max(dfs(root)[0])

        # Iterative
        stack = [root]
        pairs = []
        visited = set()
        while stack:
            node = stack.pop()
            if node:
                if node in visited:
                    leftPair = pairs.pop()
                    rightPair = pairs.pop()
                    withRoot = node.val + leftPair[1] + rightPair[1]
                    withoutRoot = max(leftPair) + max(rightPair)
                    pairs.append([withRoot, withoutRoot])
                else:
                    stack.extend([node, node.right, node.left])
                    visited.add(node)
            else:
                pairs.append([0,0]) 
        return max(pairs.pop())