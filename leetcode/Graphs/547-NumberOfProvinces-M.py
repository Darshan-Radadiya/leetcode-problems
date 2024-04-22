from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # #  with adj list
        adj = {}
        ROWS = len(isConnected)
        COLS = len(isConnected[0])
        for r in range(ROWS):
            for c in range(COLS):
                if isConnected[r][c] == 1:
                    if r not in adj: adj[r] = []  
                    if c not in adj: adj[c] = [] 
                    adj[r].append(c)
                    adj[c].append(r) 
        
        def dfs(u):
            visited.add(u)
            for v in adj[u]:
                if v not in visited:
                    dfs(v)

        count = 0
        visited = set()
        for u in range(len(adj)):
            if u not in visited:
                dfs(u)
                count += 1
        return count

        #  without adj list
        def dfs(u):
            visited.add(u)
            for v in range(len(isConnected)):
                if v not in visited and isConnected[u][v] == 1:
                    dfs(v)

        count = 0
        visited = set()
        for u in range(len(isConnected)):
            if u not in visited:
                dfs(u)
                count += 1
        return count
    
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
sol = Solution()
Output = sol.findCircleNum(isConnected)
ExpectedOutput = 2
print("Output is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and Space Complexity is: O(Row * Col)\n" )