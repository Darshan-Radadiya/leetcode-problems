class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.heapList = [float("-inf")]
        self.currentSize = 0
        self.k = k
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        if self.currentSize < self.k:
            self.insertEle(val)
        elif val > self.heapList[1]:
            self.deleteMinEle()
            self.insertEle(val)
        return self.heapList[1]
    
    def insertEle(self, val):
        self.heapList.append(val) # add ele at last index of current list
        self.currentSize += 1 # increment current size of list by 1.
        self.shiftUp(self.currentSize)

    def shiftUp(self, i):
        while i // 2 > 0:
            if self.heapList[i//2] < self.heapList[i]: # check current node and its parent node.
                self.heapList[i//2], self.heapList[i] = self.heapList[i], self.heapList[i//2] # swap of parent is greater then current.
            i = i // 2 # Go one level up

    def deleteMinEle(self):
        if self.currentSize == 1:
            return "Empty heap list"
        else:
            root = self.heapList[1]
            self.heapList[1] = self.heapList[self.currentSize]
            self.currentSize -= 1
            self.heapList.pop()
            self.shiftDown(1)
            return root
        
    def shiftDown(self, i):
        while (i * 2) < self.currentSize:
            minChild = self.minChild(i)
            if self.heapList[minChild] < self.heapList[i]:
                self.heapList[minChild], self.heapList[i] =  self.heapList[i], self.heapList[minChild]
            else:
                return
            i = minChild

    def minChild(self, i):
        if (i * 2) + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[(i * 2) + 1] < self.heapList[( i * 2)]:
                return i * 2
            else:
                return (i * 2) + 1


kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))   # return 4
print(kthLargest.add(5))   # return 5
print(kthLargest.add(10))  # return 5
print(kthLargest.add(9))   # return 8
print(kthLargest.add(4))   # return 8