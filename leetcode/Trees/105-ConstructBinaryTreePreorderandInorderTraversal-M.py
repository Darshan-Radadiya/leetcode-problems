# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder , inorder):
        
        # O(n) Time Complexity
        # Stored the index in hashMap for O(1) lookup.
        def buildSubTree(left, right):
            nonlocal position
            if left > right:
                return None
            root = TreeNode(preorder[position])
            position += 1
            mid = inorderIndexMap[root.val]
            root.left = buildSubTree(left, mid-1)
            root.right = buildSubTree(mid + 1, right)
            return root
        if not preorder:
            return None
        position = 0
        inorderIndexMap = { val:i for i, val in enumerate(inorder)}
        return buildSubTree(0, len(preorder) - 1)
    
        # O(n^2) Time Complexity
        #  because we are checking index in each recursive call.
        if not inorder or not preorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        
        return root