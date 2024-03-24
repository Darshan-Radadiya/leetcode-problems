from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
       
        # O(n) Time Complexity
        # Stored the index in hashMap for O(1) lookup.
        if not inorder:
            return None
        inorderIndexMap = {val:i for i, val in enumerate(inorder)}

        def buildSubTree(left, right):
            if left > right:
                return None
            root = TreeNode(postorder.pop())
            idx = inorderIndexMap[root.val]

            root.right = buildSubTree(idx + 1, right) 
            root.left = buildSubTree(left, idx - 1) 
            return root
        return buildSubTree(0, len(postorder) - 1)
       
        # O(n^2) Time Complexity
        #  because we are checking index in each recursive call.
        if not inorder or not postorder:
            return None
        
        root = TreeNode(postorder.pop())
        mid = inorder.index(root.val)
        root.right = self.buildTree(inorder[mid+1:], postorder)
        root.left = self.buildTree(inorder[:mid], postorder)
        
        return root