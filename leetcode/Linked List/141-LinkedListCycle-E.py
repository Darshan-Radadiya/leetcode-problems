# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        if not head or not head.next:
            return False

        left = head
        right = head.next

        while right and right.next:
            if left == right:
                return True
            left = left.next
            right = right.next.next

        return False