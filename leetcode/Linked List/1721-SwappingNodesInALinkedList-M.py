# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
       # Move the fast pointer k nodes ahead of the head
        fast = head
        for _ in range(k):
            fast = fast.next

        # Now our fast will be k nodes ahead of the head
        slow = head
        prev_slow = None
        while fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next

        # Now we have our slow pointer at the kth node from the end of the LL.
        # Let's do swapping of nodes instead of values
        if prev_slow:
            temp = slow.next
            slow.next = head.next
            head.next = temp
            prev_slow.next = head
            head = slow
        else:
            temp = slow.next
            slow.next = head.next
            head.next = temp
            head = slow

        return head
