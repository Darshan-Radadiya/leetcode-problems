# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from typing import Optional

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        curr, nxt = root, root.left if root else None
        while curr and nxt:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
            curr = curr.next
            if not curr:
                curr = nxt
                nxt = curr.left
        return root

        # with extra space O(n) for queue:
        if not root:
            return
        q = deque()
        q.append(root)
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if i < n - 1:
                    node.next = q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
    
Input =[1,2,3,4,5,6,7]
# Output = [1,#,2,3,#,4,5,6,7,#]
# 1st Time and Space complexity is O(n) and O(1) respectively.
# 2nd Time and Space complexity is O(n) and O(n) respectively.
# Recommended to check problem  117 which is follow up of this problem.