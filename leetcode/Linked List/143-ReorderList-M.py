# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # finding mid point
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reversing second half 
        second_portion = slow.next
        prev = slow.next = None
        while second_portion:
            temp = second_portion.next
            second_portion.next = prev
            prev = second_portion
            second_portion = temp
            
        #merging the two half's in one
        first_half, second_half = head, prev
        while second_half:
            temp1, temp2 = first_half.next, second_half.next
            first_half.next = second_half
            second_half.next = temp1
            first_half, second_half = temp1, temp2
        
