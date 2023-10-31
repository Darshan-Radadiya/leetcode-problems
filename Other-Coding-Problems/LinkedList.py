class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertNodeAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node

    def deleteElementAtEnd(self):
        if self.head is None:
            return
        else:
            curr_node = self.head
            while curr_node.next.next:
                curr_node = curr_node.next
            curr_node.next = None

    def insertNodeAtStart(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def deleteElementAtStart(self):
        if self.head is None:
            return
        else:
            self.head = self.head.next

    def insertNodeAtIndex(self,data, index):
        new_node = Node(data)
        # Checking Index
        if index < 0:
            print("Index must be greater than 0")
            return
        
        # Checking is Linked List is not empty
        if self.head is None:
            self.head = new_node
            return
        
        # Checking if index 0 then insert at the beginning of the LL.
        position = 0
        if index == position:
            # insertNodeAtStart(data)
            new_node.next = self.head
            self.head = new_node
            return
        else:
            curr_node = self.head
            while curr_node and position < index - 1:
                curr_node = curr_node.next
                position += 1
            if curr_node:
                new_node.next = curr_node.next
                curr_node.next = new_node
            else:
                print("Index not present!!!")
                return
            
    def deleteElementAtIndex(self, index):
        # Checking Index
        if index < 0:
            print("Index must be greater than 0")
            return
        
        # Checking is Linked List is not empty
        if self.head is None:
            return
        
        position = 0
        curr_node = self.head
        if position == index:
            self.head = curr_node.next
        else:
            while curr_node and position < index + 1:
                position += 1
                curr_node = curr_node.next
            if curr_node and curr_node.next:
                curr_node.next = curr_node.next.next
            else:
                print("Index Not present")

        
    def deleteElementWithValue(self, data):
        if self.head is None:
            return
        else:
            curr_node = self.head
            while curr_node and curr_node.data != data:
                curr_node = curr_node.next
            
            if curr_node is None:
                return
            else:
                curr_node.next = curr_node.next.next
            
            
    def printLinkedList(self):
        curr_node = self.head
        while(curr_node):
            print("I am data", curr_node.data)
            curr_node = curr_node.next



ll = LinkedList()
ll.insertNodeAtStart(0)

ll.insertNodeAtEnd(1)
ll.insertNodeAtEnd(10)
ll.insertNodeAtEnd(100)

ll.insertNodeAtIndex(5,2)
ll.insertNodeAtIndex(50,4)

ll.printLinkedList()

print(" Insertion (beginning -- O(1)")
print(" Insertion (end)      -- O(n)")
print(" Insertion (specific) -- O(n)")
print(" Deletion (beginning) -- O(1)")
print(" Deletion (end)       -- O(n)")
print(" Deletion (specific)  -- O(n)")
print(" Printing (traversal) -- O(n)")