from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}
        def generate_trees(num):
            if num % 2 == 0:
                return []
            if num == 1:
                return [TreeNode()]
            if num in memo:
                return memo[num]
            res = []
            for i in range(1, num, 2):
                left = generate_trees(i)
                right = generate_trees(num - i - 1)

                for nodeL in left:
                    for nodeR in right:
                        root = TreeNode(0, nodeL, nodeR)
                        res.append(root)
            memo[num] = res
            return res
        
        return generate_trees(n)

n = 7
ExpectedOutput = [[0,0,0,None,None,0,0,None,None,0,0],[0,0,0,None,None,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,None,None,None,None,0,0],[0,0,0,0,0,None,None,0,0]]
print("Time Complexity is: O(n)\n" )
