from typing import Optional
# Definition for a binary tree node.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        # --------Iterative-------
        # ------------------------
        # newNode = TreeNode(val)
        # if not root: return newNode
        # curr = root
        # tail = None
        # # Find the correct spot for the new node.
        # while curr:
        #     tail = curr
        #     if val < curr.val:
        #         curr = curr.left
        #     else:
        #         curr = curr.right
        # # Found the correct spot now add new node here.
        # if val < tail.val:
        #     tail.left = newNode
        # else:
        #     tail.right = newNode
        # return root

        # -------Recursive-------
        # -----------------------
        if not root: return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left,val)
        else:
            root.right = self.insertIntoBST(root.right,val)
        return root

        # --------2nd flavour -------
        # --------of Iterator--------
        # def insert(root, val):
        #     newNode = TreeNode(val)
        #     if not root: return newNode
        #     curr = root
        #     # Find the correct spot for the new node.
        #     while curr:
        #         if val < curr.val:
        #             if not curr.left:
        #                 curr.left = newNode
        #                 break
        #             curr = curr.left
        #         else:
        #             if not curr.right:
        #                 curr.right = newNode
        #                 break
        #             curr = curr.right
        #     return root