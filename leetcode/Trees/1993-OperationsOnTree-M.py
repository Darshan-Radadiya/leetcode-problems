from collections import deque
class LockingTree:

    def __init__(self, parent: list[int]):
        self.parent = parent
        self.lockedNodes = {} # node : user
        self.child = {i : [] for i in range(len(parent))}
        for i in range(1, len(parent)):
            self.child[parent[i]].append(i)

    def lock(self, num: int, user: int) -> bool:
        if num in self.lockedNodes:
            return False
        else:
            self.lockedNodes[num] = user
            return True

    def unlock(self, num: int, user: int) -> bool:
        if num in self.lockedNodes and self.lockedNodes[num] == user:
            del self.lockedNodes[num]
            return True
        else:
            return False

    def upgrade(self, num: int, user: int) -> bool:
        i = num
        while i != -1:
            if i in self.lockedNodes:
                return False
            i = self.parent[i]
        
        isDescendentLocked = False
        q = deque()
        q.append(num)
        while q:
            curr = q.popleft()
            if curr != num and curr in self.lockedNodes:
                isDescendentLocked=True
                del self.lockedNodes[curr]
            #  check if its a parent node then add its child to the current queue.
            if curr in self.child:
                for i in self.child[curr]:
                    q.append(i)
        
        if isDescendentLocked:
            self.lockedNodes[num] = user
        return isDescendentLocked

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)