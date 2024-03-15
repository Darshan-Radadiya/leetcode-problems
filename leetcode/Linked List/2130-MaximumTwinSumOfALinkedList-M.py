# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: ListNode) -> int:
        slow, fast = head, head 
        # find middle point
        while fast.next.next:
            slow = slow.next
            fast = fast.next.next
        fast = fast.next
        slow = slow.next

        # reverse the list from middle point
        prev = None
        curr = slow
        while curr:
            tail = curr.next
            curr.next = prev
            prev = curr
            curr = tail
        
        # we have reversed list in prev
        res = 0
        front = head
        while prev:
            currSum = prev.val + front.val
            res = max(currSum, res)
            front = front.next
            prev = prev.next
        return res

