from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        centerIdx = len(nums) // 2
        root = TreeNode(nums[centerIdx])

        root.left = self.sortedArrayToBST(nums[:centerIdx])
        root.right = self.sortedArrayToBST(nums[centerIdx+1:])

        return root

        # Iterative solution
        stack = [(0, len(nums)-1, None, None)] # floor, ceiling, parent, direction
        root = None
        while stack:
            floor, ceiling, parent, direction = stack.pop()
            mid = (floor + ceiling) // 2
            node = TreeNode(nums[mid])
            if not root:
                root = node
            else:
                if direction == 'l':
                    parent.left = node
                elif direction == 'r':
                    parent.right = node
            
            if mid+1 <= ceiling:
                stack.append((mid+1, ceiling, node, 'r' ))
            if floor <= mid - 1:
                stack.append((floor, mid - 1, node, 'l'))
        return root


