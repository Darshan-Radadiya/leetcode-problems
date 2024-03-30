from typing import List
from collections import defaultdict, deque
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # create a adjacency list of manager to its employee
        adjacencyList = defaultdict(list) 
        for i in range(n):
            adjacencyList[manager[i]].append(i)

        # now run BFS
        q = deque()
        q.append((headID, 0))
        timeNeeded = 0
        while q:
            managerId, time = q.popleft()
            timeNeeded = max(timeNeeded, time)
            for emp in adjacencyList[managerId]:
                q.append((emp, time + informTime[managerId])) 
        return timeNeeded

sol = Solution()
n = 6
headID = 2
manager = [2,2,-1,2,2,2]
informTime = [0,0,1,0,0,0]
ExpectedOutput = 1
Output = sol.numOfMinutes(n, headID, manager, informTime) 
print("\nOutput is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(n)\n" )
