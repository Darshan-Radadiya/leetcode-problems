# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        current = root

        while True:
            while current is not None:
                stack.append(current)
                current = current.left
            
            if not stack:
                break
                
            node = stack.pop()
            k -= 1
            
            if k == 0:
                return node.val
            
            current = node.right