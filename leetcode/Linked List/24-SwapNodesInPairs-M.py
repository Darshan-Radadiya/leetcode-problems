# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        curr = head
        prev = dummy

        while curr and curr.next:
            # save ptrs.
            nextPairPtr = curr.next.next
            secondNode = curr.next

            # swap the nodes
            secondNode.next = curr
            curr.next = nextPairPtr
            prev.next = secondNode

            # update prev and curr ptrs.
            prev = curr
            curr = nextPairPtr
            
        return dummy.next