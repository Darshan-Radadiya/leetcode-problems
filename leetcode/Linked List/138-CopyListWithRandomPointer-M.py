# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Node) -> Node:
        # brute force approach will use O(n) extra space for hash map but it is working tho.
        # Step 1 create a hash map
        originalToCopy = {None: None}
        curr = head
        while curr:
            originalToCopy[curr] = Node(curr.val)
            curr = curr.next
        
        # step 2 assign pointers by taking ref from hash map
        curr = head
        while curr:
            originalToCopy[curr].next = originalToCopy[curr.next]
            originalToCopy[curr].random = originalToCopy[curr.random]
            curr = curr.next
        return originalToCopy[head]


        # Optimized way, we can remove extra O(n) space by eliminating need of hashmap
        # its is three pass process

        # First Pass: - we will create a copy node after the original node and 
        # for example :- 7 --> 7' --> 13 --> 13' --> 11 --> 11'

        curr = head
        while curr:
            copyNode = Node(curr.val)
            copyNode.next = curr.next
            curr.next = copyNode
            curr = copyNode.next
        
        # Second pass: - we will create a link for the random pointer.
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # Third pass: - we will break the next link and separate both the lists.
        curr = head
        dummy = Node(0) # To keep ref to copy list head.
        copyListCurr = dummy
        starter = None
        while curr:
            starter = curr.next.next
            copyListCurr.next = curr.next
            curr.next = starter
            copyListCurr = copyListCurr.next
            curr = starter

        return dummy.next

