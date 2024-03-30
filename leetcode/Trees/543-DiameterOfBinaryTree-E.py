from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Recursive Approach:
        diameter = 0
        
        def dfs(root):
            nonlocal diameter
            if not root: return 0
            leftHeight = self.dfs(root.left)
            rightHeight = self.dfs(root.right)
            diameter = max(diameter, leftHeight + rightHeight)
            return 1 + max(leftHeight, rightHeight)
        dfs(root)
        return diameter

        # Full dry run in notes.
        # Iterative approach:
        diameter = 0
        stack = [(root,False)]
        nodeHeight = {None:-1}
        while stack:
            currNode, isVisited = stack.pop()
            if currNode:
                if isVisited:
                    leftHeight = nodeHeight[currNode.left]
                    rightHeight = nodeHeight[currNode.right]
                    nodeHeight[currNode] = 1 + max(leftHeight, rightHeight)
                    diameter = max(diameter, 2 + leftHeight + rightHeight)
                else:
                    stack.append((currNode, True))
                    stack.append((currNode.right, False))
                    stack.append((currNode.left, False))
        return diameter
