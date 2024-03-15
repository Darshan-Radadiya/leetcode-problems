# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        O, E = head, head.next

        tempEven = E
        while E and E.next:
            O.next = O.next.next
            E.next = E.next.next
            O = O.next
            E = E.next
            
        O.next = tempEven
        return head