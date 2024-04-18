class Solution:
    def numIslands(self, grid):
        
        if not grid:
            return 

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        numberOfIsland = 0

        #recursive 
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visited or grid[r][c] == "0":
                return  
            visited.add((r,c))

            dfs(r - 1, c)  # Up
            dfs(r + 1, c)  # Down
            dfs(r, c - 1)  # Left
            dfs(r, c + 1)  # Right

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    numberOfIsland += 1
                    dfs(r,c)
        return numberOfIsland
    
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
sol = Solution()
Output = sol.numIslands(grid)
ExpectedOutput = 1
print("Output is:      ", Output ,"\n" )
print("Expected Output:",ExpectedOutput,"\n" )
print("The output matches with expected Output: ", ExpectedOutput == Output, "\n" )
print("Time and Space Complexity is: O(Row * Col)\n" )