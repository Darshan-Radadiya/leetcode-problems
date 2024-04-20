from typing import List
from collections import deque
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = set()
        adj = {}

        for a, b in connections:
            edges.add((a,b))
            if a not in adj:
                adj[a] = []
            if b not in adj:
                adj[b] = []
            adj[a].append(b)
            adj[b].append(a)
        
        #  DFS
        visited = set()
        def dfs(city, changes):
            visited.add(city) 
            for nei in adj[city]:
                if nei not in visited:
                    if (nei, city) not in edges:
                        changes += 1
                    changes = dfs(nei, changes)
            return changes
        return dfs(0, 0)

        #  BFS
        q = deque([0])
        changes = 0
        while q:
            city = q.popleft()
            visited.add(city)
            for nei in adj[city]:
                if nei not in visited:
                    if (nei, city) not in edges:
                        changes += 1
                    q.append(nei)
        return changes
            
n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
sol = Solution()
Output = sol.minReorder(n, connections)
ExpectedOutput = 3
print("Output is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and Space Complexity is: O(N)\n" )