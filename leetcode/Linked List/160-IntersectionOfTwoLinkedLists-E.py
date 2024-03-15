# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# THIS SOLUTION USES THE EXTRA O(N) SPACE AND ITS MODIFIES THE ORIGINAL LIST. 
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        # Find the end of headA list
        currentA = headA
        while currentA.next:
            currentA = currentA.next
        
        # Temporarily connect the end of list A to the start of list B, creating a cycle
        currentA.next = headB
        
        slow = fast = headA
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = headA
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                
                # Before returning, restore the original structure by disconnecting A and B
                currentA.next = None
                return slow
        
        # Restore the original structure by disconnecting A and B before returning None
        currentA.next = None
        return None


# Optimized solution
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a

# Visualization of this solution:
# Case 1 (Have Intersection & Same Len):

#        a
# A:     a1 → a2 → a3
#                    ↘
#                      c1 → c2 → c3 → null
#                    ↗            
# B:     b1 → b2 → b3
#        b

#             a
# A:     a1 → a2 → a3
#                    ↘
#                      c1 → c2 → c3 → null
#                    ↗            
# B:     b1 → b2 → b3
#             b

#                  a
# A:     a1 → a2 → a3
#                    ↘
#                      c1 → c2 → c3 → null
#                    ↗            
# B:     b1 → b2 → b3
#                  b
# A:     a1 → a2 → a3
#                    ↘ a
#                      c1 → c2 → c3 → null
#                    ↗ b            
# B:     b1 → b2 → b3
# Since a == b is true, end loop while(a != b), return the intersection node a = c1.

# Case 2 (Have Intersection & Different Len):


#             a
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3 → null
#                    ↗            
# B:     b1 → b2 → b3
#        b

#                  a
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3 → null
#                    ↗            
# B:     b1 → b2 → b3
#             b

# A:          a1 → a2
#                    ↘ a
#                      c1 → c2 → c3 → null
#                    ↗            
# B:     b1 → b2 → b3
#                  b
# A:          a1 → a2
#                    ↘      a
#                      c1 → c2 → c3 → null
#                    ↗ b           
# B:     b1 → b2 → b3
# A:          a1 → a2
#                    ↘           a
#                      c1 → c2 → c3 → null
#                    ↗      b           
# B:     b1 → b2 → b3
# A:          a1 → a2
#                    ↘                a = null, then a = b1
#                      c1 → c2 → c3 → null
#                    ↗           b           
# B:     b1 → b2 → b3

# A:          a1 → a2
#                    ↘ 
#                      c1 → c2 → c3 → null
#                    ↗                b = null, then b = a1 
# B:     b1 → b2 → b3
#        a

#             b         
# A:          a1 → a2
#                    ↘ 
#                      c1 → c2 → c3 → null
#                    ↗
# B:     b1 → b2 → b3
#             a

#                  b         
# A:          a1 → a2
#                    ↘ 
#                      c1 → c2 → c3 → null
#                    ↗ 
# B:     b1 → b2 → b3
#                  a
# A:          a1 → a2
#                    ↘ b
#                      c1 → c2 → c3 → null
#                    ↗ a
# B:     b1 → b2 → b3
# Since a == b is true, end loop while(a != b), return the intersection node a = c1.

# Case 3 (Have No Intersection & Same Len):

#        a
# A:     a1 → a2 → a3 → null
# B:     b1 → b2 → b3 → null
#        b
#             a
# A:     a1 → a2 → a3 → null
# B:     b1 → b2 → b3 → null
#             b
#                  a
# A:     a1 → a2 → a3 → null
# B:     b1 → b2 → b3 → null
#                  b
#                       a = null
# A:     a1 → a2 → a3 → null
# B:     b1 → b2 → b3 → null
#                       b = null
# Since a == b is true (both refer to null), end loop while(a != b), return a = null.

# Case 4 (Have No Intersection & Different Len):

#        a
# A:     a1 → a2 → a3 → a4 → null
# B:     b1 → b2 → b3 → null
#        b
#             a
# A:     a1 → a2 → a3 → a4 → null
# B:     b1 → b2 → b3 → null
#             b
#                  a
# A:     a1 → a2 → a3 → a4 → null
# B:     b1 → b2 → b3 → null
#                  b
#                       a
# A:     a1 → a2 → a3 → a4 → null
# B:     b1 → b2 → b3 → null
#                       b = null, then b = a1
#        b                   a = null, then a = b1
# A:     a1 → a2 → a3 → a4 → null
# B:     b1 → b2 → b3 → null
#             b                   
# A:     a1 → a2 → a3 → a4 → null
# B:     b1 → b2 → b3 → null
#        a
#                  b
# A:     a1 → a2 → a3 → a4 → null
# B:     b1 → b2 → b3 → null
#             a
#                       b
# A:     a1 → a2 → a3 → a4 → null
# B:     b1 → b2 → b3 → null
#                  a
#                            b = null
# A:     a1 → a2 → a3 → a4 → null
# B:     b1 → b2 → b3 → null
#                       a = null
# Since a == b is true (both refer to null), end loop while(a != b), return a = null.

# Notice that if list A and list B have the same length, this solution will terminate in no more than 1 traversal; 
# if both lists have different lengths, 
#   this solution will terminate in no more than 2 traversals -- 
#   in the second traversal, swapping a and b synchronizes a and b before the end of the second traversal. 
#   By synchronizing a and b I mean both have the same remaining steps in the second traversal 
#   so that it's guaranteed for them to reach the first intersection node, 
#   or reach null at the same time (technically speaking, in the same iteration) -- 
# see Case 2 (Have Intersection & Different Len) and Case 4 (Have No Intersection & Different Len).