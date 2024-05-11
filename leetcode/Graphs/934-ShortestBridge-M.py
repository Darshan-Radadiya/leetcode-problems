from typing import List
from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # Our goal is tp find the shortest path in graph. 
        # For SP we have two options 1. Dijkstra's and BFS.
        # Dijkstra doesn't support Multi source that's why we will use BFS.
        # Our approach will be to find the first position of Island (first 1 in grid) and from this position we will 
        # Run DFS to cover the current Island. and add the visited into the queue.
        # Once we are done with the current island. run the BFS level by level and once we found the first cell with value 1.
        # return the current level length. 

        visited = set()
        q = deque()
        ROWS = len(grid) 
        COLS = len(grid[0]) 
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r,c):
            if min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0 or (r,c) in visited:
                return 
            visited.add((r,c))
            q.append([r,c])
            for dr, dc in directions:
                dfs(dr+r, dc+c)
        
        def bfs():
            level = 0
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in directions:
                        row, col = r + dr, c + dc
                        if  min(row,col) < 0 or row == ROWS or col == COLS or (row,col) in visited:
                            continue
                        if grid[row][col] == 1:
                            return level
                        q.append([row, col])
                        visited.add((row,col))             
                level += 1 
            return level
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r,c)
                    return bfs()
        

grid = [[0,1,0],[0,0,0],[0,0,1]]
sol = Solution()
Output = sol.shortestBridge(grid)
ExpectedOutput = 2
print("Output is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and Space Complexity is: O(Row * Col)\n" )