from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # Iterative
        stack = [(root, -1, None)]
        while stack:
            node, parent, isRightChild = stack.pop()
            # node is lower than our lower bound.
            if node.val < low:
                if parent == -1:
                    root = node.right
                    if node.right: stack.append((node.right, parent, True))
                    continue
                if isRightChild:
                    parent.right = node.right
                else:
                    parent.left = node.right
                if node.right: stack.append((node.right, parent, isRightChild))
            
            # node is higher than our upper bound.
            elif node.val > high:
                if parent == -1:
                    root = node.left
                    if node.left: stack.append((node.left, parent, False))
                    continue
                if isRightChild:
                    parent.right = node.left
                else:
                    parent.left = node.left
                if node.left: stack.append((node.left, parent, isRightChild))
            
            # node is within the range.
            else:
                if node.left:stack.append((node.left, node, False))
                if node.right:stack.append((node.right, node, True))
        return root
                
        # recursive
        if not root:
            return None
        
        if root.val > high:
            return self.trimBST(root.left, low, high)

        if root.val < low:
            return self.trimBST(root.right, low, high)

        else:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root
# LeetCode solution link:- https://leetcode.com/problems/trim-a-binary-search-tree/solutions/4936676/beginner-friendly-dfs-iterative-approach-beats-94-runtime/
            




                    