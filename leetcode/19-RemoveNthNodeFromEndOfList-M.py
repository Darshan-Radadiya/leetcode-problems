# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # BRUTE FORCE SOLUTION WITH TWO PASSES OVER THE LL ITS WORKING BUT WE WANT SINGLE PASS SOLUTION.
#         length = 0
#         curr = head
#         while curr:
#             length += 1
#             curr = curr.next

#         diff = length - n
#         if diff == 0:
#             return head.next

#         prev = None
#         idx = 0
#         curr = head
#         while curr:
#             if idx == diff:
#                 prev.next = curr.next
#                 return head
#             prev = curr
#             curr = curr.next
#             idx += 1
#         return None

#         NOW, WHEN WE THINK ABOUT THE OPTIMIZATION WE CAN USE FAST AND SLOW POINTER APPROACH.
#         ONLY THING WE NEED TO TAKE CARE IS WE NEED TO SET THE FAST POINTER N NODES AHEAD OF THE SLOW.
#         SO, WHEN SLOW FAST REACHES THE LAST NODE OF THE LL SLOW WILL BE AT LEN(LL) - N TH NODE.
#         TIME COMPLEXITY IS O(N) and SPACE IS O(1).
        
        slow = head
        fast = head
        for _ in range(n):
            fast = fast.next
            
        if fast is None:
            return head.next
    
        while fast.next:
            slow = slow.next
            fast = fast.next
        if slow and slow.next:
            slow.next = slow.next.next
        return head
