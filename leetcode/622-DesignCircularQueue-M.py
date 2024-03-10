#  We will solve this problem with three different approach:

#-------------------------------------------------
#------------ Approach 1: - Array ----------------
#-------------------------------------------------

class MyCircularQueue:

    def __init__(self, k: int):
        self.cQueue = [None] * k
        self.k = k
        self.position = 0
        self.head = 0
        self.tail = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull(): 
            return False
        else:
            self.cQueue[self.tail] = value
            self.tail = (self.tail+1)%self.k # to handle tail position > k
            self.position += 1
            return True

    def deQueue(self) -> bool:
        if self.isEmpty(): 
            return False
        else:
            self.head = (self.head+1)%self.k # to handle head position > k
            self.position -= 1
            return True
        
    def Front(self) -> int:
        return -1 if self.isEmpty() else self.cQueue[self.head]
        
    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.cQueue[self.tail-1]
        
    def isEmpty(self) -> bool:
        return self.position == 0

    def isFull(self) -> bool:
        return self.position == self.k

#-------------------------------------------------
#------ Approach 2: - Singly Linked List ---------
#-------------------------------------------------
# class for ListNode
class ListNode():
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

class MyCircularQueueSinglyLinkedList:

    def __init__(self, k: int):
        self.k = k
        self.position = 0
        self.tail = self.head = None

    def enQueue(self, value: int) -> bool:
        if self.isFull(): 
            return False
        else:
            newNode = ListNode(value)
            if not self.head:
                self.head = self.tail = newNode
                self.head.next = self.head
            else:
                self.tail.next = newNode
                self.tail = newNode
                self.tail.next = self.head
            self.position += 1
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
            self.position -= 1
            return True
        
    def Front(self) -> int:
        return -1 if self.isEmpty() else self.head.val

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.tail.val

    def isEmpty(self) -> bool:
        return self.position == 0

    def isFull(self) -> bool:
        return self.position == self.k
    
#-------------------------------------------------
#------ Approach 3: - Doubly Linked List ---------
#-------------------------------------------------
# class for ListNode
class ListNode2():
    def __init__(self,val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
class MyCircularQueueDoublyLinkedList:

    def __init__(self, k: int):
        self.k = k
        self.left = ListNode2(0, None, None)
        self.right = ListNode2(0, self.left, None)
        self.left.next = self.right

    def enQueue(self, value: int) -> bool:
        if self.isFull(): 
            return False
        else:
            curr = ListNode2(value, self.right.prev, self.right)
            self.right.prev.next = curr
            self.right.prev = curr
            self.k -= 1
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.left.next = self.left.next.next
            self.left.next.prev = self.left
            self.k += 1
            return True
        
    def Front(self) -> int:
        return -1 if self.isEmpty() else self.left.next.val

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.right.prev.val

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.k == 0
    

operations = ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
values = [[3], [1], [2], [3], [4], [], [], [], [4], []]
output = []

operations = ["MyCircularQueueSinglyLinkedList", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
values = [[3], [1], [2], [3], [4], [], [], [], [4], []]
output = []

operations = ["MyCircularQueueDoublyLinkedList", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
values = [[3], [1], [2], [3], [4], [], [], [], [4], []]
output = []


ExpectedOutput = [None, True, True, True, False, 3, True, True, True, 4]
obj = None
for op, val in zip(operations, values):
    if op == "MyCircularQueue":
        obj = MyCircularQueue(*val)
        output.append(None)
    elif op == "MyCircularQueueLinkedList":
        obj = MyCircularQueueSinglyLinkedList(*val)
        output.append(None)
    elif op == "MyCircularQueueDoublyLinkedList":
        obj = MyCircularQueueDoublyLinkedList(*val)
        output.append(None)
    elif op == "enQueue":
        output.append(obj.enQueue(*val))
    elif op == "deQueue":
        output.append(obj.deQueue())
    elif op == "Rear":
        output.append(obj.Rear())
    elif op == "isFull":
        output.append(obj.isFull())
    else:
        output.append("Unsupported operation")

print("\nOutput is:      ", output ,"\n" )
print("Expected Output:", ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == output, "\n" )
print("Time Complexity is: O(1) and space is O(k)\n" )


