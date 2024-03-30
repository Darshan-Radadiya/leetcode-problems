class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
    

class Solution:
    def postOrderTraversal(self, root):

        # Iterative approach
        # 
        if not root:
            return
        stack = [root]
        visited = [False]
        res = []
        while stack:
            curr, isVisited = stack.pop(), visited.pop()
            if curr:
                if isVisited:
                    res.append(curr.val)
                else:
                    stack.append(curr)
                    visited.append(True)
                    stack.append(curr.right)
                    visited.append(False)
                    stack.append(curr.left)
                    visited.append(False)
        return res
        
        #  Recursive
        #
        return self.preorderTraversal(root.left) + self.preorderTraversal(root.right) + [root.val] if root else []