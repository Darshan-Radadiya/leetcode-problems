from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> list[Optional[ListNode]]:
        n = 1
        curr = head
        while curr:
            curr = curr.next
            n += 1
        
        q = n // k
        r = n % k

        curr = head
        groups = []
        for i in range(k):
            grpSize = q
            if r > 1:
                grpSize += 1
                r -= 1
            t = currGrp = ListNode(0)
            while curr and grpSize:
                currGrp.next = ListNode(curr.val)
                currGrp = currGrp.next
                curr = curr.next
                grpSize -= 1
            groups.append(t.next)
        return groups