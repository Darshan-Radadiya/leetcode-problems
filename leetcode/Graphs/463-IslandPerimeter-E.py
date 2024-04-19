from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        def exploreIsland(grid, r, c, visited):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 1
            if (r,c) in visited:
                return 0
            visited.add((r,c))
            perimeter = exploreIsland(grid, r - 1, c, visited) + exploreIsland(grid, r + 1, c, visited) + exploreIsland(grid, r, c - 1, visited) + exploreIsland(grid, r, c + 1, visited)
            return perimeter 
                
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return exploreIsland(grid, r, c, visited)
                
grid = [[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]]
sol = Solution()
Output = sol.islandPerimeter(grid)
ExpectedOutput = 16
print("Output is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and Space Complexity is: O(Row * Col)\n" )