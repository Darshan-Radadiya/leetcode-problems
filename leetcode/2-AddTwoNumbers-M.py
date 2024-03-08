# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        resHead = ListNode(0)
        res = resHead
        carry = 0
        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            _sum = (a + b + carry) % 10
            carry = (a + b + carry) // 10
            res.next = ListNode(_sum)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            res = res.next

        return resHead.next

