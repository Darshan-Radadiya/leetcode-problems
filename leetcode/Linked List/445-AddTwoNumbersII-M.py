# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # one way to solve this problem is by reversing both the LL and then performing the sum as add number 1.
        # but ask is to do it without reversing a LL.
        # So, the another approach is to use a stack to store the elements of both the LL
        # then pop from the top of the stack and perform the summation and create a new res node.
        def createStack(head):
            s = []
            while head:
                s.append(head.val)
                head = head.next
            return s

        s1 = createStack(l1)  
        s2 = createStack(l2)  
        summation = 0
        carry = 0
        res = None
        while s1 or s2 or carry:
            n1 = s1.pop() if s1 else 0
            n2 = s2.pop() if s2 else 0
            summation = (n1 + n2 + carry) % 10
            carry = (n1 + n2 + carry) // 10
            head = ListNode(summation)
            head.next = res
            res = head
        return res