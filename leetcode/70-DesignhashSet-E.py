class LinkedList:
    def __init__(self,key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.hashSet = [LinkedList(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        indx = key % len(self.hashSet)
        curr = self.hashSet[indx]
        while curr.next:
            if curr.next.key == key:
                return 
            curr = curr.next
        curr.next = LinkedList(key)

    def remove(self, key: int) -> None:
        indx = key % len(self.hashSet)
        curr = self.hashSet[indx]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        indx = key % len(self.hashSet)
        curr = self.hashSet[indx]
        while curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)