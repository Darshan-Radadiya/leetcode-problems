from typing import List
from collections import deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for i in range(numCourses)]
        for u, v in prerequisites:
            adj[u].append(v)
        
        # step 1 - create inDegree list
        inDegree = [0]*numCourses
        for u in range(numCourses):
            for v in adj[u]:
                inDegree[v] += 1
        
        # Step 2 - Append 0 InDegree node to Queue.
        q = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
            
        #  Step 3 - Process the queue.
        prereqMap = {i:set() for i in range(numCourses)} # map course -> set indirect prerequisites.
        while (q):
            u = q.popleft()
            for v in adj[u]:
                inDegree[v] -= 1
                prereqMap[v].add(u)
                prereqMap[v].update(prereqMap[u])
                if inDegree[v] == 0:
                    q.append(v)
        res = []
        for u, v in queries:
            res.append(u in prereqMap[v])
        return res


numCourses = 3
prerequisites = [[1,2],[1,0],[2,0]]
queries = [[1,0],[1,2]]
sol = Solution()
Output = sol.checkIfPrerequisite(numCourses, prerequisites, queries)
ExpectedOutput = [True, True]
print("Output is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time Complexity is: O(m + n + n*n + z) -> O(n^2) and Space O(n*n + n + n*n + n + z) -> O(n^2) where, m = len(prereqs) and z = len(queries)\n" )