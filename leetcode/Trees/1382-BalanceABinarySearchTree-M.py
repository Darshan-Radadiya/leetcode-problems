# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # get the sorted array for the given BST
        # To get the sorted Array we can use the In Order Traversal. 
        # Left - Root - Right
        def inorderTraversal(root):
            curr = root
            stack = []
            res = []
            while curr or stack:
                while curr:
                    stack.append(curr)
                    curr = curr.left
                curr = stack.pop()
                res.append(curr.val)
                curr = curr.right
            return res

        def createBST(start, end):
            if start > end:
                return None
            mid = start + ((end-start) // 2)

            left = createBST(start, mid-1)
            right = createBST(mid+1, end)
            node = TreeNode(sortedArr[mid], left, right)
            return node

        sortedArr = inorderTraversal(root)
        return createBST(0, len(sortedArr) - 1)

