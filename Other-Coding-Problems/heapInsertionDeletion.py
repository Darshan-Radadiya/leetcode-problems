class MaxHeap():
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
    
    def insertEle(self, val):
        self.heapList.append(val) # add ele at last index of current list
        self.currentSize += 1 # increment current size of list by 1.
        self.shiftUp(self.currentSize)
    
    def shiftUp(self, i):
        while i // 2 > 0:
            if self.heapList[i//2] < self.heapList[i]: # check current node and its parent node.
                self.heapList[i//2], self.heapList[i] = self.heapList[i], self.heapList[i//2] # swap of parent is smaller then current.
            else:
                return
            i = i // 2 # Go one level up
    
    def deleteMaxEle(self):
        if self.currentSize == 1:
            return "Empty heap list"
        else:
            root = self.heapList[1]
            self.heapList[1] = self.heapList[self.currentSize]
                    # we can store this ele at the last just for copy or ref what are the nodes we deleted and 
                    # once we delete all the node this heapList will become sorted.
                    # self.heapList[self.currentSize] = root 
            self.heapList.pop()
            self.currentSize -= 1
            self.shiftDown(1)
            return root
        
    def shiftDown(self, i):
        while i * 2 < self.currentSize:
            maximumChild = self.maxChild(i)
            if self.heapList[maximumChild] > self.heapList[i]:
                self.heapList[maximumChild], self.heapList[i] =  self.heapList[i], self.heapList[maximumChild]
            else:
                return
            i = maximumChild

    def maxChild(self, i):
        if (i * 2) + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[(i * 2) + 1] > self.heapList[( i * 2)]:
                return (i * 2) + 1
            else:
                return i * 2

    def printHeap(self):
        return print(self.heapList[1:])
    
print("...Max Heap Insertion and deletion...")
MaxHeapObj = MaxHeap()
MaxHeapObj.insertEle(60)
MaxHeapObj.insertEle(50)
MaxHeapObj.insertEle(80)
MaxHeapObj.insertEle(90)
MaxHeapObj.insertEle(600)
MaxHeapObj.insertEle(650)
MaxHeapObj.printHeap() # [650, 90, 600, 50, 80, 60]
print(MaxHeapObj.deleteMaxEle()) # 650
print(MaxHeapObj.deleteMaxEle()) # 600
print(MaxHeapObj.deleteMaxEle()) # 90
print(MaxHeapObj.deleteMaxEle()) # 80
print(MaxHeapObj.deleteMaxEle()) # 60
print(MaxHeapObj.deleteMaxEle()) # Empty heap list

class MinHeap():
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
    
    def insertEle(self, val):
        self.heapList.append(val) # add ele at last index of current list
        self.currentSize += 1 # increment current size of list by 1.
        self.shiftUp(self.currentSize)
    
    def shiftUp(self, i):
        while i // 2 > 0:
            if self.heapList[i//2] > self.heapList[i]: # check current node and its parent node.
                self.heapList[i//2], self.heapList[i] = self.heapList[i], self.heapList[i//2] # swap of parent is greater then current.
            else:
                return
            i = i // 2 # Go one level up
    
    def deleteMinEle(self):
        if self.currentSize == 1:
            return "Empty heap list"
        else:
            root = self.heapList[1]
            self.heapList[1] = self.heapList[self.currentSize]
                    # we can store this ele at the last just for copy or ref what are the nodes we deleted and 
                    # once we delete all the node this heapList will become sorted.
                    # self.heapList[self.currentSize] = root 
            self.heapList.pop()
            self.currentSize -= 1
            self.shiftDown(1)
            return root
        
    def shiftDown(self, i):
        while (i * 2) < self.currentSize:
            minimumChild = self.minChild(i)
            if self.heapList[minimumChild] < self.heapList[i]:
                self.heapList[minimumChild], self.heapList[i] =  self.heapList[i], self.heapList[minimumChild]
            else:
                return
            i = minimumChild

    def minChild(self, i):
        if (i * 2) + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[(i * 2) + 1] < self.heapList[( i * 2)]:
                return (i * 2) + 1
            else:
                return i * 2

    def printHeap(self):
        return print(self.heapList[1:])
    
print("...Min Heap Insertion and deletion...")
MinHeapObj = MinHeap()
MinHeapObj.insertEle(60)
MinHeapObj.insertEle(50)
MinHeapObj.insertEle(80)
MinHeapObj.insertEle(90)
MinHeapObj.insertEle(600)
MinHeapObj.insertEle(650)
MinHeapObj.printHeap() # [50, 60, 80, 90, 600, 650]
print(MinHeapObj.deleteMinEle()) # 50
print(MinHeapObj.deleteMinEle()) # 60
print(MinHeapObj.deleteMinEle()) # 80
print(MinHeapObj.deleteMinEle()) # 90
print(MinHeapObj.deleteMinEle()) # 600
print(MinHeapObj.deleteMinEle()) # Empty heap list