class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # Initialize dummy nodes for smaller and larger lists
        dummy_smaller = ListNode(0)
        dummy_larger = ListNode(0)
        smaller_tail = dummy_smaller
        larger_tail = dummy_larger
        
        # Iterate through the original list
        curr = head
        while curr:
            if curr.val < x:
                smaller_tail.next = curr
                smaller_tail = smaller_tail.next
            else:
                larger_tail.next = curr
                larger_tail = larger_tail.next
            curr = curr.next
        
        # Link the end of the smaller list to the start of the larger list
        smaller_tail.next = dummy_larger.next
        
        # Terminate the end of the larger list to avoid cycle in the list. After appending all nodes larger than or equal to x,
        # the next pointer of the last node in the larger list (previously pointed to None) might still be pointing to a node in the original list.
        # and if it is pointing to node form the list then this node will be present in the smaller list so it will create a cycle.
        larger_tail.next = None
        
        # Return the combined partitioned list
        return dummy_smaller.next
