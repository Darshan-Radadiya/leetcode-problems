# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        # finding middle ele (Slow pointer)
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse the LL from middle point 
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        # check for the palindrom
        while prev:
            if head.val != prev.val:
                return False
            head= head.next
            prev = prev.next
        return True

#  Time complexity = O(n)
#  Space Complexity = O(1)