from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #### Iterative #### same as finding diameter of tree just one line change.
        stack = [(root,False)]
        nodeHeight = {None:-1}
        while stack:
            currNode, isVisited = stack.pop()
            if currNode:
                if isVisited:
                    leftHeight = nodeHeight[currNode.left]
                    rightHeight = nodeHeight[currNode.right]
                    if abs(leftHeight - rightHeight) > 1:
                        return False
                    nodeHeight[currNode] = 1 + max(leftHeight, rightHeight)
                else:
                    stack.append((currNode, True))
                    if currNode.right: stack.append((currNode.right, False))
                    if currNode.left: stack.append((currNode.left, False))
        return True


    ##### Recursive #####
        return self.dfs(root) != -1
    def dfs(self, root):
        if not root:
            return 0
        leftHeight = self.dfs(root.left)
        rightHeight = self.dfs(root.right)
        diff = abs(leftHeight-rightHeight)
        if leftHeight == -1  or rightHeight == -1 or diff > 1:
            return -1
        return 1 + max(leftHeight, rightHeight)