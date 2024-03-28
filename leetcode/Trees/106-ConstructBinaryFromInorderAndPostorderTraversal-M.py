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
            # Right subtree is built first because examining the postorder traversal allows us to determine the root, 
            # left subtree, and right subtree in that order. Postorder traversal ensures that the root node is visited last. 
            # By utilizing the in-order traversal alongside the postorder traversal, crucial information about the binary tree's
            # structure can be inferred. The in-order traversal indicates the sequence of nodes visited when traversing the 
            # left subtree, root node, and right subtree. Since the root node is always the last node visited in postorder 
            # traversal, this information is utilized to determine where the right subtree begins and where the left subtree ends.
            #  Therefore, constructing the right subtree first simplifies the process and ensures accurate reconstruction of the 
            # binary tree from its inorder and postorder traversals.
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