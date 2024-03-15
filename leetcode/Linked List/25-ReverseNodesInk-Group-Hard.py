from typing import Optional
class ListNode():
    def __init__(self,val, next):
        self.val = val
        self.next = None

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        

        dummy = ListNode(0, head)
        prevGrpEnd = dummy
        # 0 - 1 - 2 - 3 - 4 - 5
        # ^
        #  prevGrpEnd
        
        while head:
            # Check if there's enough nodes left to reverse
            count = 0
            curr = head
            while curr and count < k:
                curr = curr.next
                count += 1
            if count < k:
                break

            # 1 - 2 - 3 - 4 - 5
            #     |
            #     curr

            # reverse the ele till curr.
            prev = None
            curr = head
            for _ in range(k):
                tail = curr.next
                curr.next = prev
                prev = curr
                curr = tail
            
            # 2 - 1 - None      - 3 - 4 - 5
            # |    
            # prev
                
            #  Connect the end of the last reversed group to the current reversed head
            # 0 - 2 - 1 - None      - 3 - 4 - 5
            # |       |-> head        | -> curr
            # |   |-> prev
            # prevGrpEnd
            prevGrpEnd.next = prev

            # Connect the end of the current reversed group to the remaining list
            # 0 - 2 - 1 - 3 - 4 - 5
            #             |-> curr
            #         |-> head  
            #     |-> prev
            # 
            head.next = curr

            # Move the pointers forward
            # 0 - 2 - 1 - 3 - 4 - 5
            #         |   |-> curr = head  
            #         |-> head  = prevGrpEnd
            #  
            prevGrpEnd = head
            head = curr

        return dummy.next



