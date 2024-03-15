# Definition for singly-linked list.
from typing import Optional  # If you're using Python 3.9+, you can directly use list or dict as optional types without importing from typing

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
        
    # Helper function to find mid 
    def getMid(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Merging both list
    def merge(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        if l1:
            curr.next = l1
        if l2:
            curr.next = l2

        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # we will do merge sort here because merger sort is best fit for linked list problem
        # compare to the heap sort. 

        # handling edge cases.
        if not head or not head.next:
            return head

        # start the merge sort.
        # find the mid point and disconnect the LL from mid point.

        mid = self.getMid(head)
        leftHead = head
        rightHead = mid.next
        mid.next = None  # Split the list into two halves

        left = self.sortList(leftHead)
        right = self.sortList(rightHead)

        return self.merge(left, right)
    

print("Time Complexity is O(n lon n) and space O(1) logically its O(n) space but LL don't consider the space that internal stack uses during recursive calls.")


      




