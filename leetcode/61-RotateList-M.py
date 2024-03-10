from typing import Optional 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head and not head.next:
            return head

        #  find the len of the LL.
        temp = head
        n = 1
        while temp:
            temp = temp.next
            n += 1
            
        # adjust k to avoid repeated rotation when k > n.
        k = k % n
        # if k == 0 mean no rotation needed.
        if k == 0:
            return head
        
        # move fast pointer k points ahead in the list.
        fast = head
        while fast:
            fast = fast.next
        
        # move slow and fast pointer together now till fast reach lastNode.
        slow = head
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # now we will rearrange the pointers.
        new_head = slow.next
        slow.next = None
        fast.next = head

        return new_head  
        