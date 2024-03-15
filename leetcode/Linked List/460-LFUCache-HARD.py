from typing import Collections

class Node():
    def __init__(self,value,prev=None, next=None):
        self.val = value
        self.next = next
        self.prev = prev

class LinkedList():
    def __init__(self):
        self.head = Node(0,0)
        self.tail = Node(0,self.head)
        self.head.next = self.tail
        self.map = {} # {val : node}
    
    def insertRight(self, val):
        new_node = Node(val, self.tail.prev, self.tail)
        self.map[val] = new_node
        self.tail.prev = new_node
        new_node.prev.next = new_node
    
    def length(self):
        return len(self.map)
    
    def pop(self,val):
        if val in self.map:
            currNode = self.map[val]
            next, prev = currNode.next, currNode.prev
            next.prev = prev
            prev.next = next
            self.map.pop(val, None)
    
    def popLeft(self):
        res = self.head.next.val
        self.pop(res)
        return res
    
    def update(self,val):
        self.pop(val)
        self.insertRight(val)

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.lfucnt = 0
        self.valMap = {}
        self.countMap = Collections.defaultdict(int)
        self.listMap = Collections.defaultdict(LinkedList)
         
    def counter(self,key):
        cnt = self.countMap[key]
        self.countMap[key] += 1
        self.listMap[cnt].pop(key)
        self.listMap[cnt + 1].insertRight(key)

        if cnt == self.lfucnt and self.listMap[cnt].length() == 0:
            self.lfucnt += 1
    def get(self, key: int) -> int:
        if key not in self.valMap:
            return -1
        self.counter(key)
        return self.valMap[key]  

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return 
        if key not in self.valMap and len(self.valMap) == self.cap:
            res = self.listMap[self.lfucnt].popLeft()
            self.valMap.pop(res)
            self.countMap.pop(res)

        self.valMap[key] = value
        self.counter(key)
        self.lfucnt = min(self.lfucnt,self.countMap[key])
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)