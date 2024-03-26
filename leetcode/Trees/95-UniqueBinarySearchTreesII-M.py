from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateAllPossibleBST(self, left, right, memo):
        res = []
        if left > right:
            res.append(None)
        if (left, right) in memo:
            return memo[(left, right)]
        
        for i in range(left, right + 1):
            leftSubTrees = self.generateAllPossibleBST(left, i - 1, memo)
            rightSubTrees = self.generateAllPossibleBST(i + 1, right, memo)

            for leftTree in leftSubTrees:
                for rightTree in rightSubTrees:
                    root = TreeNode(i, leftTree, rightTree)
                    res.append(root)
        memo[(left, right)] = res
        return res

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}
        return self.generateAllPossibleBST(1, n, memo)