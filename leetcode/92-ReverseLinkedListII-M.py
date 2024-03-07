# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or not head.next or (left == 1 and right == 1):
            return head

        # first reach the left.
        dummy = ListNode(0, head)
        PL, curr = dummy, head
        for _ in range(left - 1):
            PL, curr = curr, curr.next
        
        # use simple reverse logic to reverse the r - l + 1 part of the LL.
        prev = None
        for _ in range( right - left + 1):
            tail = curr.next
            curr.next = prev
            prev = curr
            curr = tail
        
        # Update the pointers. that's it. 
        PL.next.next = curr
        PL.next = prev
        return dummy.next