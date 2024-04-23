from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def exploreIsland(grid, r, c, visited):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visited or grid[r][c] == 0:
                return 0
            visited.add((r,c))
            islandSize = 1
            islandSize += exploreIsland(grid, r - 1, c, visited) 
            islandSize += exploreIsland(grid, r + 1, c, visited) 
            islandSize += exploreIsland(grid, r, c - 1, visited) 
            islandSize += exploreIsland(grid, r, c + 1, visited)
            return islandSize

        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == 1:
                    currIslandSize = exploreIsland(grid, r, c, visited)
                    res = max(res, currIslandSize)
        return res

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
ExpectedOutput = 6
sol  = Solution()
Output = sol.maxAreaOfIsland(grid) 
print("Output is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and Space Complexity is: O(Row * Col)\n" )