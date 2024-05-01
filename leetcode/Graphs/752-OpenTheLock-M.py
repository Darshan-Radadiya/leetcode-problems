from typing import List
from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        def getChild(lock):
            children = []
            for i in range(4):
                incrementDigit = str((int(lock[i]) + 1) % 10)
                children.append(lock[:i] + incrementDigit + lock[i+1:])
                decrementDigit = str((int(lock[i]) - 1 + 10) % 10)
                children.append(lock[:i] + decrementDigit + lock[i+1:])
            return children


        q = deque()
        q.append(["0000", 0])
        visited = set(deadends) # added deadends bcs we don't want to visit this values.
        while q:
            lock, moves = q.popleft()
            if lock == target:
                return moves
            for child in getChild(lock):
                if child not in visited:
                    visited.add(child)
                    q.append([child, moves + 1])
        return -1

deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
sol = Solution()
Output = sol.openLock(deadends, target)
ExpectedOutput =  6
print("Output is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and Space Complexity is: O(10000) bcs in worst case our target is 9999\n" )