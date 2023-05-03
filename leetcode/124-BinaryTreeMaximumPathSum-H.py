# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root) -> int:

        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            
            leftChild = dfs(root.left)
            rightChild = dfs(root.right)
            leftMaxChild = max(leftChild,0)
            rightMaxChild = max(rightChild,0)

            res[0] = max(res[0], root.val+leftMaxChild+rightMaxChild)
            return root.val + max(leftMaxChild,rightMaxChild)
        dfs(root)
        return res[0]

