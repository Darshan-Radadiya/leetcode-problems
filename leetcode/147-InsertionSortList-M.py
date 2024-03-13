from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        curr = head.next
        prev = head
        dummy = ListNode(0, head)
        while curr:
            if curr.val > prev.val:
                prev = curr
                curr = curr.next
                continue
            
            temp = dummy # bcs we will check from starting for node value temp.next.val below is first node in sorted list. 
            while curr.val > temp.next.val:
                temp = temp.next

            prev.next = curr.next
            curr.next = temp.next
            temp.next = curr
            curr = prev.next

        return dummy.next

