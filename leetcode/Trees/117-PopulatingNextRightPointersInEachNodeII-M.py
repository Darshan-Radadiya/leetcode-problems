from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
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
    
        # Without extra space.
        # We will set one extra dummy node at the start of the each level.
        # and will update this dummy node's next pointer based on the current node's left
        # or right child and once we done with current level.
        # we will set the curr to the dummy.next that will contains all the nodes for the nxt level.
        # O(1) extra space. O(n) time.   
        if not root:
            return 
        curr = root
        while curr:
            dummy = Node(0)
            temp = dummy
            while curr:
                if curr.left:
                    temp.next = curr.left
                    temp = temp.next
                if curr.right:
                    temp.next = curr.right
                    temp = temp.next
                curr = curr.next
            curr = dummy.next
        return root
 
# This is a follow up of the question 116. Where we have a perfect binary tree.
# Approach one of this problem will work for 116 and 117 both but with extra space.

            
                