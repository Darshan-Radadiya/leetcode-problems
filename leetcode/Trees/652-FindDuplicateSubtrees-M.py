from typing import Optional, List
from collections import defaultdict
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subTreeStringMap = defaultdict(int)

        def dfs(root):
            if not root: return "None"

            # inorder
            # subTreeString = ",".join(["l", dfs(root.left), str(root.val), dfs(root.right), "r"])
            
            # PreOrder
            # subTreeString = ",".join([str(root.val), dfs(root.left), dfs(root.right)])
            
            # PostOrder
            subTreeString = ",".join([dfs(root.left), dfs(root.right), str(root.val)])
            
            if subTreeStringMap[subTreeString] == 1:
                res.append(root)
            subTreeStringMap[subTreeString] += 1
            return subTreeString
        
        res = []
        dfs(root)
        return res