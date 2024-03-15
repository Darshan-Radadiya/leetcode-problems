# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # check is there is a cycle.
            if slow == fast:
                start = head
                # now we need to find the starting point of the cycle.
                while slow != start:
                    start = start.next
                    slow = slow.next
                return slow
        return None
